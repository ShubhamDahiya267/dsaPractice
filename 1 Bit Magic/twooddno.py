def twoOddNum(Arr, N):
        xor2 = Arr[0]
        ans = [0,0]
        set_bit_no = 1
        k = 0
        for i in range(1,N):
            xor2 ^= Arr[i]
        #to get rightmost bit        
        set_bit_no = xor2 & (~(xor2-1))
        for i in range(N):
            if (Arr[i]&set_bit_no):
                ans[1]^=Arr[i]
            else:
                ans[0]^=Arr[i]
        return sorted(ans,reverse = True)

if __name__=="__main__":
    N = int(input())
    Arr = input().split()
    for i in range(N):
        Arr[i]=int(Arr[i])
    print(twoOddNum(Arr,N))
