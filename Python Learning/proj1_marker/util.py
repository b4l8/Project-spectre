#! /usr/bin/env python

## prototype : find text bloc

# bloc -> collect all lines, until find empty line
# no empty line returns ,no empty bloc returns, but last line must be empty line

def lines(file):
    for line in file : yield line
    yield '\n'
    
def blocks(file):
    """go through file , if line not empty, put line into block;
    if line empty , and block not empty, generate this block as string.
    """
    block=[]
    for line in lines(file):
        if line.strip():  #strip(char):  return str with all defined char remouved from begin and end ; default white spaces
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block=[]
       
