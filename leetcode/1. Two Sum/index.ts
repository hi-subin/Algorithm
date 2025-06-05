const twoSum = (nums: number[], target: number): number[] => {
    const indexMap: Map<number, number> = new Map();

    for (let i = 0; i < nums.length; i++) {
        const diff = indexMap.get(target - nums[i]);
        if (diff !== undefined) return [diff, i];
        
        indexMap.set(nums[i], i);
    }

    return [];
};
