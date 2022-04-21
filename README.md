# tag_stripper
Remove unwanted LaTeX commands and their associated closing brackets

## Example
Consider the .tex file given in `example.tex`:

<img width="814" alt="revised_unstripped" src="https://user-images.githubusercontent.com/67121429/164489012-dd3a6afb-5c2f-4d98-9cc2-a5197a1e6ac5.png">
<img width="454" alt="output_unstripped" src="https://user-images.githubusercontent.com/67121429/164488183-85aa5288-a44a-4657-af0c-17aa3518feb6.png">

Here, a custom command `\revised{}` is being used to draw the reader's attention to changes that have been made in the document. Once changes are accepted, these commands and their associated closing brackets can be removed using `tag_stripper.py`. 

From the command line,

`python tag_stripper.py example.tex example_output.tex revised`

writes a new file `example_output.tex` which shows the same document with the `\revised{}` commands and their associated closing brackets removed.

<img width="804" alt="revised_stripped" src="https://user-images.githubusercontent.com/67121429/164488235-af2d21d1-58ea-43ce-9141-fe8696ed92f2.png">
<img width="440" alt="output_stripped" src="https://user-images.githubusercontent.com/67121429/164488246-c59df21e-7b31-49c0-b4cd-ef5c7e305c27.png">


## To Install
In the terminal, clone the github repository using the command:

`git clone git@github.com:CaseyMiddleton/tag_stripper.git`

You should now have a copy of the `tag_stripper` repository on your machine, containing example files and source code. 

## To Run

This script requires the filename to be modified and the `\command{}` to be removed. These arguments can be passed from the terminal or input directly in the python script.

### From terminal

The syntax to run this script from the command line is as follows:
``` 
$ python tag_stripper.py <path to input file> <path to output file> <command to remove>
```
If no output filename is provided, output will be stored in `inputfile_no_command`.

### From python 

To manually input arguments, replace lines 84--86 in `tag_stripper.py` with the desired input and output filenames and command to be removed.

### Questions
This script handles basic commands in the form of `\command{}` in LaTeX! If you have any questions, problems, or suggestions for improvement, please email <Casey.Middleton@colorado.edu>.
