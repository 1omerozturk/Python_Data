my_name="Ben"
my_surname="Omer"
my_age=22
ID_number=123456789
where_i_live='Van'

print(f"My name is {my_name} {my_surname} and I am {str(my_age)} years old. I live in {where_i_live}")
limit=5000
item_list=["Laptop", "Headset","Second monitor","Mousepad","USB drive","External drive"]

price_sheet={
    'Laptop':1500,
    'Headset':100,
    'Second monitor':200,
    'Mousepad':50,
    'USB drive':25,
    'External drive':250
}

cart=[]

def add_to_cart(item,quanity):
    cart.append((item,quanity))
    item_list.remove(item)
    
def create_invoice():
    total_amount_inc_tax=0
    for item,quanity in cart:
        price=price_sheet[item]
        tax=0.18*price
        total=(tax+price)*quanity
        total_amount_inc_tax+=total
        print('Item:',item,'\t','Price:',price,'\t','Quantity:',quanity,'\t','Tax:',tax ,'\t','Total:',total,'\n')
        
    print('After the taxes are applied the totla amount is:','\t',total_amount_inc_tax)
    return total_amount_inc_tax
    
def checkout():
    global limit
    total_amount=create_invoice()
    if limit==0:
        print("You don't have any budget")
    elif total_amount>limit:
        print("The amount you have to pay is above the spending limit. You have to drop some items.")
    else:
        limit-=total_amount
        print(f"The total amount (incl. taxes) you've paid is {total_amount}. You have {limit} dollars left")
    
add_to_cart("Laptop",1)
add_to_cart("Headset",8)
add_to_cart("Second monitor",1)
add_to_cart("Mousepad",1)
add_to_cart("USB drive",2)
add_to_cart('External drive',4)
print("\n")
checkout()
print("\n")