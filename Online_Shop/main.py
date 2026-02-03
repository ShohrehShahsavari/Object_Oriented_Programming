from classes import *

ProductFactory.register_product('rug', Rug)
ProductFactory.register_product('mobile', Mobile)
ProductFactory.register_product('giftcard', GiftCard)

if __name__ == '__main__':
    r1 = ProductFactory.create_product('rug', initial_price =100, company='persian rug', shaneh=700)
    m1 = ProductFactory.create_product('mobile', initial_price=700, company='Samsung', year=2024)
    g1 =ProductFactory.create_product('giftcard', initial_price=20, company='google', max_price=60)
    
    products = [r1, m1, g1]
    for product in products:
        print(product.detail)
        print('='*50)

# for product_type, product_class in ProductFactory._products.items():
#     print(f"Type: {product_type}")
#     print(f"Class: {product_class.__name__}")
#     print(f"Module: {product_class.__module__}")
#     print(f"Detail: {product_class.detail}")
#     print("-" * 30)
