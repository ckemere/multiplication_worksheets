import random

latex_header = """%%----------LaTeX template for teachers-----------------------------%%
%%----------Samuel S. Watson----------------------------------------%% 
%%----------January 2013--------------------------------------------%% 

\\documentclass[12pt]{article} % Specifies font size

%----------------PACKAGES-------------------------------------------%%
\\usepackage[left=0.75in, right=0.75in, top=0.5in, bottom=0.5in]{geometry} % Sets all four margins 
\\usepackage[pdftex]{graphicx} % Allows inclusion of image files
\\usepackage{amssymb} % Access to extra math symbols
\\usepackage{amsmath} % Access to extra math symbols
\\usepackage{wrapfig} % Allows wrapping of text around figures
\\usepackage{calc} % Gives access to a basic calculator 
%-------------------------------------------------------------------%%

%----------------COMMANDS-------------------------------------------%%
\\newcommand\\blank{\\underline{\\hspace{2cm}}} % Gives a blank 
\\newcounter{prob} % A new counter for current problem number
\\setcounter{prob}{1} % Start the counter at the value 1
\\newcommand\\itm{
\\fbox{\\textbf{\\theprob}} \\refstepcounter{prob}
} % Calls problem number
\\newcommand{\\problem}[1]{\\makebox[0.5cm]{\\itm}   
  \\begin{minipage}[t]{\\textwidth-0.5cm} #1 \\end{minipage} 
} % An environment for a problem statement on or more lines
\\newcommand{\\pairofprobs}[2]{
  \\begin{minipage}[t]{0.5\\textwidth}\\itm #1 \\end{minipage} 
  \\begin{minipage}[t]{0.5\\textwidth}\itm #2 \\end{minipage} 
} % Fits two problems on a line
\\newcommand{\\threeprobs}[3]{
\\begin{minipage}[t]{0.31\\textwidth}\\itm #1 \\end{minipage} \\hfill
 \\begin{minipage}[t]{0.31\\textwidth}\\itm #2 \\end{minipage} \\hfill 
 \\begin{minipage}[t]{0.31\\textwidth}\\itm #3 \\end{minipage}
} % Fits three problems on a line
\\newcommand{\\fourprobs}[4]{
\\begin{minipage}[t]{0.18\\textwidth}\\itm #1 \\end{minipage} \\hfill
 \\begin{minipage}[t]{0.18\\textwidth}\\itm #2 \\end{minipage} \\hfill 
 \\begin{minipage}[t]{0.18\\textwidth}\\itm #3 \\end{minipage} \\hfill
 \\begin{minipage}[t]{0.18\\textwidth}\\itm #4 \\end{minipage}
} % Fits three problems on a line
\\newcounter{choice} % Counter for multiple choice problems 
\\setcounter{choice}{1} % Start the counter at the value 1
\\newcommand\\achoice{
(\\alph{choice}) \\stepcounter{choice}
} % Generates letter for multiple choice option
\\newcommand{\\answers}[5]{\\vspace*{-7mm} 
  \\begin{tabular}{l@{\hspace{1mm}}}p{0.9\\textwidth}
    \\achoice & #1 \\\\ \\achoice & #2 \\\\ \\achoice & #3 \\\\ 
    \\achoice & #4 \\\\ \\achoice & #5 \\end{tabular}
  \\setcounter{choice}{1}
} % Makes multiple-choice options 
%---------------------------------

% The commands below are for setting up arithmetic 
% problems with the four basic operations. See examples 
% in the CONTENT section  

\\newcommand\\divi[2]{
$#1 \\: \\begin{array}{|l}
\\hline #2
\\end{array}$
}

\\newcommand\\mult[2]{
$\\begin{array}{rr} 
 & #1 \\\\ 
 \\times & #2 \\\\ \\hline 
 \\end{array}$}
 
\\newcommand\\addi[2]{
  $\\begin{array}{rr} 
   &  #1 \\\\ 
    + & #2 \\\\ \\hline 
  \\end{array}$}

\\newcommand\\subt[2]{
  $\\begin{array}{rr}
    & #1 \\\\ 
    - & #2 \\\\ \\hline
  \\end{array}$}
%-------------------------------------------------------------------%%

%-----------FORMATTING----------------------------------------------%%
\\pagestyle{empty} % Ensures that no page numbers are printed
\\parskip = 0.2 in % Puts a little space between paragraphs 
\\parindent = 0.0 in % Enforces no indentation for paragraphs
%-------------------------------------------------------------------%%

%-----------USAGE EXAMPLES------------------------------------------%%
% To try any of the examples below, uncomment them and paste 
% them below the \\begin{document} command in the CONTENT section. 

% To set up a division problem such as 93 divided by 3:
% \\divi{3}{93}

% To set up a muliplication problem such as 14 times 4:
% \\mult{14}{4}

% To put two problems on the same line: 
% \\pairofprobs{\\divi{3}{93}{\\mult{14}{4} 

% To include a 3cm vertical space between questions 
% \\vspace{3cm} 

%--------------------------------------------------------------------%%

%-----------CONTENT--------------------------------------------------%%
\\begin{document}

"""

latex_page_template = """
\\setcounter{{prob}}{{1}} % Start the counter at the value 1

\\begin{{center}} 
  \\textsc{{Lydias's Math Problems \#{seed}}} \\\\ 
  %Teacher's name
\\end{{center}}

%\\fontsize{{14}}{{18pt}} \\selectfont % Increase Font Size
\\vspace{{-2cm}}

{problems}
"""

latex_footer="""
\\end{document}
%-------------------------------------------------------------------%%

"""

def form_subtraction():
    a = random.choice(range(10,20))
    b = random.choice(range(3,a+1))
    return f'\\subt{{{a}}}{{{b}}}'

def form_addition():
    (a,b) = random.choices(range(5, 10), k=2)
    return f'\\addi{{{a}}}{{{b}}}'

def form_multiplication():
    (a,b) = random.choices(range(2,12), k=2)
    return f'\\mult{{{a}}}{{{b}}}'

def form_division():
    pass

def get_row_of_random_problems():
   
   #(a,b,c,d,e,f) = random.choices(range(1, 20), k=6) #this is beautiful if your student can handle subtraction with 
   #a smaller number on top. Mine can't yet, so Iv'e got to use a less elegant solution.
   
  #  return f'\\threeprobs{{{form_multiplication()}}}{{{form_multiplication()}}}{{{form_multiplication()}}}'
   return f'\\fourprobs{{{form_multiplication()}}}{{{form_multiplication()}}}{{{form_multiplication()}}}{{{form_multiplication()}}}'

def get_rows_of_random_problems(n):
    rows = ""
    for x in range(n):
        rows = rows +  '\n\n\\vspace{2cm}\n\n' + get_row_of_random_problems()
    return rows



with open(f'worksheet.tex', 'w') as f:
    f.write(latex_header)
    for seed in range(50):
        random.seed(seed)
        problems = get_rows_of_random_problems(7) 

        page = latex_page_template.format(seed=seed, problems=problems)
        f.write(page)
        f.write('\pagebreak\n')
    f.write(latex_footer)
