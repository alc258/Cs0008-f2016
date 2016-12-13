# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       : 12/7/16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description: Final Project


# Notes:

# ...and now let's program with Python
#create class for participant
class participant:
    #Create initializer method; n=name d=distance
    def __init__(self,n,d=0):
        #set name
        self.name=n
        #set distance
        self.distance=d
        #if statement for if distance is 0, then runs is 0
        if (d==0):
            self.runs=0
        #if distance is not 0, runs = 1
        else:
            self.runs=1
    #create method for adding a distance
    def addDistance(self,d):
        #if statement for if the distance is greater than 0 then add number to distance, and increase runs by 1
        if d>0:
            self.distance+=d
            self.runs+=1
    #create method for getting the distance and return value
    def getDistance(self):
        return self.distance
    #create string method; format the name, distance run, and runs, make a string, then return it
    def __str__(self):
        return "Name: " + format(self.name, '>20s'  ) + ". Distance Run: " + format(self.distacne, '9.4f') + \
        ". Runs: " + format(self.runs, '4d')
    #Create method to get name and return it
    def getName(self):
        return self.name
    #create method to get # of runs and return it
    def getRuns(self):
        return self.runs
    #Create method to add more than one distance at a time
    def addDistances(self,ld):
        #loop through the list of floats
        for d in ld:
            #if distance is greater than 0, add it to the distance accumulator and increase runs by 1
            if d>0:
                self.distance+=d
                self.runs+=1
    #create method to joining together name,runs , and distances and convert them to string to make
    #it easier to write to output file later and return the result
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])


#create function to get information from file
def getData(file):
    # initialize output list
    output = []
    # create loop to read file by line
    for line in open(file,'r'):
        # create if statement to skip over header
        if "distance" in line:
            # skip line
            continue
        # remove newline and split commas
        temp1 = line.rstrip('\n').split(',')
        # use try/except to avoid  errors
        try:
            # append records to output list
            # strip spaces and convert distance to a float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            # skip lines that are not in correct format
            print('Invalid row : '+line.rstrip('\n'))
    # return data
    return output

# Have user enter master file name
master_file = input("Enter name of master file : ")

# read master file and get data files and strip files of newline
try:
    data_files = [file.rstrip('\n') for file in open(master_file,'r')]
#if user inputs name wrong or it doesnt exist print error
except:
    print("Error: Can't read master file or invalid name")
    exit(1)
# read data files
#combine lists of records in data files and getData list by using loops and appending it to raw_data
raw_data = [];
for file in data_files:
    for item2 in getData(file):
        raw_data.append(item2)

#create variable for number of files read
number_of_files=len(data_files)
#create variable for total lines read
total_lines=len(raw_data)
#
total_distance_run=sum([item['distance'] for item in raw_data])
# the previous statement can be complicated and hard to understand
# it is equivalent to do the following:
# uniqueListData = [];
#  for item1 in rawData:
#     for item2 in item1:
#          uniqueListData.append(item2)
#      # end for item2
#  # end for item1
#
# number of files read

# compute distance run for each participant and how many records we have for each one of them
# initialize all the accmulators
# dictionary with one element for each participant whose value is
# the list of all the distances found in data for the participant
participants = {}

# loops on all the records
for item in raw_data:
    # check if the names has already been found previously or if it is new
    # if it is new, initialize elements in the accumulators
    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
    # insert distance in the list for this participant
    participants[item['name']].addDistance(item['distance'])
# end for

# minmum distance run with name
minDistance = { 'name' : None, 'distance': None }
# maximum distance run with name
maxDistance = { 'name' : None, 'distance': None }
# appearances dictionary
appearances = {}
#
# computes the total distance run for each participant iterating on all the participants
for name, object in participants.items():
    # compute distance for current name / participant
    distance=object.getDistance()
    # check if we need to update min
    # if this is the first iteration or if the current participant distance is lower than the current min
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance
    # end if
    # check if we need to update max
    # if this is the first iteration or if the current participant distance is lower than the current min
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance
    # end if
    #
    # appearences is equivalent to the length of the distances
    participant_appearances = object.getRuns()
    #
    # check if we need to initialize this entry
    if not participant_appearances in appearances.keys():
        appearances[participant_appearances] = []
    appearances[participant_appearances].append(name)
# end for

#
# compute total number of participant
# this is equivalent to the length of the participantDistances
total_participants = len(participants);

#
#  compute total number of participants with more than one record
duplicate_participant_record = len([1 for item in participants.values() if item.getRuns() >1])

#
# set format strings
INTEGER = '5d'
FLOAT = '12.5f'
STRING = '20s'
#
# provide requested output
print("")
print(" Number of Input files read   : " + format(number_of_files,INTEGER))
print(" Total number of lines read   : " + format(total_lines,INTEGER))
print("")
print(" Total distance run           : " + format(total_distance_run,FLOAT))
print("")
print(" Max distance run             : " + format(maxDistance['distance'],FLOAT))
print("   by participant             : " + format(maxDistance['name'],STRING))
print("")
print(" Min distance run             : " + format(minDistance['distance'],FLOAT))
print("   by participant             : " + format(minDistance['name'],STRING))
print("")
print(" Total number of participants : " + format(total_participants,INTEGER))
print(" Number of participants")
print("  with multiple records       : " + format(duplicate_participant_record,FLOAT))
print("")


#
# create output file
outputFile = "f2016_cs8_alc258_fp.data.output.csv"
# open file for writing
fh = open(outputFile,'w')
# write header in file
fh.write('name,records,distance\n')
# loop on all the participants
for name, object in participants.items():
    # write line in file using csv method/object and print newline
    fh.write(object.tocsv() + '\n')
# close files
fh.close()


