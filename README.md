# Blocks World

This repository contains 2 Python source code files with a simple implementation of a solution to the [Blocks world problem](https://www.kaggle.com/camnugent/california-housing-prices).<br/>

The approach followed in this solution is combining the A* search algorithm with a simple heuristic functions that counts the number of blocks that are placed in the wrong position.

This software supports up to 26 blocks (as many as the number of letters in the English alphabet).


In order to execute the code, you will also need the following 2 Python source files from the [AIMA Python source code repository](https://github.com/aimacode/aima-python):
* search.py
* utils.py


To execute the code, place all the 4 required source files in the same directory, cd in that directory and type:
```bash
python ./Main.py -n <number-of-blocks>
```

The code is written in Python 3.
