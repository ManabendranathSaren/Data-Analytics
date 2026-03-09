def apply_discount(price, discount):
    if type(price) != int and type(price) != float:
        print("The price should be a number")
    elif type(discount) != int and type(discount) != float:
        print("The discount should be a number")
    elif price <= 0:
        print("The price should be greater than 0")
    elif discount < 0 or discount > 100:
        print("The discount should be between 0 and 100")
    else:
        final_price = price-(price * discount/100)
        print("Final cost:", final_price)

apply_discount(74.5,20.0)
