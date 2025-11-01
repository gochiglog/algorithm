# N, K = map(int, input().split())

# h = list(map(int, input().split()))

# if K >= N:
#     K = N-1

# dp = [0]*N


# for i in range(N):
#     # ★tempを初期化するのを忘れていた
#     temp = []
#     if i == 0:
#         dp[i] = 0
#     else: 
#         for k in range(1, K):
#             temp.append(abs(h[i]- h[i-k]))
#         print(f'N={i+1}の時、{temp}')
#         dp[i] = min(temp)

# print(dp[N-1])


N, K = map(int, input().split())
h = list(map(int, input().split()))

if K >= N:
    K = N-1

# ★minを使うので、初期値は無限大にする
dp = [float('inf')]*N


for i in range(N):
    # ★tempを初期化するのを忘れていた
    temp = []
    if i == 0:
        dp[i] = 0
    else: 
        # ★range(N)とrange(1, N+1)の違いに注意
        for k in range(1, K+1):
            temp.append(dp[i-k] + abs(h[i]- h[i-k]))
        print(f'N={i+1}の時、{temp}')
        print(f'N={i+1}の時、{dp}')
        dp[i] = min(dp[i], min(temp))


print(dp[N-1])