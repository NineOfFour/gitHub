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
