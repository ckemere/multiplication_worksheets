# mathgenerator
A program to generate math problems in a pretty format

forked from [https://github.com/djotaku/mathgenerator](https://github.com/djotaku/mathgenerator)

This script generates 50 pages of random multiplication problems, 28 per page. The numbers are
chosen randomly from 2 to 12 inclusive.

# Running

`python3 mathgenerator.py`

When it's done:

`pdflatex worksheet.tex`

Alternatively, load it into Overleaf and compile there!

# Modifications

You probably would want to change the name a the top of the page template
from `Lydia` to your child's name!

See the parent repository for more comments, but note that the code can be
easily modified to generate addition, subtraction, or division problems. 
(Though the number choice for division presumably needs some careful
curation.)