function isValid(s: string): boolean {
    const stack: string[] = [];
    const map: Record<string, string> = {
        ')': '(',
        '}': '{',
        ']': '['
    };

    for (const char of s) {
        if ('([{'.includes(char)) stack.push(char);
        else if (map[char] !== stack.pop()) return false;
    }

    return !stack.length;
};