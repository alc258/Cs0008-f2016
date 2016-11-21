# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :10/28/26
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment number 2
#
# Notes:
#had to use a few variable/functions that were not learned in the chapter because i had to google
#some things to figure out how to make the program work

# ...and now let's program with Python


# MN: place comments at the beginning 
def processFile(fh):                             # creates process file function which reads file and loops
                                                 # through all lines of file handled
    lines = fh.readlines()                       # read all lines and store them in variable files

    line_count = 0                               # count how many lines there are in the file

    total_distance = 0                           # count total distance

    for l in lines:                             # loop through each line in the file
        l = l.rstrip('\n')                      # remove new line character

        data = l.split(',')                     # split name and distance

        if len(data) == 2:                      # only process lines where a name and
                                                # distance are found

            distance = float(data[1])           # set distance variable from value in file

            if (distance, float):               # make sure distance is a float
                total_distance += distance

            line_count += 1                      # increment line count
    fh.close                                     #close file

    return (line_count, total_distance)          # return the two values, line count and total distance

# MN: place comments at the beginning 
def printKV(key, value, klen = 0):              # printKV: prints and formats key values
    if value == None:                           # print simple strings without value
        print(key)

    if (value, str):                                                     # check for different data types
        print('{:<{}}: {:>20}'.format(key, len(key) + klen, value))      #and format to be the correct length
    elif (value, float):                                                 #and decimal placement
        print('{:<{}}: {:>10.3f}'.format(key, len(key) + klen, value))   #(len is used for the length)
    elif (value, int):
        print('{:<{}}: {:>10}'.format(key, len(key) + klen, value))

# MN: place comments at the beginning 
def summary(totalLineCount, total_distance):    #function for printing
    printKV('Totals', None)
    printKV('Total # of lines', totalLineCount)
    printKV('Total distance run', total_distance)


# MN: place comments at the beginning 
def main():                                                      # Creates the main function
    x=1
    while x != 0:
        file = input("Enter the name of the file: ")
        if file== "quit":
            x=0
        if file=="q":
            x=0
        if file==" ":
            x=0
        else:
            fh=open(file, 'r')
            # MN: this following statement assumes that you have defined a function named "file"  
            #total_distance,line_count=file(fh)
            # MN: if call processFile this way, you are not passing in the file handle/object in
            #     and you do not collect the output from it
            #processFile()
            # MN: here how you should have called processFile
            total_distance, line_count = processFile(fh)
            # MN: if you call printKV without arguments, it cannot print anything
            #printKV()
            # MN: here how you should have been calling printKV
            printKX('File number of lines',line_count)
            printKV('File distance run',total_distance)
            # MN: if you call summary here you will run it after processing every file
            #summary()


main()      # call the main function




