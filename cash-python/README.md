# Cash (Python)

{% video https://www.youtube.com/watch?v=f3iMmGry05Q %}
In past years, the "Cash" problem was known as "Greedy".


{% next %}

## Greedy Algorithms

<!-- http://mypieceofthe31415927.blogspot.com/2014/04/whats-wrong-with-these-us-coins.html -->
![US coins](coins.jpg)

When making change, odds are you want to minimize the number of coins you're dispensing for each customer, lest you run out (or annoy the customer!).  Fortunately, computer science has given cashiers everywhere ways to minimize numbers of coins due: greedy algorithms.

According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one "that always takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some instances of other problems."

What's all that mean? Well, suppose that a cashier owes a customer some change and in that cashier's drawer are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢). The problem to be solved is to decide which coins and how many of each to hand to the customer. Think of a "greedy" cashier as one who wants to take the biggest bite out of this problem as possible with each coin they take out of the drawer. For instance, if some customer is owed 41¢, the biggest first (i.e., best immediate, or local) bite that can be taken is 25¢. (That bite is "best" inasmuch as it gets us closer to 0¢ faster than any other coin would.) Note that a bite of this size would whittle what was a 41¢ problem down to a 16¢ problem, since 41 - 25 = 16. That is, the remainder is a similar but smaller problem. Needless to say, another 25¢ bite would be too big (assuming the cashier prefers not to lose money), and so our greedy cashier would move on to a bite of size 10¢, leaving him or her with a 6¢ problem. At that point, greed calls for one 5¢ bite followed by one 1¢ bite, at which point the problem is solved. The customer receives one quarter, one dime, one nickel, and one penny: four coins in total.

It turns out that this greedy approach (i.e., algorithm) is not only locally optimal but also globally so for America's currency (and also the European Union's). That is, so long as a cashier has enough of each coin, this largest-to-smallest approach will yield the fewest coins possible. How few? Well, you tell us!

{% next %}

## Implementation Details

Implement, in `cash.py` at right, a program that first asks the user how much change is owed and then prints the minimum number of coins with which that change can be made.

* Use `get_float` to get the user's input. Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).
* We ask that you use `get_float` so that you can handle dollars and cents, albeit sans dollar sign. In other words, if some customer is owed $9.75 (as in the case where a newspaper costs 25¢ but the customer pays with a $10 bill), assume that your program's input will be `9.75` and not `$9.75` or `975`. However, if some customer is owed $9 exactly, assume that your program's input will be `9.00` or just `9` but, again, not `$9` or `900`. Of course, by nature of floating-point values, your program will likely work with inputs like `9.0` and `9.000` as well; you need not worry about checking whether the user's input is "formatted" like money should be.
* If the user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies.
* Your output does not need to contain the number of each denomination. It can simply be the total number of coins.
* Beware the inherent imprecision of floating-point values. A computer, with a finite number of bytes, cannot store an infinite number of decimal numbers. So you may want to convert your input into cents before proceeding.
* Take care to round your cents to the nearest penny, as with `round`.

  ```
  cents = round(dollars * 100);
  ```

  will safely convert `0.20` (or even `0.200000002980232238769531250`) to `20`.

Your program should behave per the examples below.

```
$ python cash.py
Change owed: 0.41
4
```

```
$ python cash.py
Change owed: -0.41
Change owed: foo
Change owed: 0.41
4
```

{% spoiler "Hints" %}
Here is some pseudocode which might help. Be free to write your own pseudocode as well, particulary after watching the walkthrough video on top of this lab.

1. Import the get_float function from the cs50 module
2. To validate your user input, use a while loop to keep prompting for input, and break out of it when the value is valid. See the walkthrough video above.
2. prompt the user for change and store the result in a new variable using get_float("Change owed: ")
3. Since this original amount will be in dollars, convert this to cents as indicated above, and round to the nearest whole number
4. Create a new variable for your number of coins, and initialize it to 0
4. There are two different ways to solve from here. One way is to use a series of while loops adding on to the number of coins as you go along. The other way is to use a combination of floor division, (as in `cents // 25`) to determine how may quarters, and modulo (the remainder operator, as in `cents % 25`) to determine how much is then left after you've taken out all the quarters.
5. Print out the total number of coins
6. Test your code and debug any errors


{% endspoiler %}


### How to Test Your Code

Does your code work as prescribed when you input

* `-1.00` (or other negative numbers)?
* `0.00`?
* `0.01` (or other positive numbers)?
* letters or words?
* no input at all, when you only hit Enter?

### Check50

When you feel your code is in good shape, it's time to run it through check50.

```
check50 cs50/problems/2019/ap/sentimental/cash
```

inputting your GitHub username and GitHub password as prompted.


{% next "Ready to submit?" %}

In the terminal, type in:

```
submit50 cs50/problems/2019/ap/sentimental/cash
```

