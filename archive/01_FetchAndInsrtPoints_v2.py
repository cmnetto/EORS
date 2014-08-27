
# 1. open text file
# 2. read the header line
# 3. Loop through header line to find the index position of the lat and long value
# 4. Read the rest of the lines
# 5. Split  each line into a list of values, using the "," as a delimiter
# 6. Find the values in the list that coorespond to the lat and long coords and
#       write them a list
# 7. From the newly created coord list right to a point file

import arcpy, fileinput, os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "M:\work\nettoc\MAS201300311\PythonModule\import_data"
fc = "newPointFile.shp"
arcpy.CreateFeatureclass_management("M:\work\nettoc\MAS201300311\PythonModule\import_data", fc, "POINT")

out_path = r"M:\work\nettoc\MAS201300311\PythonModule\import_data"
pointFC = r"M:\work\nettoc\MAS201300311\PythonModule\import_data\POI.shp"
geoType = "POINT"
StructurePoints = open(r"M:\work\nettoc\MAS201300311\PythonModule\import_data\TEST2.txt", "r")
coordList = []


# Parse the exported text file and create a list that Python can read

# figure out position of the lat and long in the header
headerLine = StructurePoints.readline()
valueList = headerLine.split(",")

latValueIndex = valueList.index('"SURF_LATITUDE"')
longValueIndex = valueList.index('"SURF_LONGITUDE"')
planValueIndex = valueList.index('"PLAN"')
typeValueIndex = valueList.index('"PLAN_SITE_TYPE"')
ancRadiusValueIndex = valueList.index('"ANCHOR_RADIUS"')

# Read line in the file and append to coordinate list
for line in StructurePoints.readlines():
    # need to say what the seperating value is, in this case its the ","
    segmentedLine = line.split(",")
    # only append the value (index) indicated... we could have used "segmentedline[2]", but if lat changes position in the header list
    # we would have to change the index number.
    coordList.append([segmentedLine[planValueIndex], segmentedLine[typeValueIndex], segmentedLine[ancRadiusValueIndex], segmentedLine[longValueIndex], segmentedLine[latValueIndex]])

print "MS Access export file accepted..."
#-------------
# Loop and delete any existing features in the shapefile
##rows = arcpy.UpdateCursor(pointFC)
##
##for row in rows:
##    rows.deleteRow(row)
##del rows, row
##print "Prepairing shape file..."
#-------------
# Loop through new created coordlist and insert the the points in the existing shape file
rowInserter = arcpy.InsertCursor(fc)

#Loop through each coordinate in the list
for coordinate in coordList:

    # Grab a set of coordinates from the list and assign them to a point obejct
    LONGVALUE = float(coordinate[3])
    LATVALUE = float(coordinate[4])
    pointGeometry = arcpy.Point()
    pointGeometry.X = LONGVALUE
    pointGeometry.Y = LATVALUE
##    pointGeometry.remove("Nan Nan")
    print pointGeometry

    # use the insert cursor to put in the point object in the feature class
    newPoint = rowInserter.newRow()
    newPoint.Shape = pointGeometry
    newPoint.DESCR = coordinate[0] + ", " + coordinate[1]
    newPoint.ANCHOR_RAD = coordinate[2]
    newPoint.x = pointGeometry.X
    newPoint.y = pointGeometry.Y
    rowInserter.insertRow(newPoint)


# clean up
del rowInserter
StructurePoints.close()
print "The following points were created"
print coordList
#-------------





