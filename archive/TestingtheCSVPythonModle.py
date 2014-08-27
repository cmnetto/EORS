
# Just practicing with the CSV Module http://docs.python.org/2/library/csv.html

# import system modules
import arcpy, csv
##from arcpy import env

# Set environment settings
##arcpy.env.workspace = (r'L:\work\nettoc\MAS201300311\PythonModule\import_data')

f = open('L:/work/nettoc/MAS201300311/PythonModule/import_data/TEST2.txt')
##r = csv.DictReader(f)


with f as r:
    reader = csv.reader(r)
    for row in reader:
        print row


