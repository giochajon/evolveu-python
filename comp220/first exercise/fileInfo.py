import sys
#get the name of the file 


def getlinenumbers(targetfile,pattern):
## get the number of lines
    f = open(targetfile,'r')

    linenumber = len(f.readlines( ))

    #print("Number of Lines:",linenumber)


    ## get contents into z and number of chars
    # move to the beginning
    f.seek(0,0)

    z = f.read()
    numchars = len(z)
    # how many of the pattern are in the file
    thnum = z.count(pattern)
    #print (f"I found {thnum} {pattern}'s in the file")

    # tell will tell you the position on the file
    #if f.tell() == numchars:
    #    print(f'we are at char {numchars} at the end of file')

    # move to the beginning
    f.seek(0,0)
    f.close()
    return [linenumber,numchars,thnum] 


if __name__ == "__main__":
    myfile = sys.argv[1]
    pattern = sys.argv[2]
    print("we are using ", myfile)
    r = getlinenumbers(myfile,pattern)
    print (f"there are {r[0]} lines and {r[1]} characters as well as {r[2]} occurrences of {pattern}'s in {myfile}")
