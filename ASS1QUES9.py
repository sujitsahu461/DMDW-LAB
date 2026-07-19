#Write a program to create a class for Product having member data: Product No, Product Name, Cost, Quantity, Total Amount. Member functions: input(), calculator(), display(). Calculator() is used to find Total Amount = Cost × Quantity. Input 5 product details and display the product whose total cost is highest.

class Product:
    def input(self):
        self.product_no = int(input("Enter the product number: "))
        self.product_name = input("Enter the name: ")
        self.cost = int(input("Enter the cost: "))
        self.quantity = int(input("Enter the quantity: "))
    def calculator(self):
        self.total_amount = self.cost * self.quantity
    def display(self):
        print("Product No:", self.product_no)
        print("Product Name:", self.product_name)
        print("Cost:", self.cost)
        print("Quantity:", self.quantity)
        print("Total Amount:", self.total_amount)
pk = []
for i in range(5):
    print("Enter Product", i + 1)
    p = Product()
    p.input()
    p.calculator()
    pk.append(p)
high = pk[0]
for p in pk:
    if p.total_amount > high.total_amount:
        high = p
print("\nHighest Cost Product")
high.display()