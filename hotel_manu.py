#menu of the resturent
menu={
    'Coffee':80,
    'Cappuccino':120,
    'Chicken Burger':150,
    'Veggie Barger': 120,
    'Pizza':200,
    'French Fries':80,
    'Salad':60,
    'Ice Cream': 70,
}
#Greet
print("Wlcome to our Resturent")
print("Coffee:80\nCappuccino:120\nChicken Burger:150\nVeggie Barger: 120\nPizza:200\nFrench Fries:80\nSalad:60\nIce Cream: 70")

#80+60=140
total_order=0

#order 1
item_1=input("Enter the name of item you want to order: ")
if item_1 in menu:
    total_order+=menu[item_1]    #0+ 
    print("Your item",item_1,"Has been added to your order")
else:
    print(f"Sorry! Orderd {item_1} is not available yet")

#another order
order_2=input("Do you wnat to add another item? (Yes/No): ")
if order_2=="yes":
    item_2=input("Enter the second item name you want to add: ")
    if item_2 in menu:
        total_order+=menu[item_2]
        print(f"Item {item_2} has been added to the order")
    else:
        print(f"Sorry! ordered {item_2} is not available!")
print(f"Total amount to pay is: {total_order}")