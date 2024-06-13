from tabulate import tabulate
import sqlite3

con = sqlite3.connect('db/store.db')
cur = con.cursor()

class Product:
    @staticmethod
    def add():
        name = input('Enter product name: ')
        price = int(input('Enter product price: '))
        quantity = int(input("Enter product quantity: "))
        cur.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
                    (name, price, quantity))
        con.commit()
        print("Product added successfully.")
        con.close()

    @staticmethod
    def delete():
        Product.list_all()
        product_id = int(input('Enter product id to Delete: '))
        cur.execute('DELETE FROM products WHERE id = ?', (product_id,))
        con.commit()
        print('Product deleted successfully')
        con.close()

    @staticmethod
    def list_all():
        cur.execute('SELECT * FROM products')
        products = cur.fetchall()
        if products:
            headers = ['ID', 'Name', 'Price ', 'Quantity ']
            print(tabulate(products, headers=headers, tablefmt='github'))
        else:
            print('No products found.')
        con.close()
