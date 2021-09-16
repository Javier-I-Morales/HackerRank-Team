def swap_case(s):
    return ''.join([l.upper() if l.islower() else l.lower() for l in s])
    #return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)