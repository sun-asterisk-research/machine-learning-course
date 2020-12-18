import string
# ex1
f1 = open("week1_ex1.txt")
new_line_f1 = ""
for x in f1:
    new_line_f1 += x[0]
print(new_line_f1)
f1.close
# ex2
summary = 0
number = str(2**10000)
for x in number:
    summary += int(x)
print(summary)
# ex3
f2 = open("week1_ex2.txt")
new_line_f2 = ""
for x in f2:
    # buffer = list(x)
    for i in x:
        if i in string.punctuation or i in ['1','2','3','4','5','6','7','8','9','0']:
            x=x.replace(i,'')
    new_line_f2 += x
print(new_line_f2)
f2.close
ex4
 a + 13 × b : c + d + 12 × e – f – 11 + g × h : i – 10 = 66
for a in range(1,9):
    for b in range(1,9):
        for c in range(1,9):
            for d in range(1,9):
                for e in range(1,9):
                    for f in range(1,9):
                        for g in range(1,9):
                            for h in range(1,9):
                                for i in range(1,9):
                                    if(a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10) == 66:
                                        print(a,b,c,d,e,f,g,h,i)
# ex5
word = 'python'
result = 0
for character in word:
    number = ord(character) - 96
    result += number
print('Sum of all letters in the word: ', result)
# ex6
x = 1
y = 1
print(x)	
while(x < 10000):
	temp = y
	y = x
	x = x + temp
	print(y)

# ex7
check = 1
for i in range(3,10000):
	# a int(i/2)
	for j in range(2,int(i/2)+1):
		if i%j == 0:
			check = 0
	if check == 1:
		print(i)
	check = 1
 # ex8
count = {}
f3 = open("week1_ex8.txt")
for x in f3:
	for word in x.lower().split():
	    if word not in count:
	        count[word] = 1
	    else:
	        count[word] += 1
print(count)
# ex9
A = [1, 2, 3, 4, 5, 6]
B = [3, 4, 5, 6, 7, 8, 9, 10]
check = 0
intercept = []
A_only = []
B_only = []
union = []
for i in A:
    for j in B:
        if(i == j):
            intercept.append(i)
            check = 1
            union.append(i)
            break
    if check == 0:
        union.append(i)
    check = 0

for i in B:
    for j in A:
        if(i == j):
            check = 1
            break
    if check == 0:
        union.append(i)
    check = 0
print(union)
print(intercept)
# ex10

    

