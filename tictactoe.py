a = [0, 1, 2, 3, 4,5,6,7,8,9]

print("",a[1],"|",a[2],"|",a[3],"\n-----------\n",a[4],"|",a[5],"|",a[6],"\n-----------\n",a[7],"|",a[8],"|",a[9],"\n")

moveX=input("choose from 1 to 9 : ")

while(int(moveX) >9 or int(moveX)<1):
    moveX=input("choose from 1 to 9 : ")

moveY=input("X choose from 1 to 9 : ")

a[int(moveX)]="X"
print("",a[1],"|",a[2],"|",a[3],"\n-----------\n",a[4],"|",a[5],"|",a[6],"\n-----------\n",a[7],"|",a[8],"|",a[9],"\n")

while(int(moveY) >9 or int(moveY)<1 or moveY == moveX):
    moveY=input("O choose from 1 to 9 : ")

a[int(moveY)]="O"
print("",a[1],"|",a[2],"|",a[3],"\n-----------\n",a[4],"|",a[5],"|",a[6],"\n-----------\n",a[7],"|",a[8],"|",a[9],"\n")