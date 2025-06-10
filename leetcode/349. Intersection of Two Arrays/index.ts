function intersection(nums1: number[], nums2: number[]): number[] {
    let set1 = new Set(nums1);
    let set2 = new Set(nums2);

    if (set1.size > set2.size) {
        [set1, set2] = [set2, set1];
    }

    return Array.from(set1).filter(x => set2.has(x));
};