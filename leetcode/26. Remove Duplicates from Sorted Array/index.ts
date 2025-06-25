function removeDuplicates(nums: number[]): number {
    let k: number = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== nums[k]) {
            k++;
            nums[k] = nums[i];
        }
    }

    return k + 1;
};