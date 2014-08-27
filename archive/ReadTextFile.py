# import system modules
import arcpy, csv
##from arcpy import env

# Set environment settings
##arcpy.env.workspace = (r'L:\work\nettoc\MAS201300311\PythonModule\import_data')

f = open('L:/work/nettoc/MAS201300311/PythonModule/import_data/TEST2.txt')
r = csv.DictReader(f)
