import math
def AllPossibleStrings(s):
		s = list(s)
		ans = []
		pow_set_size = int(math.pow(2,len(s)))
		for counter in range(1,pow_set_size):
		    a = []
		    for j in range(len(s)):
		        if ((counter&(1<<j))>0):
		            a.append(s[j])
		    ans.append("".join(a))
		ans.sort()
		return(ans)

if __name__=="__main__":
    print(AllPossibleStrings(input()))