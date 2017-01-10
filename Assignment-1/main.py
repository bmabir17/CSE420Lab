print "Lexical Analyzer by B M Abir 12201022"
inFile= open('input.txt','r')
word_list=[]





def removeSpace(inFile):
    
    for line in inFile:
        
        print 'line1'
        for char in line:
            print char
            word_list=word_list+char



removeSpace(inFile)
