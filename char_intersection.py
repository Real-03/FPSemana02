sentence = input()
sentence2 = input()
x = sentence.split()
x2 = sentence2.split()
a = set()
b = set()
for i in x:
    a.add(i)
for j in x2:
    b.add(j)
text=""
for k in a.intersection(b):
    text+=k+" "
print(text.strip())

