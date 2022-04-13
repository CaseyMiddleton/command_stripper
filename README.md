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

`tag_stripper('example.tex','example_output.tex','\revised{}')`

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
In the terminal, clone the github repository using the command:

`git clone git@github.com:CaseyMiddleton/tag_stripper.git`

You should now have the `tag_stripper` repo on your machine, containing example files and source code. 

## To Run
The syntax to run this script from the command line is as follows:
``` 
$ python
>>> input_file = '< path to input file >'
>>> output_file = '< path to output file and desired filename >'
>>> command = '\ < command to remove with opening and closing brackets >'
>>> import tag_stripper; tag_stripper.remove_cmd(input_file,output_file,command)
```
Note that for LaTeX commands beginning with '\', such as `\revised{}`, an extra \ is required when the command is specified. 
