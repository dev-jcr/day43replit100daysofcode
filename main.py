import random, pprint
from prettytable import PrettyTable
bingo=[["","",""],["","",""],["","",""]]

counter=0
# def gen():
c=0
n=0
while True:
  if n<3:
    turn=random.randint(1, 100)
    bingo[c][n]=turn
    n+=1
    if n==3:
      c=+1
      if c==3:
        print(bingo)
        break
    else:
      continue
    