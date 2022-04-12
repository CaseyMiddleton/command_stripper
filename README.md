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

Here, a custom command `\revised{}` is being used to draw the reader's attention to changes that have been made in the document. Once changes are accepted, these commands and their associated closing brackets can be removed using `tag_stripper`. 

Running the terminal 

`tag_stripper('example.tex','output.tex','\revised{}')`

writes a new file `output.tex` which shows the same document with the `\revised{}` commands and their associated closing brackets removed.

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


## To Run
The syntax to run this script is as follows:

`tag_stripper(<input filename>, <output filename>, <command to remove>)`
