def birthday(user_age):
    user_age = int(input()) + 1
    return user_age
print('Age is:', birthday(25))

def get_minutes_as_hours(minutes):

    return minutes / 60

minutes = float(input())
print('Total Minutes:', get_minutes_as_hours(minutes))

def calc_total_inches(num_feet, num_inches):
    num_feet = feet * 12
    num_inches = inches
   
    return num_feet + num_inches

feet = int(input())
inches = int(input())
print('Total inches:', calc_total_inches(feet, inches))

def calc_pyramid_volume(base_length, base_width, pyramid_height):
    pyramid_height = height
    base_width = width
    base_length = length
    base_area = base_width * base_length
    volume = base_area * 1/3
    return volume * pyramid_height
    

length = float(input())
width = float(input())
height = float(input())
print(f'Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}')

def mph_and_minutes_to_miles(miles_per_hour, miles_traveled):
   return (minutes_traveled / 60 ) * (miles_per_hour)

    

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')