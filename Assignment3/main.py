inFile= open('input.txt', 'r')
import re
rule=[]
reg=[]
word_list=[]
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
                print('word_list',word_list)
                tempWord=' '

                
            tempWord+=char
    print('word_list',word_list)

def checkRE():
    rule_count=0
    rule_limit=int(word_list[rule_count])
    print("rule limit",rule_limit)
    while(rule_count<rule_limit):
        print("rule count",rule_count)
        line=word_list[(rule_count+1)]
        print(line)
        rule.insert(rule_count,line)
        rule_count+=1
        print("rule",rule)
    string_count=0
    string_limit=int(word_list[rule_limit+1])
    ##print(string_limit);
    while(string_count<string_limit):
        tempString=word_list[rule_limit+string_count+1]
        reg.insert(string_count,tempString)
        ruleCount=0
        while(ruleCount<rule_limit):
            tempRule=rule[ruleCount]
            print(tempRule)
        string_count+=1
    print("rule",rule)
    print("String",reg)
    
    regex="a{1}b*c*d{1}"
    if re.search(regex, "accccd"):
        match=re.match(regex,"accccd")
        print ("Match at index %s, %s" % (match.start(),match.end()))
    
removeSpace()
checkRE()

