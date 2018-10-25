
def three_percentage(string):
    counter = 0
    value_holder = 0
    result = False
    for i in string:
        if i.isdigit():
            digit = int(i)
            if digit + value_holder == 10:
                if counter != 3:
                    return False
                result = True
            value_holder = digit
            counter = 0
        elif i == '%':
            counter = counter + 1
    if result:
        return True
    return False

print(three_percentage('arrb6%%%4xxb8l5%%%eee5'))
print(three_percentage('acc%7%%sss%3rr1%%%%%%5'))
print(three_percentage('5%%aaaaaaaaaaaaaaaaaaa%5%5'))
print(three_percentage('9%%%1%%%9%%%1%%%9'))
print(three_percentage('aa6%9'))
