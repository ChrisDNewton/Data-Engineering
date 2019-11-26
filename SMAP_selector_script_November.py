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


##print a list of PM retrievals:            
#for subdir, dirs, files in os.walk(rootdir):
#    for file in files:
#        #print os.path.join(subdir, file)
#        filepath = file
#        
#        if ("AM_soil_moisture") in filepath:
#            print (filepath)
        

"""
#Loop through the folders, selecting AM/PM and moving them to a pre-created subfolder - 

newfilepath = "C:\Research_work\COSMOS-SMAP_2\SMAP_V3_AM\SMAP_timeseries" + os.sep + file
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
            newfilepath = "C:\Research_work\COSMOS-SMAP_2\SMAP_V3_AM\SMAP_timeseries" + os.sep + file
            os.rename(filepath, newfilepath)
            print("moved to")
            print(newfilepath)
 
"""           
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
"""
            