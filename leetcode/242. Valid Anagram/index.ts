function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    let count = Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        count[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
        count[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
    }

    return count.every(c => c === 0);
};