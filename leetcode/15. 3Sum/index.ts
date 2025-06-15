function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const answers: number[][] = [];

    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let l = i + 1, r = nums.length - 1;
        while (l < r) {
            const sum = nums[i] + nums[l] + nums[r];

            if (sum === 0) {
                answers.push([nums[i], nums[l], nums[r]]);

                while (nums[l] === nums[l + 1]) l++;
                while (nums[r] === nums[r - 1]) r--;

                l++;
                r--;
            } else if (sum < 0) {
                l++;
            } else {
                r--;
            }
        }
    }

    return answers;
};