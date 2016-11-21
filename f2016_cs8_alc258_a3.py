# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :11/18/16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment number 3
#
# Notes:
#outfile=open(output.txt,'w')
#make dictionary a global dictionary
global_dict={}
#ask user to enter filename
master_filename=str(input("Enter the name of your file: "))
#open file to read
master_file=open(master_filename,'r')
#create function to create dictionary and format files
def fh(file,dictionary):
    #open file
    file=open(file, 'r')
    #set accumulator
    count=0
    file=0
    file.readline()
    #create loop to count lines in files and strip new line
    for line in file:
        count+=1
        line=line.strip('\n').split(',')
        #assaign key value to names
        key=str(line[0])
        #assaign value to distances
        value=float(line[1])
        #set parameters for searching dictionary
        if (key in dictionary):
            dictionary[key]=dictionary[key]+[value]
        else:
            dictionary[key]=[value]
    #close file
    file.close()
    #return values
    return[dictionary,count]
#create variables for max distance and their name
max_name=' '
max_dist=' '
#create loop to iterate through dictionary to find highest value
for key in global_dict:
    l_values=global_dict[key]
    if(max(l_values)>max_dist):
        #assaign max value to max_dist
        max_dist=max(l_values)
        #assaign key with max dist found to max_name
        max_name=key
#create variables for min distance and their name
min_name=' '
min_dist=0
#create loop to iterate through dictionary to find lowest value
for key in global_dict:
    r_values=global_dict[key]
    if(min(r_values)<min_dist):
        #assagin the lowest value found to min_dist
        min_dist=min(r_values)
        #assagin the key value associated with lowest distance to min_name
        min_name=key
#set accumulator for total files
total_files=0
#create loop to get rid of newline and count how many files are in master
for line in master_file:
    line=line.rstrip('\n')
    total_files+=1
file_list=master_file.readlines()
#close master file
master_file.close()
#print all outputs in format
print(' ')
print('Number of input files read: ',total_files)
print('Total number of lines read: ',)
print(' ')
print('Total distance run: ',)
print(' ')
print('Max distance run: ',)
print('  by participant:',)
print('')
print('Max distance run: ',)
print('  by participant:',)
print('')
print('Total number of participants:',)
print('Number of participants: ',)
print(' with multiple records:',)



