class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        c = 0
        dp[0] = 1

        for i in range(1, n):
            dp[i] = c + dp[i-delay] - dp[i-forget]
            c = dp[i]

        return sum(dp[n-forget:]) % 1000000007
