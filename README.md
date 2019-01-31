# SoHo_Project
SoHo project for CodeAcademy Data Structures class

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
    

# PRESENTATION QUESTIONS:
"""
1) 'What data structure did you use for part one? Why did you select these data structures?'

I decided to sort restaurant types using a hashmap. I used the restaurant type as the value, and the type's first letter as the corresponding key. The reason I chose this data structure was because I wanted to index elements according to their first letter. That way, when a user entered the start of a word, the code would be able to quickly retrieve all of the restaurants with the same starting letters.

2) 'What is the runtime (in asymptotic notation) of searching for a food type?'

Runtime is O(N)
Justification:

a) Given a user input, the first letter of that input is hashed to find the corresponding index of that letter within the map. Runtime: O(1).

b) At that index is a list of restaurant types with the same first letter. If the user's input was longer than one letter, The code must iterate through the list to see if the second letter of the user's input matches the second letter of any of the restaurant types. RuntimeO(N)

Therefore total run time is O(N)

I don't believe that there is a more efficiant worse case run time, but I do think that a Trie would perform better on average. #JUSTIFY.

3) In this part, I also sorted restaurant data into a hashmap, this time with the restaurant's data as the value and the user's choice of cuisine as the key.

I chose this data structure because I wanted to quickly access all of the restaurants of a particular cuisine. In fact, I noticed that my needs in this part were almost identical to my needs in part one:

I had a large collection of objects I wanted grouped up according to some 'key' piece of information. In part one, I wanted cuisine types grouped up by their first letter. In part 2, I wanted restaurant types grouped up by their cuisine.

4) 'What is the runtime of retrieving the restaurant data? Do you think there's a more efficiant runtime?'

Runtime is O(N):
Justification:

I wanted to print all restaurants of a specific cuisine type. Given N restaurants, the worst case scenario would be if all N restaurants had the same cuisine tpye. Therefore I have reason to believe that the hashmap is the most efficiant data structure for this job.

5)  'Outside of this project, what are other innovative ways you can use data structures?'

+ Lists of golf players and their scores could be sorted in increasing order using a heap.

+ A weighted graph could be used to simulate a simple circuit board with resistors.

+ A tree could be used as the data structure behind a 'what number am I thinking of' game?

"""
