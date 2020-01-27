cart=[]
def greeting(name):
    print("Hello %s , welcome to the grocery store" % name)

def user_shopping(cart):
    item_name = input("What products did your purchase? ")
    while item_name != "done":
        item_quantity = int(input("Enter the quantity of your item: "))
        item_price = int(input("Enter the price of your item: "))

        item = {
            "name": item_name,
            "quantity": item_quantity,
            "price": item_price
    }

        cart.append(item)
        item_name = input("What products did you purchase? ")

name = input("What is your name? ")
greeting(name)

user_shopping(cart)
print()
print("---------------------")
print("reciept")
print("--------------------")
print()
total=0.0
for item in cart:
    print("%d %s %f KWD" %(item['quantity'], item['name'], item['price']))
    total+= (item['quantity']*item['price'])
print("Total Price: %f KWD"% total)






    

