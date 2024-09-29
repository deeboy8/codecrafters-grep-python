import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    def is_digit(char):
        return char.isdigit()
    
    def is_alnum(char):
        return char.isalnum()

    def match_character_class(input_line, char_class):
        for char in input_line:
            if char_class == '\\d' and is_digit():
                return True
            elif char_class == '\\w' and is_alnum():
                return True
        return False

    def is_negative_character_class(input_line, pattern):
        return any(char in pattern[1:-1] for char in input_line)

    def is_character_class(input_line, pattern):
        return any(char in pattern[1:-1] for char in input_line) 

    i = 0
    pattern_matched = True #boolean flag to check if the pattern is matched
    while i < len(input_line):
        #code block wil solely focus on alphnumeric characters
        #such as  a-z, A-Z, 0-9, etc., " apples"
        if is_alnum(pattern[i]):
            continue
        #code block focuses on digit and alnum character classes   
        elif pattern[i] == '\\':
            next_char = pattern[i + 1]
            if next_char == 'd' or next_char == 'w':
                if match_character_class(input_line, next_char):
                    i += 1
                    continue
        #code block will focus on character group identification
        elif pattern[i] == '[':
            closing_bracket = pattern.find(']', i)
            if closing_bracket == -1:
                raise RuntimeError(f"Unmatched '[' in pattern: {pattern}")
            
            char_set = pattern[i + 1:closing_bracket]
            if char_set[0] == '^':
                if not is_negative_character_class(input_line, char_set):
                    pattern_matched = False
            else:
                if not is_character_class(input_line, char_set):
                    pattern_matched = False
        else:
            raise RuntimeError(f"Unhandled pattern: {pattern}")
        i += 1

    return pattern_matched  
      
def main():
    pattern = sys.argv[2]
    # input_line = sys.stdin.read()
    input_line = input("Enter input_line: ")

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")
    print(f"input line is: {input_line}")
    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main()
