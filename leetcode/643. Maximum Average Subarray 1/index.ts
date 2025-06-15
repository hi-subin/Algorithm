function findMaxAverage(nums: number[], k: number): number {
    let cur = nums.slice(0, k).reduce((a, c) => a + c, 0);
    let max = cur;

    for (let i = k; i < nums.length; i++) {
        cur = cur - nums[i - k] + nums[i];
        max = Math.max(max, cur);
    }

    return max / k;
};