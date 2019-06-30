prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}
total = 0

for key1, value1 in prices.items():
    print('*',key1, end='\n')
    print('price: ',value1,end='\n')
    for key2, value2 in stock.items():
        if key1 == key2:
            print('stock: ',value2,end='\n')
            mult = (value1 * value2)
            print(mult)
            total += mult

print('The total: ',total)



