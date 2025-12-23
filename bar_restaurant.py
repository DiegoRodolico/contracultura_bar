import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # your MySQL username
    password="",        # your MySQL password
    database="bar_restaurant"
)

cursor = conn.cursor()

# ---------------- MENU MANAGEMENT ----------------
def create_item(item_name, category, price):
    query = "INSERT INTO menu (item_name, category, price) VALUES (%s, %s, %s)"
    cursor.execute(query, (item_name, category, price))
    conn.commit()
    print("Menu item added successfully.")

def read_menu():
    cursor.execute("SELECT * FROM menu")
    for (id, item_name, category, price) in cursor.fetchall():
        print(f"ID: {id}, Item: {item_name}, Category: {category}, Price: {price}")

def update_item(item_id, item_name, category, price):
    query = "UPDATE menu SET item_name=%s, category=%s, price=%s WHERE id=%s"
    cursor.execute(query, (item_name, category, price, item_id))
    conn.commit()
    print("Menu item updated successfully.")

def delete_item(item_id):
    query = "DELETE FROM menu WHERE id=%s"
    cursor.execute(query, (item_id,))
    conn.commit()
    print("Menu item deleted successfully.")

# ---------------- CUSTOMER MANAGEMENT ----------------
def create_customer(name, contact, email):
    query = "INSERT INTO customers (name, contact, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, contact, email))
    conn.commit()
    print("Customer added successfully.")

def read_customers():
    cursor.execute("SELECT * FROM customers")
    for (id, name, contact, email) in cursor.fetchall():
        print(f"ID: {id}, Name: {name}, Contact: {contact}, Email: {email}")

def update_customer(customer_id, name, contact, email):
    query = "UPDATE customers SET name=%s, contact=%s, email=%s WHERE id=%s"
    cursor.execute(query, (name, contact, email, customer_id))
    conn.commit()
    print("Customer updated successfully.")

def delete_customer(customer_id):
    query = "DELETE FROM customers WHERE id=%s"
    cursor.execute(query, (customer_id,))
    conn.commit()
    print("Customer deleted successfully.")

# ---------------- ORDER MANAGEMENT ----------------
def create_order(customer_id, item_id, quantity):
    cursor.execute("SELECT price FROM menu WHERE id=%s", (item_id,))
    result = cursor.fetchone()
    if not result:
        print("Invalid item ID.")
        return
    price = result[0]
    total_price = price * quantity

    query = "INSERT INTO orders (customer_id, item_id, quantity, total_price) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (customer_id, item_id, quantity, total_price))
    conn.commit()
    print("Order placed successfully. Total Price:", total_price)

def read_orders():
    cursor.execute("""
        SELECT orders.id, customers.name, menu.item_name, orders.quantity, orders.total_price 
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        JOIN menu ON orders.item_id = menu.id
    """)
    for (id, customer_name, item_name, quantity, total_price) in cursor.fetchall():
        print(f"Order ID: {id}, Customer: {customer_name}, Item: {item_name}, Quantity: {quantity}, Total: {total_price}")

def delete_order(order_id):
    query = "DELETE FROM orders WHERE id=%s"
    cursor.execute(query, (order_id,))
    conn.commit()
    print("Order deleted successfully.")

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n--- Bar & Restaurant Management System ---")
        print("1. Manage Menu")
        print("2. Manage Customers")
        print("3. Manage Orders")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            while True:
                print("\n--- MENU MANAGEMENT ---")
                print("1. Add Menu Item")
                print("2. View Menu")
                print("3. Update Menu Item")
                print("4. Delete Menu Item")
                print("5. Back to Main Menu")

                ch = input("Enter choice: ")
                if ch == '1':
                    item_name = input("Enter item name: ")
                    category = input("Enter category: ")
                    price = float(input("Enter price: "))
                    create_item(item_name, category, price)
                elif ch == '2':
                    read_menu()
                elif ch == '3':
                    item_id = int(input("Enter item ID to update: "))
                    item_name = input("Enter new item name: ")
                    category = input("Enter new category: ")
                    price = float(input("Enter new price: "))
                    update_item(item_id, item_name, category, price)
                elif ch == '4':
                    item_id = int(input("Enter item ID to delete: "))
                    delete_item(item_id)
                elif ch == '5':
                    break
                else:
                    print("Invalid choice.")

        elif choice == '2':
            while True:
                print("\n--- CUSTOMER MANAGEMENT ---")
                print("1. Add Customer")
                print("2. View Customers")
                print("3. Update Customer")
                print("4. Delete Customer")
                print("5. Back to Main Menu")

                ch = input("Enter choice: ")
                if ch == '1':
                    name = input("Enter name: ")
                    contact = input("Enter contact: ")
                    email = input("Enter email: ")
                    create_customer(name, contact, email)
                elif ch == '2':
                    read_customers()
                elif ch == '3':
                    customer_id = int(input("Enter customer ID to update: "))
                    name = input("Enter new name: ")
                    contact = input("Enter new contact: ")
                    email = input("Enter new email: ")
                    update_customer(customer_id, name, contact, email)
                elif ch == '4':
                    customer_id = int(input("Enter customer ID to delete: "))
                    delete_customer(customer_id)
                elif ch == '5':
                    break
                else:
                    print("Invalid choice.")

        elif choice == '3':
            while True:
                print("\n--- ORDER MANAGEMENT ---")
                print("1. Place New Order")
                print("2. View All Orders")
                print("3. Delete Order")
                print("4. Back to Main Menu")

                ch = input("Enter choice: ")
                if ch == '1':
                    customer_id = int(input("Enter customer ID: "))
                    item_id = int(input("Enter menu item ID: "))
                    quantity = int(input("Enter quantity: "))
                    create_order(customer_id, item_id, quantity)
                elif ch == '2':
                    read_orders()
                elif ch == '3':
                    order_id = int(input("Enter order ID to delete: "))
                    delete_order(order_id)
                elif ch == '4':
                    break
                else:
                    print("Invalid choice.")

        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
