class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
        numSet = set()
        i = 1
        while len(numSet) != n:
            if k - i not in numSet:
                numSet.add(i)
            i += 1
        # print("numSet: ", numSet)
        return sum(numSet)



        # wrong
    
        # ans=0
        # if n > (k//2):
        #     for i in range(1, (k//2)+1):
        #         ans+=i
        #         print(i)
        #     for i in range(n-(k//2)):
        #         ans+=i+k
        #         print(i+k)
        # else:
        #     for i in range(1,n+1):
        #         ans+=i
        #         print(i)
        # return ans

def main(n, k):
    result = Solution()
    print(result.minimumSum(n, k))

if __name__== "__main__" :
    n = 5
    k = 4
    main(n, k)
