#store the datas in a list giving the different lines
with open("C:/Users/Philippe/Documents/GitHub/advent-of-code/02 december/input.txt",'r') as data:
    input=data.read().splitlines()

total_score=0
for i in input :
    current_score=0
    p1=i[0]
    p2=i[2]
    if p1=='A':
        if p2=='X':
            total_score+=3
        if p2=='Y':
            total_score+=4
        if p2=='Z':
            total_score+=8
    elif p1=='B':
        if p2=='X':
            total_score+=1
        elif p2=='Y':
            total_score+=5
        elif p2=='Z':
            total_score+=9
    elif p1=='C':
        if p2=='X':
            total_score+=2
        elif p2=='Y':
            total_score+=6
        elif p2=='Z':
            total_score+=7
print(total_score)