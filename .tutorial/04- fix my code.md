# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*


```python
my2DList =  ["Johnny", 21, "Mac"],
             ["Sian" 19, "PC"]
             ["Gethin", 17, "PC"], ]

print(my2DList[0][1])


```

<details> <summary> 👀 Answer </summary>
Lots of lovely syntax errors here.  Read the code comments for each one.

```python
my2DList =  [ ["Johnny", 21, "Mac"], # No opening square bracket
             ["Sian", 19, "PC"], # Missing , between Sian and 19. Also missing , after the square bracket for this sub-list.
             ["Gethin", 17, "PC"] ] #Extra , after this sub list - the last sub-list doesn't have a comma after it.

print(my2DList[0][1])
```
</details>