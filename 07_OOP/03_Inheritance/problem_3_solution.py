class Product:
    def __init__(self, Product_name,Product_ID,Price):
        self.Product_name=Product_name
        self.Product_ID=Product_ID
        self.Price=Price

    def display_info(self):
        print("Product:", self.Product_name)
        print("ID:", self.Product_ID)
        print("Price: RM", self.Price)

class Electronics(Product):
    def __init__(self, Product_name,Product_ID,Price,Warranty):
        super().__init__(Product_name,Product_ID,Price)
        self.Warranty=Warranty

    def display_info(self):
        super().display_info()
        print("Warranty:", self.Warranty, "years")


class Clothing(Product):
    def __init__(self,Product_name,Product_ID,Price,Size):
        super().__init__(Product_name,Product_ID,Price)
        self.Size=Size

    def display_info(self):
        super().display_info()
        print("Size:", self.Size)
    

class Food(Product):
    def __init__(self,Product_name,Product_ID,Price,Expiry_date):
        super().__init__(Product_name,Product_ID,Price)
        self.Expiry_date=Expiry_date

    def display_info(self):
        super().display_info()
        print("Expiry date:", self.Expiry_date)


laptop = Electronics("Laptop", "P001", 3000, 2)

shirt = Clothing("T-Shirt", "P002", 50, "M")

chocolate = Food("Chocolate", "P003", 10, "2026-12-30")


laptop.display_info()
shirt.display_info()

chocolate.display_info()
