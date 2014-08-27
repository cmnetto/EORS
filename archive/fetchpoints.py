#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nettoc
#
# Created:     13/01/2014
# Copyright:   (c) nettoc 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# import system modules
import arcpy
from arcpy import env

# Set environment settings
arcpy.env.workspace = (r'L:\work\nettoc\MAS201300311\PythonModule\import_data')

try:
    # Set the local variables
    in_Table = "TEST2.txt"
    x_coords = "SURF_LATITUDE"
    y_coords = "SURF_LONGITUDE"
    z_coords = "WATER_DEPTH"
    out_Layer = "points_layer"
    saved_Layer = r"c:\output\test.lyr"

    # Set the spatial reference
    spRef = r"L:\work\nettoc\MAS201300311\PythonModule\import_data\POI.prj"

    # Make the XY event layer...
    arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

    # Print the total rows
    print arcpy.GetCount_management(out_Layer)

    # Save to a layer file
    arcpy.SaveToLayerFile_management(out_Layer, saved_Layer)

except:
    # If an error occurred print the message to the screen
    print arcpy.GetMessages()


