# Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division `//`, which throws away the remainder. `10/3` is `3.333333`, `10//3` is `3`.

## Concepts Covered

- conditionals, comparisons
- arithmetic

## Version 1

Have the user enter the total number in pennies, e.g. for $1.37, the user will enter 137.

The output would be something like:
```
quarters: 5
dimes: 1
nickels: 0
pennies: 2
```

## Version 2

Have the user enter a dollar amount as a float (1.37)
