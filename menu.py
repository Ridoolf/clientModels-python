from package_client.client import Client

my_client = Client('Lucas', 'password123', 'lucas@mail.com')
print(my_client)

my_client.add_product_to_cart('Iphone 15 Pro Max')
my_client.add_product_to_cart('PS5') # la re plata tenia jajaja

my_client.make_purchase()