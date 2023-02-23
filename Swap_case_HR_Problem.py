def swap_case(s):
    SwAp = ''   #HEREE we given a empty string to add the modified values
    for char in s:
        if char.upper() != char:
            SwAp += char.upper()
        elif char.lower() != char:
            SwAp += char.lower()
        else:
            SwAp += char

    return SwAp


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)