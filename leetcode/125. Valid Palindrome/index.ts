const isValid = (c: number): boolean => (c > 47 && c < 58) || (c > 96 && c < 123);

const isPalindrome = (s: string): boolean => {
    s = s.toLowerCase();

    for (let l = 0, r = s.length - 1; l <= r; l++) {
        if (!isValid(s[l].charCodeAt(0))) {
            continue;
        }

        if (!isValid(s[r].charCodeAt(0))) {
            l--;
            r--;
            continue;
        }

        if (s[l] !== s[r]) return false;

        r--;
    }

    return true;
};