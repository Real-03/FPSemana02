sentence = input()
sentence = sentence.lower()
contador=0
thisdict = {}

while(contador<len(sentence)):
    if(sentence[contador].isalpha() ):
        thisdict[sentence[contador]] = sentence.count(sentence[contador])
    contador+=1

print(thisdict)