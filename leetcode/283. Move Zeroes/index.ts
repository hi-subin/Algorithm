function moveZeroes(nums: number[]): void {
    for (let l = 0, r = 0; r < nums.length; r++) {
        if (nums[r]) {
            [nums[r], nums[l]] = [nums[l], nums[r]];
            l++;
        }
    }
};