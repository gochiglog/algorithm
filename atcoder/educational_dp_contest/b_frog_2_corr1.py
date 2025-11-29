N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0

# 1番目の足場から N-1 番目まで順に計算
for i in range(1, N):
    
    # 1. 最小コストを保持する変数を無限大で初期化
    min_cost = float('inf') 
    
    # k はジャンプ幅 (1からK)
    for k in range(1, K + 1):
        
        # 範囲チェック
        if i - k >= 0:
            
            # 2. ジャンプ元 (i-k) からのコストを計算
            cost = dp[i-k] + abs(h[i] - h[i-k])
            
            # 3. 最小値を直接更新する (リストへの append はしない)
            min_cost = min(min_cost, cost)
    
    # 4. ループが終わったら、見つけた最小値を dp[i] に設定
    dp[i] = min_cost

print(dp[N-1])