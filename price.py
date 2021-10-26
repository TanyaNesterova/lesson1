def discounted(price, discount, max_discount=20):
   try:
      price=abs(float(price))
      discount=abs(float(discount))
      max_discount=int(max_discount)
      if discount>=max_discount:
         print(price)
      else:
         print(price-(price*discount/100))
   except (KeyboardInterrupt, ValueError, TypeError):
      print("не коректные данные")

discounted (100, 10.3)