def swap_case(s):
    string_input = list(str(s))
    n = len(string_input)
    x = ""
    for i in range(n):
        if string_input[i] >= 'a' and string_input[i] <= 'z':
            x = x + string_input[i].upper()
            
        else:
            x = x + string_input[i].lower()
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)