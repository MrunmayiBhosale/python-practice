#set

print("\n---Product Management---\n")
products = {"Laptop", "Mouse", "Keyboard", "Monitor", "Printer"}
discount_products = {"Mouse", "Monitor", "Printer"}

#display product list
print("Products List:", products)
print("Discount Products:", discount_products)

#Add a product
new_product = input("\nEnter new product:")
products.add(new_product)
print("Product is added successfully.")
print("Products:", products)

#Add multiple products
new_products = input("\nEnter multiple products separated by comma:")
new_products = set(new_products.split(","))
products.update(new_products)
print("Multiple products are added successfully.")
print("Products:", products)

#remove product
remove_product = input("\nEnter product to remove: ")
if remove_product in products:
    products.remove(remove_product)
    print("Product is removed successfully.")
else:
    print("Product not found.")
print("Products:", products)

#search product
check_product = input("\nEnter product to check:")
if check_product in products:
    print(check_product, "is available.")
else:
    print(check_product, "is not available.")

#check discount on products
discount_available = products.intersection(discount_products)
print("\nDiscount Products Available:", discount_available)