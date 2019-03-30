def findMin(arr, n):
    hap = 0
    for i in range(n):
        hap += arr[i]
    dp=[[True for col in range(hap+1)] for row in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(hap+1):
        dp[0][i] = False

    for i in range(1,n+1):
        for j in range(1,hap+1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j]|= dp[i-1][j-arr[i-1]]


    diff = 10000
    for j in range(hap//2,-1,-1):
        if dp[n][j] == True:
            diff = hap-2*j
            break
    return diff


arr=[3,1,4,2,2,1]
n = len(arr)
print('minimum difference between 2 sets is', findMin(arr,n))