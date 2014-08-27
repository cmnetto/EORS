import arcpy

# Retrieve input Parameters
inX = 2047347.50
inY = 1702783.40
inDescription = "new well"

indidentsFC = "L:\\work\\nettoc\\MAS201300311\\PythonModule\\import_data\\POI.shp"
descriptionField = "DESCR"

#Create a point
inPoint = arcpy.Point(inX, inY)

#Create the insert cursor and a new empty row
rowInserter = arcpy.InsertCursor(indidentsFC)
newIncident = rowInserter.newRow()

#Populate attributtes of new row
newIncident.SHAPE = inPoint
newIncident.setValue(descriptionField, inDescription)

# Insert the new row into the shapefile
rowInserter.insertRow(newIncident)

#Clean up
del rowInserter