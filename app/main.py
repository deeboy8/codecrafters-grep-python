import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

def check_for_achoring_match(pattern, new_input_line):
    return pattern == new_input_line
        
def end_of_string_anchor(pattern, input_line):
    return pattern == input_line

def match_pattern(input_line: str, pattern: str) -> bool:
    if pattern.startswith('^'):
        pattern = pattern[1:]
        len_of_pattern = len(pattern)
        new_input_line = input_line[:len_of_pattern + 1]
        x = check_for_achoring_match(pattern, new_input_line)
        if x == False:
            return False
        else:
            return True
    
    if pattern.endswith('$'):
        pattern, input_line = pattern[::-1], input_line[::-1] # reversed each string
        pattern = pattern[1:] # removed $ from pattern string
        pattern_len = len(pattern) 
        input_line = input_line[:pattern_len]
        value = end_of_string_anchor(pattern, input_line)
        if value:
            return True
        else:
            return False

    i, j = 0, 0
    while i < len(pattern) and j < len(input_line):
        # loop over alphanumeric characters in input line if no match with pattern
        if pattern[i] == input_line[j]: ## what if you had /d in input_line
            i += 1; j += 1
            continue
        if pattern[i] == '\\':
            i += 1
            if i < len(pattern):
                if pattern[i] == 'd':
                    if not input_line[j].isdigit():
                        j += 1; i -= 1
                        continue
                elif pattern[i] == 'w': ##
                    if not input_line[j].isalnum():
                        j += 1
                        continue
                i += 1
                j += 1
            else:
                return False
        #TODO: good place for error handling -> if \\ but doesn't match d/w then its a problem
        # if find negative or positive character groups in pattern
        elif pattern[i] == '[':
            closing_bracket = pattern.find(']', i)
            if closing_bracket == -1:
                # raise RuntimeError(f"Unmatched '[' in pattern: {pattern}")
                return False 
            char_set = pattern[i + 1:-1]
            if char_set.startswith('^'):
                if input_line[j] in char_set[1:]:
                    return False
            else:
                if input_line[j] not in char_set:
                    j += 1
                    continue
            i = closing_bracket + 1
            j += 1                
        else:
            j += 1
        
    return i == len(pattern)
      
def main():
    # pattern = sys.argv[2]
    pattern = 'log$'
    # input_line = sys.stdin.read()
    input_line = "slog" #input("Enter input_line: ")

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