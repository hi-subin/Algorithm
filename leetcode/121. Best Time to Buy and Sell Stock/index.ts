const maxProfit = (prices: number[]): number => {
    let buy = prices[0], profit = 0;

    for (let i = 1; i < prices.length; i++) {
        if (prices[i] < buy) {
            buy = prices[i];
        }

        const newProfit = prices[i] - buy;
        
        if (newProfit > profit) {
            profit = newProfit;
        }
    } 

    return profit;
};