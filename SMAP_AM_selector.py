import os
rootdir = os.getcwd()

print(rootdir)

#Print a list of AM retrievals:            
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = file
        
        if ("AM_soil_moisture") in filepath:
            print (filepath) 


#print a list of PM retrievals:            
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = file
        
        if ("AM_soil_moisture") in filepath:
            print (filepath)
            
"""
Separate AM files and PM files into separate folders. 
Will want to create paralel time series of each, can possibly take an average
if both present or use the one reading if missing data for either reading.
"""

"""
#Loop through the folders, selecting AM/PM and moving them to a pre-created subfolder - 

newfilepath = "D:\CD_Newton_06_06AM\SMAP\SMAP_TS_AM" + os.sep + file
os.rename(filepath, newfilepath)
print(newfilepath)
"""

#Move the AM retrievals to a subfolder:            
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        
        if ("AM_soil_moisture") in filepath:
            print (filepath)
            newfilepath = "D:\CD_Newton_06_06AM\SMAP\SMAP_TS_AM" + os.sep + file
            os.rename(filepath, newfilepath)
            print("moved to")
            print(newfilepath)
            
#Move the PM retrievals to a subfolder:            
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        
        if ("PM_soil_moisture") in filepath:
            print (filepath)
            newfilepath = "D:\CD_Newton_06_06AM\SMAP\SMAP_TS_PM" + os.sep + file
            os.rename(filepath, newfilepath)
            print("moved to")
            print(newfilepath)       
