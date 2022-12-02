with open("C:/Users/Philippe/Documents/GitHub/advent-of-code/01 january/exercise1/input.txt",'r') as data:
    input=data.read().splitlines()

max=0
current=0
for i in input:
    if i !="":
        current+=int(i)
    else:
        if current>max:
            max=current
        current=0
print(max)