def reverscore(num):
    strNum = str(num)
    reversedStr = strNum[::-1]
    return int(reversedStr)

a,b,c,d,e = input().split()
a = (reverscore(a))
b = (reverscore(b))
c = (reverscore(c))
d = (reverscore(d))
e = (reverscore(e))

scores=[]
scores = list.append(a)
scores = list.append(b)
scores = list.append(c)
scores = list.append(d)
scores = list.append(e)
print(scores)