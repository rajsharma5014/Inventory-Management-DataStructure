# ELECTRONICS SHOP INVENTORY MANAGEMENT SYSTEM

# ---------------- PRODUCT NODE ----------------
class ProductNode:
    def __init__(self, product_id, name, brand,
                 quantity, price, warranty):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price
        self.warranty = warranty
        self.next = None

# ---------------- INVENTORY MANAGER ----------------
class InventoryManager:
    def __init__(self):
        self.head = None
        self.next_id = 1

    # ADD PRODUCT
    def add_product(self):
        print()
        print("---------------- ADD PRODUCT ----------------")
        name = input("Enter Product Name: ")
        brand = input("Enter Brand: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        warranty = input("Enter Warranty: ")

        # Create new product node
        new_product = ProductNode(
            self.next_id,
            name,
            brand,
            quantity,
            price,
            warranty
        )

        # If linked list is empty
        if self.head is None:
            self.head = new_product

        # If linked list already contains products
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_product
        print()
        print("Product added successfully!")
        print("Product ID:", self.next_id)
        self.next_id = self.next_id + 1

    # DISPLAY ALL PRODUCTS
    def display_products(self):
        print()
        print("--------------- ALL PRODUCTS ---------------")
        if self.head is None:
            print("No products available.")
            return
        current = self.head
        while current is not None:
            print()
            print("Product ID :", current.product_id)
            print("Product    :", current.name)
            print("Brand      :", current.brand)
            print("Quantity   :", current.quantity)
            print("Price      : Rs.", current.price)
            print("Warranty   :", current.warranty)
            print("--------------------------------------------")
            current = current.next
            
    # SEARCH PRODUCT
    def search_product(self):
        print()
        print("---------------- SEARCH PRODUCT ----------------")
        search = input("Enter Product ID or Product Name: ")
        current = self.head
        found = False
        while current is not None:
            if str(current.product_id) == search:
                print()
                print("Product Found!")
                print("Product ID :", current.product_id)
                print("Product    :", current.name)
                print("Brand      :", current.brand)
                print("Quantity   :", current.quantity)
                print("Price      : Rs.", current.price)
                print("Warranty   :", current.warranty)
                found = True
            elif current.name.lower() == search.lower():
                print()
                print("Product Found!")
                print("Product ID :", current.product_id)
                print("Product    :", current.name)
                print("Brand      :", current.brand)
                print("Quantity   :", current.quantity)
                print("Price      : Rs.", current.price)
                print("Warranty   :", current.warranty)
                found = True
            current = current.next
        if found == False:
            print("Product not found.")

    # UPDATE PRODUCT
    def update_product(self):
        print()
        print("---------------- UPDATE PRODUCT ----------------")
        product_id = int(input("Enter Product ID: "))
        current = self.head
        while current is not None:
            if current.product_id == product_id:
                print()
                print("Current Product Details:")
                print("Product :", current.name)
                print("Brand   :", current.brand)
                print("Quantity:", current.quantity)
                print("Price   :", current.price)
                print("Warranty:", current.warranty)
                print()
                print("Enter New Details:")
                current.name = input("Enter Product Name: ")
                current.brand = input("Enter Brand: ")
                current.quantity = int(input("Enter Quantity: "))
                current.price = float(input("Enter Price: "))
                current.warranty = input("Enter Warranty: ")
                print()
                print("Product updated successfully!")
                return
            current = current.next
        print("Product not found.")

    # DELETE PRODUCT
    def delete_product(self):
        print()
        print("---------------- DELETE PRODUCT ----------------")
        product_id = int(input("Enter Product ID: "))
        current = self.head
        previous = None
        while current is not None:
            if current.product_id == product_id:
                print("Product:", current.name)
                confirm = input(
                    "Do you want to delete this product? (y/n): "
                )
                if confirm.lower() == "y":
                    # Delete first node
                    if previous is None:
                        self.head = current.next
                    # Delete middle or last node
                    else:
                        previous.next = current.next
                    print("Product deleted successfully!")
                else:
                    print("Deletion cancelled.")
                return
            previous = current
            current = current.next
        print("Product not found.")

    # STOCK IN
    def stock_in(self):
        print()
        print("---------------- STOCK IN ----------------")
        product_id = int(input("Enter Product ID: "))
        amount = int(input("Enter Quantity to Add: "))
        current = self.head
        while current is not None:
            if current.product_id == product_id:
                current.quantity = current.quantity + amount
                print()
                print("Stock added successfully!")
                print("New Quantity:", current.quantity)
                return
            current = current.next
        print("Product not found.")

    # STOCK OUT
    def stock_out(self):
        print()
        print("---------------- STOCK OUT ----------------")
        product_id = int(input("Enter Product ID: "))
        amount = int(input("Enter Quantity to Remove: "))
        current = self.head
        while current is not None:
            if current.product_id == product_id:
                if amount > current.quantity:
                    print("Insufficient stock.")
                else:
                    current.quantity = current.quantity - amount
                    print()
                    print("Stock removed successfully!")
                    print("Remaining Quantity:",
                          current.quantity)
                return
            current = current.next
        print("Product not found.")

    # LOW STOCK
    def low_stock(self):
        print()
        print("---------------- LOW STOCK PRODUCTS ----------------")
        current = self.head
        found = False
        while current is not None:
            if current.quantity < 10:
                print()
                print("Product ID :", current.product_id)
                print("Product    :", current.name)
                print("Brand      :", current.brand)
                print("Quantity   :", current.quantity)
                print("Status     : LOW STOCK")
                print("-----------------------------")
                found = True
            current = current.next
        if found == False:
            print("No low-stock products.")
            
    # TOTAL INVENTORY VALUE
    def total_inventory_value(self):
        print()
        print("---------------- INVENTORY VALUE ----------------")
        current = self.head
        total = 0
        while current is not None:
            total = total + (
                current.quantity * current.price
            )
            current = current.next
        print("Total Inventory Value: Rs.", total)

# MAIN PROGRAM
inventory = InventoryManager()
while True:
    print()
    print("================================================")
    print("       ELECTRONICS SHOP INVENTORY SYSTEM")
    print("================================================")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Stock In")
    print("7. Stock Out")
    print("8. Low Stock Products")
    print("9. Total Inventory Value")
    print("10. Exit")
    print("================================================")
    choice = input("Enter your choice: ")
    if choice == "1":
        inventory.add_product()
    elif choice == "2":
        inventory.display_products()
    elif choice == "3":
        inventory.search_product()
    elif choice == "4":
        inventory.update_product()
    elif choice == "5":
        inventory.delete_product()
    elif choice == "6":
        inventory.stock_in()
    elif choice == "7":
        inventory.stock_out()
    elif choice == "8":
        inventory.low_stock()
    elif choice == "9":
        inventory.total_inventory_value()
    elif choice == "10":
        print()
        print("Thank you for using")
        print("Electronics Shop Inventory System!")
        break
    else:
        print("Invalid choice. Please try again.")
