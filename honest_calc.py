msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_ = {
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)"
}
oper_list = ['+', '-', '*', '/']


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


def calculator(memory = 0):
    while True:
        calc = input(msg_0)
        x, oper, y = calc.split()
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_1)
        else:
            if oper not in oper_list:
                print(msg_2)
            else:
                check(x, y, oper)
                if oper == '+':
                    result = x + y
                    break
                elif oper == '-':
                    result = x - y
                    break
                elif oper == '*':
                    result = x * y
                    break
                elif oper == '/' and y != 0:
                    result = x / y
                    break
                else:
                    print(msg_3)

    print(result)
    answer = ''
    while answer != 'y' and answer != 'n':
        answer = input(msg_4)
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    answer = input(msg_[msg_index])
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            memory = result
                            break
                    elif answer == 'n':
                        break
            else:
                memory = result
    answer = ''
    while answer != 'y' and answer != 'n':
        answer = input(msg_5)
        if answer == 'y':
            calculator(memory)


calculator()
