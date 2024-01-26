class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        def sum_digit(n):
            ans = 0
            # print("n: ", n)
            
            for i in range(len(str(n))):
                # print("i: ", i)
                ans += int((str(n))[i])
            return ans

        di = {}
        for i in range(1, n + 1):
            if sum_digit(i) not in di:
                di[sum_digit(i)] = [i]
            else:
                di[sum_digit(i)].append(i)
        # print("di: ", di)

        ls = list(di.values())
        # print("ls: ", ls)
        mx = 0
        for i in range(len(ls)):
            if len(ls[i]) > mx:
                mx = len(ls[i])
        
        ans = 0
        for i in range(len(ls)):
            if len(ls[i]) == mx:
                ans += 1
        return ans

def main(n):
    result = Solution()
    print(result.countLargestGroup(n))

if __name__== "__main__" :
    n = 13
    main(n)
