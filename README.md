### What is Fuzuli
Fuzuli is a puzzle with very simple rules. See **fuzuli.pdf** for more details.
### What it is
Simple TKinter app with grid and button. After pressing a button, program generates swi-prolog script, which contains all data from grid and addiction predicates.
### How to run
To start program, just type i.e.:
```
python3 main.py 4 2 
```
which gives you 6x6 grid, as in example.

After pressing the button _Generate_, program creates file **prolog_output.pl**, which you need to run with command:
```
swipl prolog_script.pl
```
This should gives you all possible solution of this puzzle, based on what you type into grid before.
Remember, to get true fuzuli puzzle, solution should be exactly one :)
#### Requirements
- python3
- TKinter module
- swipl
