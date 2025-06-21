function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    const dy = [0, 1, 0, -1], dx = [1, 0, -1, 0];
    const queue: number[][] = [], visited: boolean[][] = image.map(row => row.map(_ => false));
    
    queue.push([sr, sc]);
    visited[sr][sc] = true;

    let startColor = image[sr][sc];
    image[sr][sc] = color;

    while (queue.length) {
        const [y, x] = queue.shift() as number[];
        let flag = false;

        for (let i = 0; i < 4; i++) {
            const ny = y + dy[i], nx = x + dx[i];

            if (
                (ny >= 0 && ny < image.length) &&
                (nx >= 0 && nx < image[0].length) &&
                !visited[ny][nx] &&
                image[ny][nx] === startColor
            ) {
                flag = true;
                visited[ny][nx] = true;
                queue.push([ny, nx]);
                image[ny][nx] = color;
            }
        }
    }

    return image;
};