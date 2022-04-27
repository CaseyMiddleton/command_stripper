#### LaTeX tag stripper
# Remove LaTeX commands and the associated closing bracket
# Developed by Casey E. Middleton
# See https://github.com/CaseyMiddleton/command_stripper for instructions for use

import sys

def remove_cmd(input_filename,output_filename,cmd):
    # detect bracket type using cmd
    open_bracket = "{"
    close_bracket = "}"
    cmd_orig = "\\"+cmd
    cmd = "\\" + cmd + open_bracket

    # Read in text file
    file = open(input_filename)
    output = open(output_filename, 'w')

    # create a stack that stores the last opened as a keeper (k) or a tosser (t)
    bracket_tracker = []
    counter = 0; # count number of command removals that took place

    # Scan text file for word cmd
    line = file.readline()
    while line:
        words = line.split() # split the lines by spaces
        for word in words:
            # iterate through characters in word
            ii = 0
            while ii < len(word):
                # check for \cmd{ or other commands
                if contains(word[ii],open_bracket):
                    # opening brackets associated with \cmd{
                    if contains(word[ii-len(cmd)+1:ii+1],cmd):
                        bracket_tracker.append("t") # t = remove closing bracket in future
                    # other commands whose closing brackets should be preserved
                    else:
                        bracket_tracker.append("k") # k = keep closing bracket in future
                        output.write(word[ii])
                # handle closing brackets
                elif contains(word[ii],close_bracket):
                    # determine if the last opening bracket was a keeper or tosser by popping from stack
                    last_opener = bracket_tracker.pop()
                    if last_opener == "t":
                        # do not add to file, but increment counter
                        counter += 1
                    else:
                        output.write(word[ii])
                # otherwise, just write to file
                else:
                    # unless it is the start of the \cmd{
                    if contains(word[ii:(ii+len(cmd))],cmd):
                        bracket_tracker.append("t")
                        ii += len(cmd) - 1 # move to the end of \cmd{ and keep scanning word
                    else:
                        output.write(word[ii])
                ii += 1
            output.write(' ')

        output.write('\n') # newline at end of each line
        line = file.readline()

    # close files
    output.close()
    file.close()
    print("Removed ", counter," instances of ",cmd_orig,". Results stored in ",output_filename)

def contains(wrd,ii):
    ''' Returns True if ii is present in wrd '''
    wrd_len = len(wrd)
    ii_len = len(ii)
    for i in range(0,wrd_len-ii_len+1):
        if wrd[i:i+ii_len] == ii:
            return True
    return False

'''
-------------------------------------------------------------------------------
-----------------------    Change Me    ---------------------------------------
-------------------------------------------------------------------------------
replace file path to input and output files and \command{} to remove to run script
'''
def manual_input():
    input_filename = "example.tex"
    output_filename = "example_output.tex"
    command = "revised"
    return (input_filename, output_filename, command)
'''
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
'''

def main():
    # User should input three arguments
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        # if no user input, assume manual input using manual_input() function
        if len(sys.argv) == 1:
            input_filename, output_filename, command = manual_input()
        # if user attempted bash run but had an improper number of arguments, send error message
        else:
            print("Argument Error \n To run file, please input: \n python tag_stripper.py <input_filename> <output_filename> <command>")
            sys.exit(1)
    # if only two arguments are provided, create output filename
    else:
        input_filename = str(sys.argv[1])
        if len(sys.argv) == 3:
            command = str(sys.argv[2])
            output_filename = input_filename[0:(len(input_filename)-4)] + "_no_" + command + input_filename[(len(input_filename)-4):len(input_filename)]
        else:
            output_filename = str(sys.argv[2])
            command = str(sys.argv[3])

    remove_cmd(input_filename,output_filename,command)

if __name__ == '__main__':
    main()
