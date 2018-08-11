TempAlert daily data download script downloadtempdata8.py
#Last Updated 20141014
#version 8: updated to remove POD #6 & 7 and to replace tempalert device 10.220.25.6 with POD #6 & 7 device 10.220.25.8

#script first generates the date and formats it properly for use as a filename
#script connects directly to TempAlert units and opens yesterday's logfile
#script saves data from logfile to persistent text file, stripping superfluous characters
#script copies data from persistent text file (that is used in importing data to MS Access database with Macro) to archival text file in another folder

import urllib.request
import datetime
import shutil
#import re

#Get today's date and format properly
now = datetime.datetime.now()

year = str(now.year)
month =now.month
day = now.day - 1
# day is -1 because it is yesterday's data

#properly format month and day to always have at least two digits
if month < 10:
    month = str('0{}'.format(month))
if day < 10:
    day = str('0{}'.format(day))

date = '{}-{}-{}'.format(year, month, day)

##DEBUG checkpoint - date
#print(date)

#generate new file name

filevar1 = '{}_P1.txt'.format(date)
filevar2 = '{}_P23.txt'.format(date)
filevar3 = '{}_P45.txt'.format(date)

##DEBUG checkpoint - write filenames
print('writing... ' + filevar1)
print('writing... ' + filevar2)
print('writing... ' + filevar3)

#open files for writing
outfile1 = open("R:\\Research and Development\\Greenhouse\\TempAlert\\P1-tempdata.txt", 'w')
outfile2 = open("R:\\Research and Development\\Greenhouse\\TempAlert\\P23-tempdata.txt", 'w')
outfile3 = open("R:\\Research and Development\\Greenhouse\\TempAlert\\P45-tempdata.txt", 'w')

#get temperature data and write to file
f1 = urllib.request.urlopen('http://10.220.25.5/logfile.rb?lf=1')
f2 = urllib.request.urlopen('http://10.220.25.8/logfile.rb?lf=1')
f3 = urllib.request.urlopen('http://10.220.25.7/logfile.rb?lf=1')

for line in f1:
    line = line.decode('utf-8')
#   line = re.sub(' ', ';', line)
    if line !='MM/DD/YYYY HH:MM:SS POD1_T POD1_H GrowArea_T GrowArea_H'+ '\n':
        print (line, file = outfile1, end = '')
for line in f2:
    line = line.decode('utf-8')
#    line = re.sub(' ', ';', line)
    if line != 'MM/DD/YYYY HH:MM:SS POD2_T POD2_H POD3_T POD3_H' + '\n':
        print (line, file = outfile2, end = '')
for line in f3:
    line = line.decode('utf-8')
#    line = re.sub(' ', ';', line)
    if line != 'MM/DD/YYYY HH:MM:SS POD4_T POD4_H POD5_T POD5_H' + '\n':
        print (line, file = outfile3, end = '')

#close opened files for prevention of "empty file copy" error 20120822, good habit to close opened files.
outfile1.close()
outfile2.close()
outfile3.close()

#move file to new location
#Don't need to make the script specific to directory:C:\\Users\\Iwong\\Applications\\Python32\\

src1 = "R:\\Research and Development\\Greenhouse\\TempAlert\\P1-tempdata.txt"
src2 = "R:\\Research and Development\\Greenhouse\\TempAlert\\P23-tempdata.txt"
src3 = "R:\\Research and Development\\Greenhouse\\TempAlert\\P45-tempdata.txt"
dest1 = "R:\\Research and Development\\Greenhouse\\TempAlert\\Txt Files\\POD1\\{}".format(filevar1)
dest2 = "R:\\Research and Development\\Greenhouse\\TempAlert\\Txt Files\\POD2&3\\{}".format(filevar2)
dest3 = "R:\\Research and Development\\Greenhouse\\TempAlert\\Txt Files\\POD4&5\\{}".format(filevar3)

shutil.copy(src1, dest1)
shutil.copy(src2, dest2)
shutil.copy(src3, dest3)

print('Done.')
