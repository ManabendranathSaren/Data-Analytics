total = 0
no_of_friends = 4
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

total += appetizers + main_courses + desserts + drinks
print("Total is:", total)
tip = total * 0.25
print("Tip is:", tip)
total += tip
print("Total bill with tip:", total)

final_bill  = total / no_of_friends
print("Bill per person:", final_bill)

each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)
