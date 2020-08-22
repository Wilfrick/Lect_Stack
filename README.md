# Lect_Stack
A lecture "stacking" utility, written in python 3 by some lads that needed a tool like this.

The idea is to have a command line utility that you run on a directory, and it smushes together all of the lec{x}.tex files into one large well ordered file and then compiles it.

We would like one python file that you run as follows "python3 run.py Optimisation" and it should do the following:
- Find all of the .tex files in the directory Optimisation/
- Find all of those files that are clearly lectures (presumably the ones that are called lecX.tex or whatever)
- Sort them sensibly (presumably lecture number)
- Aggregate them into one larger file called Optimisation.tex
