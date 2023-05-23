# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## 'Index out of range'?

👉 What is an 'out of range' error?


```python
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

print(my2DList[0][3])

```

<details> <summary> 👀 Answer </summary>

- The second square bracket references item 3 in list 0. There is no item 3 as the list index only goes up to 2. Remember, everything starts at index 0.

```python
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

print(my2DList[0][2])

```

</details>


