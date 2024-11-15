sentence = input()
sentence2 = input()
x = sentence.split()
x2 = sentence2.split()
words=[]
a = set()
for i in x:
    a.add(i)
for j in x2:

    if(j in x):
        words.append(j)


for k in range(len(words)):
    print(words[k], end =" ")


