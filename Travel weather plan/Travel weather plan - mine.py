distance_mi = 1
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

if distance_mi <= 1 and not is_raining :
    print("True")
    print("You can go out it's close")

elif distance_mi >1 and distance_mi <= 6 and has_bike and not is_raining :
    print("True")
    print("You can go out with your bike")

elif distance_mi > 6 and (has_car or has_ride_share_app) :
    print("True")
    print("You can go out in car")

else:
    print("False")
