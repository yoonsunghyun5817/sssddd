#파일 읽기 
with open('sss.txt' , 'r') as f:
    data=f.read()

print(data)
#문장 자르기
a=data.split('\n')

for y in range(len(a)):
    for x in range(len(a[0])):
        if a[y][x]=='a':
            print(x,y)

