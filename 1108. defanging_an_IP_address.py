class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        ans = ""
        for i in range(len(address)):
            if address[i] == ".":
                ans += "[.]"
            else:
                ans += address[i]
        return ans
    
def main(address):
    result = Solution()
    print(result.defangIPaddr(address))

if __name__== "__main__" :
    address = "255.100.50.0"
    main(address)
