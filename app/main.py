import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!



def match_pattern(input_line: str, pattern: str) -> bool:

    def check_for_achoring_match(pattern: str, new_input_line: str) -> bool:
        return pattern == new_input_line
    
    # searching for '+' quantifier

    # match beginning of input_line string with exact length of matching chars in pattern
    if pattern.startswith('^'):
        pattern = pattern[1:]
        len_of_pattern = len(pattern)
        new_input_line = input_line[:len_of_pattern + 1]
        value = check_for_achoring_match(pattern, new_input_line)
        if value == False: #TODO: ternary expression?
            return False
        else:
            return True
    
    # reverse both strings to compare input_line string with exact length of matching chars in pattern
    if pattern.endswith('$'):
        pattern, input_line = pattern[::-1], input_line[::-1] # reversed each string
        pattern = pattern[1:] # removed $ from pattern string
        pattern_len = len(pattern) 
        input_line = input_line[:pattern_len]
        value = check_for_achoring_match(pattern, input_line)
        if value:
            return True
        else:
            return False

    def zero_or_one_match(pattern, input_line, i, j):
        # check and make sure pattern nand input_line are valid
        if len(pattern) == 0 or len(input_line) == 0:
            #TODO: excepction/ error handling
            return False
        if pattern[i] == pattern[j] and pattern[j]:
            j+= 1; i+= 2
            return True
        elif pattern[i + 1] == pattern[j] or pattern[i + 2] == pattern[j]:
             return True
        else:
            return False
 
                                               #i
                                #pattern = "colou?r"
                         #input_line = "The color of the sky is blue."
                #                               j
                #                            i
                #         #pattern = "behavio?ur"
                #  #input_line = "Her behaviour was exemplary during the meeting."
                #                            j
    #                             i            
    #             pattern = "flavo?r"
    #      input_line = "The flavour of the ice cream was intense."
    #                             j

    i, j = 0, 0
    while i < len(pattern) and j < len(input_line):
        if pattern[i] == input_line[j]: ## what if you had /d in input_line
            i += 1; j += 1            
            continue
        # match for '+' quantifier (one or more character match)
        if pattern[i] == '+':
            if i == 0 or j == 0:
                return False
            prev_char = pattern[i - 1]
            while j < len(input_line) and input_line[j] == prev_char:
                j += 1
            i += 1
        # match for '?' quantifier (zero or one characters)
        elif pattern[i + 1] == '?' or (pattern[i] == '?' and pattern[i] != input_line[j]):
            # zero_or_one_match(pattern, input_line, i)
            if pattern[i] == '?':
                if pattern[i + 1] == input_line[j]:
                    i += 2; j += 1
                    continue
            if pattern[i + 1] == '?': #where i + 1 is ? 
                if pattern[i + 2] == input_line[j]:
                    i += 3; j += 1
                    continue
        elif pattern[i] == '\\':
            i += 1 # move idx to letter d or w character
            if i < len(pattern):
                if pattern[i] == 'd':
                    # if input_line char not a digit will move to next char in input_line and move decrement i back to //
                    if not input_line[j].isdigit(): 
                        # continue moving across input_line in search of digit to match with '\d' escape character 
                        j += 1; i -= 1
                        continue
                elif pattern[i] == 'w': 
                    if not input_line[j].isalnum():
                        j += 1; i -= 1 #TODO monitor if i -= 1 affects testing by codecrafters; added bc unsure why removed when it's present in '\d' block
                        continue
                i += 1; j += 1
            else:
                return False
        #TODO: good place for error handling -> if \\ but doesn't match d/w then its a problem
        # if find negative or positive character groups in pattern
        elif pattern[i] == '[':
            closing_bracket = pattern.find(']', i)
            if closing_bracket == -1:
                return False 
            char_set = pattern[i + 1:-1] # removing opening bracket
            if char_set.startswith('^'):
                if input_line[j] in char_set[1:]: # slicing to remove '^'
                    return False
            else:
                if input_line[j] not in char_set:
                    j += 1
                    continue
            i = closing_bracket + 1 #TODO: this will present a problem later
            j += 1                
        else:
            j += 1
        
    return i == len(pattern)
      
def main():
    pattern = sys.argv[2]
    # pattern = '[^abc]'
    input_line = sys.stdin.read()
    # input_line = "def" #input("Enter input_line: ")

    # if sys.argv[1] != "-E":
    #     print("Expected first argument to be '-E'")
    #     exit(1)

    # # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")
    # print(f"input line is: {input_line}")
    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        print('success')
        exit(0)
    else:
        print('fail')
        exit(1)

if __name__ == "__main__":
    main()