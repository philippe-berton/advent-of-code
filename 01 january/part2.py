
with open("C:/Users/Philippe/Documents/GitHub/advent-of-code/01 january/input.txt",'r') as data:
    input=data.read().splitlines()
max=[0,0,0]
current=0
for i in input:
    if i !="":
        current+=int(i)
    else:
        if current>max[0]:
            max[0]=current
        current=0
        max.sort()
print(sum(max))