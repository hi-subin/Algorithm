function findContentChildren(g: number[], s: number[]): number {
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);

    let g_i = 0, s_i = 0;
    while (g_i < g.length && s_i < s.length) {
        if (s[s_i] >= g[g_i]) {
            g_i++;
        }
        s_i++;
    }

    return g_i;
};