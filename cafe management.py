#python mini project-CAFE MANAGEMENT
#step1:Greeting the user
#step2:Showing menu{'pizza':50,'salad':30,'burger':100,'popcorn':150}
#step3:note the item
#step4:check item in our menu
#         if yes:add cost
#            ask user for anything else
#             if yes:note the second item
#                     check item in our menu
#                      calculate total cost& display
#             if no:end order & display cost
#         if no: error


menu= {
       'pizza':50,'salad':30,'burger':100,'popcorn':150,'chicken puff':150,'samosa':20
       }
print('Welcome to our Thuhi Cafe')
print(' pizza:50\n salad:30\n burger:100\n popcorn:150\n chicken puff:100\n samosa:20')
order_item=input('Enter your item: ')

order_total=0

if order_item in menu:
    order_total += menu[order_item]
    order=input('Do you want anything else (Yes/No):')
    if order == 'Yes':
        order_item2 = input('Enter your second item: ')
        if order_item2 in menu:
            order_total += menu[order_item2]
            print(f'Your order value {order_total}')
    else:
        print(f'Your order value {order_total}')
else:
    print('You entered a wrong item')
