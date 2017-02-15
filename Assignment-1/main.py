print ("Lexical Analyzer by B M Abir 12201022")
import re
inFile= open('input.txt','r')
inKeyword= open('keyword.txt','r')
inOp= open('operators.txt','r')
word_list=[]
keyword_list=[]
other_list=[]
identity_list=[]
Moperator_list=[]
Loperator_list=[]
numVal_list=[]







def removeSpace():
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
                ##print('word_list',word_list)
                tempWord=' '

                
            tempWord+=char
    print('word_list',word_list)

def findKeyword():
    
    for line in inKeyword:
        line=line.strip('\n')
        ##print(line)
        for token in word_list:
            if(token==line):
                keyword_list.append(token)
                ##print (token)
                


def findDataType():
    breakF=0
    i=0
    for token in keyword_list:   ##Iterate Keyword list to find indentifiers
        
        while word_list:            ##iterate word list with the chosen keyword
            if(word_list[i]==token):    ##if word token matches keyworkd
                i=(i+1)% len(word_list)     ##increment the pointer of the word list as we have found the keyword in the word_list, now have to assume the next word is a identifiers
                print token
                print "word:",word_list[i]
                while word_list:                
                    if(word_list[i]==','):
                        other_list.append(word_list[i])
                        i=(i+1)% len(word_list)
                        print("in if",word_list[i])
                    elif(word_list[i]==';'or word_list[i]=='(' or word_list[i]==')'):
                        other_list.append(word_list[i])
                        i=(i+1)% len(word_list)
                        print("in if",word_list[i])
                        break
                    else :
                        identity_list.append(word_list[i])
                        i=(i+1)% len(word_list)
                        print("in else",word_list[i])
                        #print(i)
            ##i=(i+1)% len(word_list)
            
            print("After if",word_list[i],i)
            break
def findOp():
    for line in inOp:
        line=line.strip('\n')
        ##print(line)
        for token in word_list:
            if(token==line):
                Moperator_list.append(token)
                ##print (token)
    
def findNum():
    for token in word_list:
        
        if token.isdigit():
            numVal_list.append(token)
                

removeSpace()
findKeyword()
findDataType()
findOp()
findNum()
print("KeyWords",keyword_list)
print("identifiers",identity_list)
print("Math Operator",Moperator_list)
print("Numbers",numVal_list)
print("Others",other_list)
##print(identity_list)
##print(other_list)
##
##print(word_list)
