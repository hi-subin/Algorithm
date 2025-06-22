let dp = Array(46);
function climbStairs(n: number): number {
    if (dp[n]) return dp[n];
    
    if (n === 1) return 1;
    if (n === 2) return 2;

    dp[n] = climbStairs(n - 1) + climbStairs(n - 2);
    return dp[n];
};