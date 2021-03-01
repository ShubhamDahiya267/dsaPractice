def checkKthBit(n,k):

    if (n & (1<<k)):
        print("SET")
    else:
        print("NOT SET")

if __name__=="__main__":
    n = int(input())
    k = int(input())
    checkKthBit(n,k)