### Editing a 2D List

We can edit values in a 2D list in the same way as variables and 1D lists. You just need to change the value to the new row and column index numbers.

👉 In this example, Sian has joined the dark side, so we're updating her computing preference to Linux.
```python
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

my2DList[1][2] = "Linux"
# The line above changes list 1, item 2 from PC to Linux

print(my2DList[1])
# I'm using this line to output list 1 to check that the change has happened correctly.
```
### Play around with assigning new data to the list.

