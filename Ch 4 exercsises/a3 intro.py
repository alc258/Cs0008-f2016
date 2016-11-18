filename="words"
fh=open(words, 'r')
words=fh.readlines()
fh.close()
words2=[]                                           #initialize variable
for line in words:                                  #create for loop
        words2.append(line.strip('\n').lower())     #append file to remove newline and make all words lowercase
words3=[line.strip('\n').lower() for line in words]
len(words)
words_no_duplicates=list(set(words3))
words_no_duplicates.sort()
words_length=[length(item) for items in words_no_duplicates]
def count_words_of_length(1):
    nwords=0
    for item in words_length:
        if item==5:
         nwords+=1
    return nwords
lc={}
for item in words_length:
    if item not in lc.keys():
        lc[item]=1
    else:
        lc[item]+=1
lc
for item in words_no_duplicates:       #check if key exsits in dictionsry
    if item not in lc.keys():
        lc[item]=[]                     #if not initalize it
    else:
        lc[item]+=1