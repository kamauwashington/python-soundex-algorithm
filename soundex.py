from typing import List


def soundex(input : str) -> str :
    # fail fast if input is None (code defensively)
    if input is None : 
        return None

    # ensure that there are at least 2 characters (code defensively)
    if len(input) < 2 :
        return None

    # resulting code translation meeting the regex of /^[A-Z]\d{3}$/
    finalCode : List[str] = []

    # codings is a representation of the alphabet according to the SOUNDEX algorithm
    # 0 represents vowels : 'A','E','I','O','U', where 9 represents 'H','W','Y'. 
    # Both 0 and 9 are skipped charcters.
    codings : str = "01230129022455012623019292"

    # list containing the coded representation of each input character
    inputCoded : List[str] = []
    
    # use an uppercase representation of the input for easier validation and iterate over each character
    for char in list(input.upper()) :

        # get the ascii character code for the current character
        charCode : int = ord(char)

        # VALIDATON : if the char is not [A-Z] skip it
        if charCode < 65 and charCode > 90 : 
            continue
        
        # SOUNDEX : Step 1a. Retain the first letter of the input
        if len(finalCode) < 1 : 
            finalCode.append(char)
            
        # SOUNDEX : Step 2. Replace consonants with digits (after the first letter):
        code : int = codings[charCode - 65]
        inputCoded.append(code)
    
    # variable that retains the last consonant coding (this will never be 0 or 9)
    previousChar : chr = None

    # iterate over the coded input, the index is needed to compare like characters with a 0 or 9 between them
    for index, char in enumerate(inputCoded) :

        # prevent further iteration once the finalCode has reached the max length according to the SOUNDEX algorithm
        if len(finalCode) == 4 :
            break

        # determine if the current character is a skippable (or to be removed) character as per the algorithm
        skipchar : bool = char in ['0','9']

        # SOUNDEX : Step 3b. Remove all the zero (0 or 9) digits (performed by skipping)
        if skipchar : 
            continue

        # store the previous character if available
        if index > 0 :
            previousChar = inputCoded[index-1]
            
        # the first character should be skipped for processing    
        else :
            continue

        # SOUNDEX : Step 3a. Replace all adjacent same digits with one digit (performed by skipping)
        if char == previousChar :
            continue

        # SOUNDEX : Step 3.
        #
        # If two or more letters with the same number are adjacent in the original word (before step 1), 
        # only retain the first letter; also two letters with the same number separated by 'h' , 'w' or 'y' 
        # are coded as a single number, whereas such letters separated by a vowel are coded twice. 
        # This rule also applies to the first letter.
        if index > 2 and inputCoded[index-2] == char :
            if previousChar == '0' :
                finalCode.append(char)
                continue

            # characters equaling 9 are skipped if the previous and next value are the same
            elif previousChar == '9' :
                continue
    

        finalCode.append(char)
            
    # SOUNDEX : Step 4. f there are too few letters in the word to assign three numbers, append zeros until there are 
    # three numbers. If there are four or more numbers, retain only the first three.
    return '{:<04s}'.format(''.join(finalCode))

