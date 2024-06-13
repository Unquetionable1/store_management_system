from classes.products import Product
from classes.orders import Orders
from classes.customers import Customer


class StoreManagement:
    @staticmethod
    def run():
        while True:
            choice = input("""
            1. Add Product
            2. Delete Product
            3. List Products
            4. Add Customer
            5. Delete Customer
            6. List Customers
            7. Add Orders
            8. Delete Orders
            9. List Orders
            10. Exit

            Enter your choice: """)
            if choice == '1':
                Product.add()
            elif choice == '2':
                Product.delete()
            elif choice == '3':
                Product.list_all()
            elif choice == '4':
                Customer.add()
            elif choice == '5':
                Customer.delete()
            elif choice == '6':
                Customer.list_all()
            elif choice == '7':
                Orders.add()
            elif choice == '8':
                Orders.delete()
            elif choice == '9':
                Orders.list_all()
            elif choice == '10':
                print("Exiting store management system.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == '__main__':
    store_management = StoreManagement()
    store_management.run()
