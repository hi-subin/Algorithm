class RecentCounter {
    private queue: number[];
    private front: number;

    constructor() {
        this.queue = [];
        this.front = 0;
    }

    ping(t: number): number {
        this.queue.push(t);
        while (this.queue[this.front] < t - 3000) this.front++;

        return this.queue.length - this.front;
    }
}