import random
wallet=int(input('add amount into the wallet: '))
stocks={
    'TATA':100,
    'SBI':200,
    'OLA':50
    }
portfolio={}

def update_prices():
    for stock in stocks:
        change=random.randint(-20,20)
        new_price=stocks[stock]+change
        stocks[stock]=max(10,new_price)

while True:
    print()
    print('-'*5,'STOCK MARKETING','-'*5)
    for name,price in stocks.items():
             print(f'{name}-{price}')
    print(f'wallet-{wallet}')
    print(f'portfolio-{portfolio if portfolio else 'empty'}')

    choice=input('\n BUY B\n SELL S\n QUIT Q: ').lower()
    
    if choice == 'b':
        stock =input('Buy stocks: ' ).upper()
        if stock not in stocks:
            print('Invalid stock')
            continue
                
        qty=int(input('Enter number of shares: '))

        cost=stocks[stock]*qty

        if cost>wallet:
            max_qty= wallet//stocks[stock]
            print(f'not enough money. you can buy {max_qty} shares')
        else:
            wallet-=cost
            portfolio[stock]=portfolio.get(stock,0) + qty
            print(f'bought - {qty} {stock} for {cost}')
        
    elif choice=='s':
        stock=input('enter stock name: ').upper()
        if stock not in portfolio:
            print('Invalid stock')
            continue

        qty=int(input('enter number of shares: '))
        if qty>portfolio[stock]:
            print(f'you only own {portfolio[stock]} shares')

        else:
            earning=stocks[stock]*qty
            wallet+=earning
            portfolio[stock]=portfolio[stock]-qty
            print(f'sold - {qty} {stock} for {earning}')
    elif choice=='q':
        print(f'wallet-{wallet}')
        print(f'portfolio-{portfolio if portfolio else 'empty'}')
        print('Thanks for trading')
    else:
        print('choose correct choice')
    update_prices()    
        
