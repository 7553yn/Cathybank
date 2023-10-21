s = 'Hello welcome to Cathay 60th year anniversary'
s = s.replace(' ','')
s = s.upper()
s = list(s)
s.sort()

for qstr in s:
    qct = s.count(qstr) 
    print(qstr,qct)
