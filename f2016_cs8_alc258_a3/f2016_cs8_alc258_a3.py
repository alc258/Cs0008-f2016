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
# MN: why do you define the functions within your main body of code?
# MN: please respect indentation with comments too.
# MN: total number of praticipants and total number of participants with more than one run are missing
# MN: output file creation is missing
#

# ...and now let's program with Python
#create output file
#out_file=open("output.txt,'w")

# MN: move all this after the fuction definition
## make dictionary a global variable
#global_dict={}
## Ask user to enter file name
#master_filename=str(input("Enter the name of your file: "))
## open file to read
#master_file=open(master_filename, 'r')

# create function to format files and read lines
# MN: you define the function fh here, but you never call it and use it
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
        # MN: I guess that here your intention is to append the value at the end
        if(key in dictionary):
            dictionary[key]=dictionary[key]+[(value)]
        else:
            dictionary[key]=[value]
        #close file
    file.close()
    #return values
    return [dictionary,count]

# MN: question: if you place the following 2 blocks here,
#     your variable global_dict is still empty
#     they should be moved after you have read the master file and
#     the data ones
##create variable for the name of person with max distance
#max_name=' '
##create a variable for the max distance
#max_dist=0
##create loop to find max distance
#for key in global_dict:
#    #search for max distance
#    l_values=global_dict[key]
#    if(max(l_values)>max_dist):
#        #reassaign max distance
#        max_dist=max(l_values)
#        #assaign the name of the person to max_name
#        max_name=key
#
##create variable for name of person with min distance
#min_name=' '
##create variable for min distance
#min_dist=0
##create loop to find min distance
#for key in global_dict:
#    #search for min distance
#    r_values=global_dict[key]
#    if(min(r_values)<min_dist):
#        #assaing the smallest r_vaulue found to min_distance
#        min_dist=min(r_values)
#        #assaign key next to smallest distance to min_name
#        min_name=key

# MN: here is where the main flow of your program start
# Ask user to enter file name
master_filename=str(input("Enter the name of your file: "))
# open file to read
master_file=open(master_filename, 'r')

#set accumulator for total number of files in master to 0
total_files=0
# MN: you need to initialize file_list if you use it in the loop
file_list = []
#create loop to srtip newline and calculate total number of files in master
for line in master_file:
        # MN: why do you read the line from the file, remove the \n and you do not utilize the value       
        line=line.rstrip('\n')
        # MN: insert the line in the file list
        file_list.append(line)
        total_files +=1

# put all read lines of maser file into file-list variable
# MN: this line is not needed because you already read all the lines from master file
#     in the previous for loop
#     you already have reached the end of the file, so it will return nothing
#file_list=master_file.readlines()
#close file
master_file.close()

# MN: before going ahead you need to read the data files
#     that is why you defined the function fh
#
# make dictionary a global variable
global_dict={}
# MN: you need to define a counter for the number of lines
tot_num_lines = 0
# loop on data file names
for file in file_list:
    [global_dict,numlines] = fh(file,global_dict)
    tot_num_lines += numlines
print(global_dict)

# MN: here where the min and max needs to be executed
#create variable for the name of person with max distance
max_name=' '
#create a variable for the max distance
max_dist=0
#create loop to find max distance
for key in global_dict:
    #search for max distance
    l_values=global_dict[key]
    # MN: you should work with the total distance run by the participant, that is computed using sum on l_values
    if(max(l_values)>max_dist):
        #reassaign max distance
        max_dist=max(l_values)
        #assaign the name of the person to max_name
        max_name=key

#create variable for name of person with min distance
min_name=' '
#create variable for min distance
# MN: if you initialize to 0, you will never be able to find the shortest distance run
#     because all of them are greate than zero
#     Initialize to a really high number
##min_dist=0
min_dist=10000
#create loop to find min distance
for key in global_dict:
    #search for min distance
    r_values=global_dict[key]
    # MN: same as for the max, you want to work with the total distance run, aka sum of l_values
    if(min(r_values)<min_dist):
        #assaing the smallest r_vaulue found to min_distance
        min_dist=min(r_values)
        #assaign key next to smallest distance to min_name
        min_name=key


#Print all the outputs/values
print ('')
print('Number of input files read : ', total_files)
# MN: here you can use tot_num_lines
print('Total number of lines read : ', tot_num_lines)
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


