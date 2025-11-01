N = int(input())
h = list(map(int, input().split()))

# コスト値を格納するリスト
dp = [0]*N

for i in range(N):
    # i=0の時はコストは0
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = abs(h[i] - h[i-1])
    else:
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))
        
# dpのN番目の値のコスト、つまりindex番号がN-1の時のコスト
print(dp[N-1])


