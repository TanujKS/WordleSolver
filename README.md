# Welcome to WordleSolver

WordleSolver is a quick and easy way to solve the popular New York Times puzzle: Wordle

# Quick Start

## Download WordleSolver  

### Using git

Run
```
git clone https://github.com/TanujKS/WordleSolver
```

## Using WordleSolver

WordleSolver has no requirements outside of the latest version of Python, to start the solver simply run:
```
python solve.py (any starting word)
```
or if that does not work:
```
python3 solve.py (any starting word)
```

You will then be prompted to enter what color you got for each letter, 'g' represents green, 'y' represents yellow, and 'n' represenets grey

**Example:**
```
$ python3 solve.py weary

Guess: skied
Letter s is: (y/g/n) n
```

# Credits:

https://github.com/fogleman/TWL06 for the `twl` module required to gather all the words in the English dictionary
