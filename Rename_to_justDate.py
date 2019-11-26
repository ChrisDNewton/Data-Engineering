"""
Renaming .tif files to just the date the image was collected (for a tidier dataframe)
Be careful though, this removes all info about the sensor, so ensure files are kept in the correct folders.
"""

#Set working directory either with the bar in the top right (in Spyder) 
#or with os.chdir("/path/to/yourDirectory")

import os
rootdir = os.getcwd()

print(rootdir)

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('tif'):
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            print (filepath)
            #15:23 is the section of the filename which refers to the date:
            newfilepath = file[15:23] + '.tif' 
            os.rename(file, newfilepath)
            print("moved to")
            print(newfilepath)
            
"""
Now we'll subset into months by selecting 4:6 of the file name.
(6 is the stopping character, note included in selection, so
4:6 will grab numbers 4 and 5 - remember Python starts counting at 0)
i.e. if file[4:6] = '01':
    newfilepath = "januaryFolder/" + os.sep + file
            os.rename(filepath, newfilepath)
"""

#Refresh the root directory as the filenames have now been changed.
rootdir = os.getcwd()

print(rootdir)


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('tif'):
            filepath = subdir + os.sep + file
            if file[4:6] == '01':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Jan" + os.sep + file
                os.rename(filepath, newfilepath)
            elif file[4:6] == '02':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Feb" + os.sep + file
                os.rename(filepath, newfilepath)
            elif file[4:6] == '03':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Mar" + os.sep + file
                os.rename(filepath, newfilepath)                
            elif file[4:6] == '04':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Apr" + os.sep + file
                os.rename(filepath, newfilepath)
            elif file[4:6] == '05':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/May" + os.sep + file
                os.rename(filepath, newfilepath)      
            elif file[4:6] == '06':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Jun" + os.sep + file
                os.rename(filepath, newfilepath)
            elif file[4:6] == '07':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Jul" + os.sep + file
                os.rename(filepath, newfilepath)                
            elif file[4:6] == '08':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Aug" + os.sep + file
                os.rename(filepath, newfilepath)
            elif file[4:6] == '09':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Sep" + os.sep + file
                os.rename(filepath, newfilepath)    
            elif file[4:6] == '10':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Oct" + os.sep + file
                os.rename(filepath, newfilepath)                
            elif file[4:6] == '11':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Nov" + os.sep + file
                os.rename(filepath, newfilepath)
            elif file[4:6] == '12':
                newfilepath = "C:/Research_work/COSMOS-SMAP_2/SMAP_V3_AM/SMAP_timeseries_months/Dec" + os.sep + file
                os.rename(filepath, newfilepath)  
        