from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()

# Prints restaurant data in a nice way
def print_restaurants(restaurant_list):
  print("Name: {0}".format(restaurant[1]))
  print("Price: {0}/5".format(restaurant[2]))
  print("Rating: {0}/5".format(restaurant[3]))
  print("Address: {0}".format(restaurant[4]))
  print("\n-------------\n")

# gets a valid response to a yes or no question
def get_valid_response():
  response = input().lower()
  while response not in ('y','n'):
    print('Please enter\'y\' or \'n\'')
    response = input().lower()
  return response
  
#Inserting food types into a data structure
type_map = HashMap(30)
for cuisine in types:
  # value_list is a list of all cuisines starting with the same letter
  value_list = type_map.retrieve(cuisine[0])
  if value_list is None:
    # def: assign(self, key, value)
  	type_map.assign(cuisine[0],[cuisine])
  else:
    value_list += [cuisine]
    type_map.assign(cuisine[0],value_list)

    
#Inserting restaurant data into a data structure
restaurant_map = HashMap(100)
for restaurant in restaurant_data:
  # cuisine type as key and restaurant name as value
  restaurant_type = restaurant[0]
  # restaurant_list is a list of restaurants with the same cuisine (I.E. Korean)
  restaurant_list = restaurant_map.retrieve(restaurant_type)
  if restaurant_list is None:
    restaurant_map.assign(restaurant_type,[restaurant])
  else:
    restaurant_list += [restaurant]
    restaurant_map.assign(restaurant_type,restaurant_list)
  
#Code for user interaction
while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    
    # FORMAT: map.retrieve(self,key)
    type_list = type_map.retrieve(user_input[0])
    
    if len(user_input) > 1 and type_list:
      # Search for items that match the second character
      new_list = []
      for cuisine in type_list:
        if cuisine[1] == user_input[1]:
          new_list += [cuisine]
      type_list = new_list
      
      # Search engine is functional but only adequate for up to two characters. Fix 1: Use a while loop to iterate through the chars of user_input. Fix 2: Use a Trie.

    if type_list:
      
      if len(type_list) > 1:
        print("With those beginning letters, your choices are {0}".format(type_list))
        
      elif len(type_list) == 1:
        print("The only option with those beginning letters is {0}. Do you wish to look at {1} restaurants? Enter \'y\' for yes and \'n\' for no".format(type_list[0],type_list[0]))
        yes_or_no = get_valid_response()
        
        if yes_or_no == 'y':
          cuisine_choice = type_list[0]
          restaurant_list = restaurant_map.retrieve(cuisine_choice)
          print("Here are your restaurants!")
          print("\n---------------\n")
          
          for restaurant in restaurant_list:
            print_restaurants(restaurant_list)
          print("Do you want to find other restaurants? Enter \'y\' for yes and \'n\' for no.")
          yes_or_no = get_valid_response()
          if yes_or_no == 'n':
            break

    else:
      print("No food for you! Try again!")
    



