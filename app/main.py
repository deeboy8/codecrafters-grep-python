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
            if char_class == 'd' and is_digit(char):
                return True
            elif char_class == 'w' and is_alnum(char):
                return True
        return False

    def is_negative_character_class(input_line, pattern):
        # x = any(char in pattern for char in input_line)
        # print(f'x is: {x}')
        return not is_character_class(input_line, pattern)

    def is_character_class(input_line, pattern):
        return any(char in pattern for char in input_line) 

    #code block focuses on digit and alnum character classes   
    if pattern[0] == '\\':
        next_char = pattern[1]
        if next_char == 'd' or next_char == 'w':
            if match_character_class(input_line, next_char):
                return True
    #code block will focus on character group identification
    elif pattern[0] == '[':
        closing_bracket = pattern.find(']')
        if closing_bracket == -1:
            raise RuntimeError(f"Unmatched '[' in pattern: {pattern}")
        char_set = pattern[1:-1]
        if char_set[0] == '^':
            # if not is_negative_character_class(input_line, char_set[1:]):
            if is_character_class(input_line, char_set[1:]):
                return False 
        else:
            if is_character_class(input_line, char_set[1:]):
                return True
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")
    
    return True
      
def main():
    # pattern = sys.argv[
    pattern = '[^abc]'
    # input_line = sys.stdin.read()
    input_line = "123" #input("Enter input_line: ")

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
        print('failure')
        exit(1)

if __name__ == "__main__":
    main()


