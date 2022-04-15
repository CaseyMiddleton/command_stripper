# tag_stripper
Remove unwanted LaTeX commands and their associated closing brackets

## Example
Consider the .tex file given in `example.tex`:

```
\documentclass[11pt]{article} 

\usepackage{amsmath}
\newcommand{\revised}[1]{\textcolor{magenta}{#1}} 

\begin{document}

I am using the color magenta to show \revised{changes I have made} since you last saw this document. 

\section*{Some changes occur \revised{within section headers} and some do not.}

\end{document}
```

Here, a custom command `\revised{}` is being used to draw the reader's attention to changes that have been made in the document. Once changes are accepted, these commands and their associated closing brackets can be removed using `tag_stripper.py`. 

From the command line,

`python tag_stripper.py example.tex example_output.tex revised)`

writes a new file `example_output.tex` which shows the same document with the `\revised{}` commands and their associated closing brackets removed.

```
\documentclass[11pt]{article} 

\usepackage{amsmath}
\newcommand{\revised}[1]{\textcolor{magenta}{#1}} 

\begin{document}

I am using the color magenta to show changes I have made since you last saw this document. 

\section*{Some changes occur within section headers and some do not.}

\end{document}
```


## To Install
In the terminal, clone the github repository using the command:

`git clone git@github.com:CaseyMiddleton/tag_stripper.git`

You should now have a copy of the `tag_stripper` repository on your machine, containing example files and source code. 

## To Run
The syntax to run this script from the command line is as follows:
``` 
$ python tag_stripper.py <path to input file> <path to output file> <command to remove>
```
If no output filename is provided, output will be stored in `inputfile_no_command'.
