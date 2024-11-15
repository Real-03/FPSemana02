sentence = input()
contador=0
thisdict = {}

while(contador<len(sentence)):
    if(not(sentence[contador].isspace())):
        
        thisdict[sentence[contador]] = sentence.count(sentence[contador])
    contador+=1

print(thisdict)