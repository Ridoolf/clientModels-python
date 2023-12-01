class Client:
    def __init__(self, user, password, mail, cart=[]):
        self.user = user
        self.__password = password
        self.__mail = mail
        self.cart = cart
    
    def __str__(self):
        return f'Cliente: {self.user}'
        
    def add_product_to_cart(self, product):
        self.cart.append(product)
        print(f'{product} agregado al carrito')

    def make_purchase(self):
        if len(self.cart) > 0:
            print(f'{self.user} ha realizado una compra')
            self.cart = []
        else:
            print(f'El carrito de {self.user} esta vacio')