"""
11726 - 2xn 타일링
https://www.acmicpc.net/problem/11726
"""
from sys import stdin

input = stdin.readline

dp = [0 for _ in range(1001)]
dp[1], dp[2] = 1, 2

for i in range(3, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]

n = int(input())
print(dp[n] % 10007)
