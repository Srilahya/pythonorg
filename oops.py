#using super keyword
#
class product():
    def __init__(self,product_name,price,deal_price,rating):
        self.name = product_name
        self.product_price = price
        self.product_deal_price = deal_price
        self.product_rating = rating
    def display_product_details(self):
        print("name",self.name)
        print("product_price",self.product_price)
        print("deal_price",self.product_deal_price)
        print("rating",self.product_rating)
class electronic_product(product):
    def __init__(self,product_name,price,deal_price,rating,waranty):
        super().__init__(product_name,price,deal_price,rating)
        self.product_waranty = waranty
    def display_electronic_details(self):
        super().display_product_details()
        print("waranty",self.product_waranty)
class grocery_product_items(product):
    def __init__(self,product_name,price,deal_price,rating,expirey,packing):
        super().__init__(product_name,price,deal_price,rating)
        self.packing_date = packing
        self.expirey_date = expirey
    def display_grocery_details(self):
        super().display_product_details()
        print("packing",self.packing_date)
        print("expirey",self.expirey_date)
obj=product("oven",5000,3500,4.9)
obj.display_product_details()
print("---------------------------------")
obj1=electronic_product("IQOO",30000,28000,4.9,2)
obj1.display_electronic_details()
print("----------------------------------")
obj2=grocery_product_items("corn",50,35,4,2022,2020)
obj2.display_grocery_details()




#without using super keyword
#
class product():
    def __init__(self,product_name,price,deal_price,rating):
        self.name = product_name
        self.product_price = price
        self.product_deal_price = deal_price
        self.product_rating = rating
    def display_product_details(self):
        print("name: {}".format(self.name))
        print("product_price: {}".format(self.product_price))
        print("deal_price: {}".format(self.product_deal_price))
        print("rating: {}".format(self.product_rating))
class electronic_product(product):
    def set_waranty(self,product_waranty):
        self.product_waranty = product_waranty
        print("waranty: {}".format(self.product_waranty))
class grocery_product_items(product):
    def __init__(self,product_name,price,deal_price,rating,expirey,packing):
        product.__init__(self,product_name,price,deal_price,rating)
        self.packing_date = packing
        self.expirey_date = expirey
    def display_grocery_details(self):
        product.display_product_details()
        print("expirey: {}".format(self.expirey_date))
obj=product("oven",5000,3500,4.9)
obj.display_product_details()
print("=========================")
obj1=electronic_product("iqoo",30000,27000,5)
obj1.display_product_details()
obj1.set_waranty(5)
print("==========================")
obj2=grocery_product_items("corn",50,30,1,2022,2024)
obj2.display_product_details()


#
class order():
    def __init__(self,items,order_type,order_address):
        self.items = items
        self.type = order_type
        self.address = order_address
    def display_order_details(self):
        print("items",self.items)
        print("type",self.type)
        print("address",self.address)
    def


#
class product():
    def __init__(self, product_name, price, deal_price, rating):
        self.name = product_name
        self.product_price = price
        self.product_deal_price = deal_price
        self.product_rating = rating

    def display_product_details(self):
        print("name: {}".format(self.name))
        print("product_price: {}".format(self.product_price))
        print("deal_price: {}".format(self.product_deal_price))
        print("rating: {}".format(self.product_rating))

class electronic_product(product):
    def set_waranty(self, product_waranty):
        self.product_waranty = product_waranty
    def get_waranty(self):
        return self.waranty


class grocery_product_items(product):
    pass

class order():
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("quantity: {}".format(quantity))
    def display_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print("total bill: {}".format(total_bill))

milk = grocery_product_items("milk",40,25,4.0)
tv = electronic_product("tv",50000,45000,4.5)
print("--------------------------------------------")
order = order("prime delivery","bangalore")
order.add_item(milk,2)
print("--------------------------------------------")
order.add_item(tv,1)

print("--------------------------------------------")
order.display_order_details()
print("--------------------------------------------")
order.display_total_bill()













#
a="lahya"
print(a.startswith('l'))

#
a="lahya"
print(a.endswith('y'))

#
a="lahya"
print(a.upper())

#
a="LAHYA"
print(a.lower())

#
a="lahya"
print(a.split())

#
a='''   lahya
        hi
        ttrr'''
print(a.strip())

#
a="lahya"
print(a.replace("lahya","ammu"))

#
a="lahya"
print('my name is {}'.format(a))

#
a=[1,2,3,2,2,3]
print(a.count(2))
print(a.count(3))

#
a="lahya"
print(len(a))

#
a="26790"
print(type(a))
b=int(a)
print(sum(b))
print(max(b))
print(min(b))


#
a=(1,2,3,4,5)
print(sum(a))
print(max(a))
print(min(a))


