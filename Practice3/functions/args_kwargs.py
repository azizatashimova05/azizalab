# Использование *args и **kwargs 
def make_pizza(size, *toppings, **details):
    """Собирает информацию о заказе пиццы"""
    print(f"\nMaking a {size}-inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")
    
    if 'delivery' in details:
        print(f"Delivery: {details['delivery']}")

make_pizza(12, 'mushrooms', 'extra cheese', delivery='Express')
