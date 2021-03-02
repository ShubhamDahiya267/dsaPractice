def setBits(N):
	counter =0
	while(N):
		N&=(N-1)
		counter+=1
	return counter
if __name__=="__main__":
    print(setBits(6))