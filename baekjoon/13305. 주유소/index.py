N = int(input())
distanceList = list(map(int, input().split()))
priceList = list(map(int, input().split()))

min_price = 1000000000
result = 0
for i in range(N - 1):
    if min_price > priceList[i]:
        min_price = priceList[i]
    result += min_price * distanceList[i]

print(result)
