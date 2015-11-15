def get_string() : 
    string = raw_input()
    return string

def compute(number1, number2, operation) :
    if operation == '+' :
        result = number1 + number2
    elif operation == '-' :
        result = number1 - number2
    elif operation == '*' :
        result = number1 * number2
    elif operation == '/' :
        result = number1 / number2
    return result

def is_operand(character) :
    if character  in ['+','-','*','/'] :
        return True
    else :
        return False

def string_to_list(str) :
    str_list = list(str)
    return str_list

def push(character,stack,stack_size) :
    stack_size = stack_size + 1
    stack[stack_size] = character
    return stack,stack_size

def pop(stack, stack_size) :
    stack_size = stack_size - 1
    return stack,stack_size,stack[stack_size + 1]
    

def main() :
    string = get_string()
    str_list = string_to_list(string)
    stack = [0 for i in range(len(string))]
    stack_count = 0
    for character in str_list :
        if is_operand(character) :
            stack,stack_count,number1 = pop(stack,stack_count)
            stack,stack_count,number2 = pop(stack,stack_count)
            result = compute(number1, number2, character)
            stack,stack_count = push(result,stack,stack_count)
        else :
            character = int(character)
            stack,stack_count = push(character,stack,stack_count)
            # print "pushed {}".format(character)
    stack,stack_count,result = pop(stack,stack_count)
    print result


if __name__ == '__main__' :
    main()
    

