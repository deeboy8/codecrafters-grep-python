import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    # if len(pattern) == 1:
    #     return pattern in input_line
    # else:
    #     raise RuntimeError(f"Unhandled pattern: {pattern}")
    #create switch statments
    match pattern:
        case '\d':
            for x in int(input_line):
                if x >= 0 and x <= 9:
                    return True
    return False
        


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    print(f"input line is: {input_line}")   
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
