def keep_long_words(words):
    '''
    >>> keep_long_words(['ls', 'codeup', 'code', 'pip', 'bayes'])
    ['codeup', 'bayes']
    >>> keep_long_words(['cd', 'ls', 'pwd'])
    []
    >>> keep_long_words(['python', 'algorithm'])
    ['python', 'algorithm']
    '''
    long_words = []
    # loop through the words list
    for word in words:
    # check if each word is longer than 4 chars
        if len(word) > 4:
            # if it is, add it to a new list
            long_words.append(word)
    # return the list of long words
    return long_words

def make_model(cars):
    '''
    >>> cars = []
    >>> cars.append({'make': 'Toyota', 'model': 'Camry'})
    >>> cars.append({'make': 'Honda', 'model': 'Accord'})
    >>> cars.append({'make': 'Ford', 'model': 'Fiesta'})
    >>> cars.append({'make': 'Ford', 'model': 'F-150'})
    >>> make_model(cars)
    ['Toyota Camry', 'Honda Accord', 'Ford Fiesta', 'Ford F-150']
    '''
    makes_and_models = []
    for car in cars:
        makes_and_models.append(car['make'] + ' ' + car['model'])
    return makes_and_models



import json

with open('profiles.json') as f:
    profiles = json.load(f)

###

active_users = [profile for profile in profiles if profile['isActive']]
n_active_users = len(active_users)

###

inactive_users = [profile for profile in profiles if not profile['isActive']]
n_inactive_users = len(inactive_users)

###

def handle_balance(s):
    return float(s[1:].replace(',', ''))

balances = [handle_balance(profile['balance']) for profile in profiles]
total_balance = sum(balances)
average_balance = sum(balances) / len(balances)

###

user_with_the_lowest_balance
user_with_the_lowest_balance = profiles[0]
for user in profiles[1:]:
    if handle_balance(user['balance']) < handle_balance(user_with_the_lowest_balance['balance']):
        user_with_the_lowest_balance = user

###

user_with_the_highest_balance = profiles[0]
for user in profiles[1:]:
    if handle_balance(user['balance']) > handle_balance(user_with_the_highest_balance['balance']):
        user_with_the_highest_balance = user

user_with_the_highest_balance

### Alternative with a custom key function

min(profiles, key=lambda profile: handle_balance(profile['balance']))
def extract_balance(profile):
    return handle_balance(profile['balance'])
min(profiles, key=extract_balance)

###

from collections import Counter
Counter([p['favoriteFruit'] for p in profiles])

fruit_counts = {}
for profile in profiles:
    fruit = profile['favoriteFruit']
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

###

greetings = [profile['greeting'] for profile in profiles]
def extract_digits(s):
    return int(''.join([c for c in s if c.isdigit()]))
n_unread_messages = [extract_digits(greeting) for greeting in greetings]
sum(n_unread_messages)


{'name': 'Zach', 'favorite_language': 'python'}
me = {}
me['name'] = 'Zach'
me['favorite_langauge'] = 'python'

me['name'] = me['name'].lower()


me['capitalized_name'] = me['name'].capitalize()


instructors = [
    {'name': 'Zach', 'favorite_language': 'clojure'},
    {'name': 'David', 'favorite_language': 'matlab'},
    {'name': 'Maggie', 'favorite_language': 'python'}
]


instructors[1]['favorite_language']

customer_id = data[0]["customer_id"] 
# list of dictionary method
# access particular dictionary value using dictionary key

import itertools

d = {1: 2, 3: 4, 5: 6} # dictionary name has to be "d"

dict(itertools.islice(d.items(), 2))

{1: 2, 3: 4}

def extract_time_components(s):
    '''
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    '''
    parts = s.split(':')
    hours = parts[0]
    minutes = parts[1]
    seconds = parts[2]

    time_dict = {}
    time_dict['hours'] = int(hours)
    time_dict['minutes'] = int(minutes)
    time_dict['seconds'] = int(seconds)

    return time_dict
# string, list, dictionary, tuple indexable
x["seconds"] = int(time_in_24[-2:]) #slicing 







for instructor in instructors:
    print("{}'s favorite language is {}".format(instructor['name'], instructor['favorite_language']))
# format print(  "{}    sfg;ksfgkdg;sgjis   {}".     format(-----------   ,   ---------------))

# What's zach's favorite language (if we don't know his position)?
for instructor in instructors:
    print('DEBUG: looking at instructor: {}'.format(instructor['name']))
    if instructor['name'] == 'Zach':
        print(instructor['favorite_language'])
        break # how to use break, break = end the loop, as soon as found the item, drop it!

# What's zach's favorite language (if we don't know his position)?
for instructor in instructors:
    if instructor['name'] != 'Zach':
        continue # how to use continue, skip all the ones not Zach, go back to the top of loop
        # fulfill if statement, go back to for loop
        # not fulfill if statement: follow thru the for loop 
    print('------')
    print(instructor['name'])
    print(instructor['favorite_language'])

