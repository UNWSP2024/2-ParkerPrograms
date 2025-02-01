#Nathan Parker
#1/31/25
#Program #3:Total Purchase

#get the inputs of the five items
item_1 = float(input('Enter the price of the first item: '))
item_2 = float(input('Enter the price of the second item: '))
item_3 = float(input('Enter the price of the third item: '))
item_4 = float(input('Enter the price of the fourth item: '))
item_5 = float(input('Enter the price of the fifth item: '))

#clalculate the subtotal
subtotal = item_1 + item_2 + item_3 + item_4 + item_5

#calculate the sales tax
sales_tax = 0.07 * subtotal

#calculate the total
total_price = subtotal + sales_tax

#print the subtotal
print(f'Subtotal: ${subtotal:,.2f}')

#print the sales tax
print(f'Sales tax: ${sales_tax:,.2f}')

#print the total
print(f'Total: ${total_price:,.2f}')
