import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

'''
\d apple should match "1 apple", but not "1 orange".
\d\d\d apple should match "100 apples", but not "1 apple".
\d \w\w\ws should match "3 dogs" and "4 cats" but not "1 dog" (because the "s" is not present at the end).
'''


def match_pattern(input_line, pattern):
    i, j = 0, 0
    while i < len(pattern) and j < len(input_line):
        # loop over alphanumeric characters in input line if no match with pattern
        if pattern[i] == input_line[j]:
            i += 1; j += 1
        # if find digit character class tags
        elif pattern[i] == '\\' and input_line[j].isdigit():
            i += 1 # move indice to d or w char
            if i < len(pattern):
                if pattern[i] == 'd' and input_line[j].isdigit() \
                or pattern[i] == 'w' and input_line[j].isalnum():
                    i += 1; j += 1
                else:
                    return False
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
                        return True
            i = closing_bracket + 1
            j += 1                
        else:
            j += 1
        
    return i == len(pattern)
      
def main():
    # pattern = sys.argv[
    pattern = '\\d apples'
    # input_line = sys.stdin.read()
    input_line = "sally has 1 oranges" #input("Enter input_line: ")

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