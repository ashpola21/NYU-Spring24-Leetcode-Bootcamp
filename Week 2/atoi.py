class Solution:
    def myAtoi(self, s: str) -> int:

        sum, num, flag = 1, 0, 0
        s = s.strip()  # this removes any spaces in the string s
        if len(s) == 0:
            return 0
        if s[0] == "-":
            sum = -1
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)  # converting the digits into integers
                flag = 1
            elif (i == "+" or i == "-") and flag == 0:
                flag = 1
                pass
            else:
                break
        num = num*sum
        if (-2**31 <= num <= (2**31)-1):
            return num  # checking if num is within the range
        if num < 0:
            return -2**31
        else:
            return 2**31-1
