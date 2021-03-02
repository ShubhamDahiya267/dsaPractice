def isPowerofTwo(n):
    return (n and (not(n&(n-1))))

if __name__=="__main__":
    print(isPowerofTwo(int(input())))