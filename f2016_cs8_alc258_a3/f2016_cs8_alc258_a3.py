# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :09/19/16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
#
# Notes:
# any notes to the instructor and/or TA goes here

# ...and now let's program with Python
#create output file
#out_file=open("output.txt,'w")
#make dictionary a global variable
global_dict={}
#Ask user to enter file name
master_filename=str(input("Enter the name of your file: "))
#open file to read
master_file=open(master_filename, 'r')
#create function to format files and read lines
def fh(file, dictionary):
        #open file
    file=open(file,'r')
        #set accumulator
    count=0
    file.readline()
        #create for loop to count total lines and format lines
    for line in file:
            count+=1
            line=line.strip('\n').split(',')
                #set key as names
            key=str(line[0])
            #set value as distances
            value=float(line[1])
            #if statement for searching dictionary
            if(key in dictionary):
                    dictionary[key]=dictionary[key]+[(value)]
            else:
                    dictionary[key]=[value]
        #close file
    file.close()
        #return values
    return [dictionary,count]
#create variable for the name of person with max distance
max_name=' '
#create a variable for the max distance
max_dist=0
#create loop to find max distance
for key in global_dict:
        #search for max distance
    l_values=global_dict[key]
    if(max(l_values)>max_dist):
        #reassaign max distance
        max_dist=max(l_values)
        #assaign the name of the person to max_name
        max_name=key
#create variable for name of person with min distance
min_name=' '
#create variable for min distance
min_dist=0
#create loop to find min distance
for key in global_dict:
    #search for min distance
    r_values=global_dict[key]
    if(min(r_values)<min_dist):
        #assaing the smallest r_vaulue found to min_distance
        min_dist=min(r_values)
        #assaign key next to smallest distance to min_name
        min_name=key
#set accumulator for total number of files in master to 0
total_files=0
#create loop to srtip newline and calculate total number of files in master
for line in master_file:
        line=line.rstrip('\n')
        total_files +=1
#put all read lines of maser file into file-list variable
file_list=master_file.readlines()
#close file
master_file.close()

#Print all the outputs/values
print ('')
print('Number of input files read : ', total_files)
print('Total number of lines read : ',)
print('')
print('Total distance run :', )
print('')
print('Max distance run :',max_dist)
print('  by participant :',max_name)
print('')
print('Min distance run :', min_dist)
print('  by participant :',min_name)
print('')
print('Total number of participants :',)
print('Number of participants:',)
print('with multiple records :',)










