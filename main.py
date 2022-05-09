print('hello world!')
import random
destinations = [' Jupiter', ' Saturn', ' Mercury', ' Neptune']
restaurants = [' Space Mcdonalds', ' Space Subway', ' Space Taco Bell', ' Space Chick-fil-a']
transportations = [' land rover', ' hover craft', ' teleportation device']
entertainments = [' Collect the coolest space rocks', ' Go to the Alien Gladiator Pit', ' Explore the core of the planet']


def destination_generator():
    destination_choice = False

    while destination_choice == False:
     destination = random.choice(destinations) 
     print('We have picked' + (destination) + ' for your desination! How exciting!')
     user_input = input('Do you want to take a trip to this planet? Enter y/n: ')
     if user_input == "y":
        destination_choice = True
        print('Awesome! Glad that is decided, lets move on.')
        return destination
     else:
        print('Sorry to hear that! Lets find you another destination.')

def restaurants_generator():
    restaurant_choice = False

    while restaurant_choice == False:
     restaurant = random.choice(restaurants)
     print('We have picked' + (restaurant) + ' for your restaurant, its the best around!')
     user_input = input('Do you want to eat here? Enter y/n: ')
     if user_input == "y":
        print('Awesome! Glad that is decided, lets move on.')
        return restaurant
     else:
        print('Sorry to hear that! Lets find you another restaurant.')
    
def transportation_generator():
    transportation_choice = False
    
    while transportation_choice == False:
     transportation = random.choice(transportations)
     print('We have picked' + (transportation) + ' for the way you get around!')
     user_input = input('Do you want to get around this way? Enter y/n: ')
     if user_input == 'y':
        print('Awesome! Glad that is decided! Lets move on.')
        return transportation
     else:
        print('Sorry to hear that! Lets find you another way to get around.')
          
def entertainment_generator():
    entertainment_choice = False

    while entertainment_choice == False:
     entertianment = random.choice(entertainments)
     print('We have picked' + (entertianment) + ' for your entertainment option. Sounds like fun!')
     user_input = input('Does this sound good? Enter y/n: ')
     if user_input == 'y':
        print('Awesome! Glad that is decided, lets move on.')
        return entertianment
     else:
        print('Sorry to hear that! Lets find you a different entertainment option.')

def trip_generatror():
    trip_satifaction = False

    if trip_satifaction == False:
        if user_input ==  'n':
            print('Hey now worries! Lets find one that will work for you!')
            returned_destination = destination_generator()
            returned_transportation = transportation_generator()
            returned_entertainment = entertainment_generator()
            returned_restaurant = restaurants_generator()
        else:
            print("Thats amazing to here!") 
        






print('Welcome to the best random space trip generator in the galaxy! Let is help you on your next adventure!')
returned_destination = destination_generator()
returned_transportation = transportation_generator()
returned_entertainment = entertainment_generator()
returned_restaurant = restaurants_generator()


print('Congrats! You now have an amazing trip planned for you! Now lets just confirm that this is the trip you wanted.')
print('The trip we have generated for you is:')
print('Destination:' + (returned_destination))
print('Transportation:' + (returned_transportation))
print('Entertainment:' + (returned_entertainment))
print('Restaurant' + (returned_restaurant))
user_input = input('Would you like to finalize this trip? Enter y/n: ')
trip_generatror()
print('We are so very happy to hear that!' + 'You will be arriving in ' + (returned_destination) + ' by ' + (returned_transportation) + ', where you will spend the day' + (returned_entertainment) + '.' + 'You will end the evening dining at the most prestigious ' + (returned_restaurant) + ' around!')

