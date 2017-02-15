# -*- coding: cp1252 -*-
print (" Analyzer by B M Abir 12201022")

inFile= open('input.txt','r')
word_list=[]
identity_list=[]
identity_val=[]
operator_list=['-','+','x','/'] ##Higher order has higher index value
output_list=[]
stack=[]
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
def findIdentity():
    limit=int(word_list[0])
    count=0
    while(count<limit): ##loops through the word list to find the identity
        line=word_list[count+1] ##line contains the current line with count+1, as the 
        c=0
        line_len=len(line)
        temp_identity=''
        while((c<line_len)):
            if(line[c]!='='):
                temp_identity+=line[c]
                ##print(temp_identity)
            else:
                break
            c+=1
        ##print(count)
        ##print(temp_identity)
        identity_list.append(temp_identity)
        print(identity_list[count])
        c+=1
        identity_val.append(int(line[c:]))
        print(identity_val[count])
        count+=1

    parseLimit=int(word_list[limit+1])
    print("Parse Limit",parseLimit)
    parseCount=0
    while(parseCount<=parseLimit):
        line=word_list[limit+1+parseCount]
        print("This is the parse ",line)
        line_len=len(line)
        c=0

        ##1)  Examine the next element in the input.
        ##2)  If it is operand, output it.
        ##3)  If it is opening parenthesis, push it on stack.
        ##4)  If it is an operator, then
        ##  i) If stack is empty, push operator on stack.
        ##  ii) If the top of stack is opening parenthesis, push operator on stack
        ##  iii) If it has higher priority than the top of stack, push operator on stack.
        ##  iv) Else pop the operator from the stack and output it, repeat step 4
        ##
        ##5)  If it is a closing parenthesis, pop operators from stack and output them until an opening parenthesis is encountered. pop and discard the opening parenthesis.
        ##6)  If there is more input go to step 1
        ##7)  If there is no more input, pop the remaining operators to output.

        while((c<line_len)):
            try:            ##if identity found
                ind=identity_list.index(line[c])
                print(line[c]," index:",ind)
                output_list.append(identity_val[ind]) ##Add the value of the identity as the operend to output
            except ValueError:  ##if no identity is found
                try:            ## else if operator is found
                    loopFlag=True
                    while(loopFlag):
                        ind=operator_list.index(line[c])
                        print(line[c]," index:",ind)
                        if(stack==[]):              ##if stack is empty
                            stack.append(line[c])   ##push operator to stack
                            loopFlag=True
                        elif(stack[-1]=='('):       ##if stack top has a '('
                            stack.append(line[c])   ##push operator to stack
                            loopFlag=True
                        elif(ind>operator_list.index(stack[-1])):
                            stack.append(line[c])   ##push operator to stack
                            loopFlag=True
                        else:
                            output_list.append(stack.pop())
                            loopFlag=False                      
                except ValueError:
                    if(line[c]=='('):           ##push '(' to stack
                        stack.append(line[c])
                    elif(line[c]==')'):
                        temp=stack.pop()        ##pop from stack as a ')' is found
                        output_list.append(temp)
                        while((temp!='(') and (stack!=[])):       ##pop from stack untill a '(' is found
                            temp=stack.pop()
                            output_list.append(temp)
            c+=1
        while(stack!=[]):
            output_list.append(stack.pop())
        parseCount+=1
removeSpace()
findIdentity()
print("output",output_list)
