#store the datas in a list giving the different lines
with open("C:/Users/Philippe/Documents/GitHub/advent-of-code/01 january/exercise1/input.txt",'r') as data:
    input=data.read().splitlines()

# max is the list of the callories carried by the top three elves. It's always sorted.
max=0
# current is the callories carried by the current elve.
current=0
for i in input:
    if i !="":
        current+=int(i)
    else:
        if current>max:
            max=current
        current=0
print(max)