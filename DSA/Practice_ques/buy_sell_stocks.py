price = [3,2,4,6,1,3,8,6]

max_profit=0
for i in range(0, len(price)):
    for j in range(i+1, len(price)):
        if price[j]>price[i]:
            profit = price[j]-price[i]
            max_profit = max(profit, max_profit)
print(max_profit)
# time complexity = O(n^2)

min_price = float("inf")
max_profit = 0
for i in range(0, len(price)):
    min_price = min(min_price, price[i])
    max_profit = max(max_profit, price[i]-min_price)
    
print(max_profit)

# time complexity = O(n)