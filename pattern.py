def generate(chars, rows, sep, half):
    #first test: generate('?', 3, 'newline', 'both') whats returned is tested against "?\n??\n???\n??\n?"
    #function should return ?\n??\n???\n??\n?               # both
    #chars = ?                                              # ?
    #rows is not rows but max number in a single row = 3    # ??
    #sep = \n                                               # ???
    #half = both : can also be first or second              # ??
        #in this case both : ?\n??\n???\n??\n?              # ?
        #             first: ?\n??\n???
        #             second: ???\n??\n?
    # Using to find the value for the variable inSep
    if sep == 'newline':
        # '\n' this gave me insertion errors changed this to '\\n' still got them
        # changed it back to '\n' this morning, ran it again no insertion errors????
        #
        inSep = '\n'
    elif sep == 'twice-space':
        inSep = '  '
    elif sep == 'space':
        inSep = ' '
    elif sep == 'twice-newline':
        inSep = '\n\n'
    else:
        inSep = ' '
        # use string variable to build the return value
    string = ''
    # half variable passed is the pattern first, second, both
    if half == 'both':
        # tryed to do this in a for loop
        # then remembered KISS: keep it simple stupid
        #
        # not needed :top = rows -1
        i = 1
        # this is the first half of both
        # in this case it will go to 3
        while i <= rows:
            j = 0
            # this loop will generate the number of chars needed for each row
            while j < i:
                # add the char to the string
                string += chars
                j += 1
            # seperater inSep : \n or \n\n
            # add the seperator
            string += inSep
            # increase the variable
            i += 1
        # second half of both 3 -1 start at two
        k = rows - 1
        # use a another string variable
        stringB = ''
        # outer loop num of rows
        while k > 0:
            l = 0
            # loop for each line
            while l < k:
                stringB += chars
                l += 1
            # no seperator at the end
            if k != 1:
                stringB += inSep
            k -= 1
        string += stringB
    elif half == 'first':
        # this is the first half of both
        i = 1
        while i <= rows:
            j = 0
            while j < i:
                string += chars
                j += 1
            # exept for this, no sep at the end
            if i != rows:
                string += inSep
            i += 1
    elif half == 'second':
        # second half of both
        k = rows
        while k > 0:
            l = 0
            while l < k:
                string += chars
                l += 1
            if k != 1:
                string += inSep
            k -= 1
    return string

# print(generate('?', 3, 'newline', 'both'))
# what you get from the print statement
# ?
# ??
# ???
# ??
# ?
# this is correct, the problem is that it need to be equal to ?\n??\n???\n??\n?
# for assertEqual function not to give an assertion error
# yesterday I got assertion errors today I get

# Ran 4 test in 0.003s

# OK
# Process finished with exit code 0

