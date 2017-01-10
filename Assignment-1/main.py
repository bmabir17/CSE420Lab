print ("Lexical Analyzer by B M Abir 12201022")
inFile= open('input.txt','r')
word_list=[]





def removeSpace(inFile):
    tempWord=' '
    i=0
    for line in inFile:
        
        ##print ('line1')
        for char in line:
            ##print (char)
            
            if(char==' ' or char=='\n' or char==',' or char==';'):
                ##print(tempWord)
                tempWord=tempWord.strip()
                tempWord=tempWord.strip('\n')
                word_list.insert(len(word_list),tempWord)
                ##print(word_list)
                tempWord=' '

                
            tempWord+=char



removeSpace(inFile)
print(word_list)
