# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=5NpIRejBPiQ)

<details> <summary> 👀 Answer </summary>

```python

import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()

```

</details>

- Join our [100 Days Community](https://replit.com/100-days-help)
- Want [live support?](https://replit.com/replit-101)