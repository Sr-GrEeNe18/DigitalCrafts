# 5
# x = 5
# x + 1
# x = y = 1
# x = 5.
# pi = 3.1415926535897931
# r = 5.0
# v = 4.0/3.0*pi* r**3
# print('volume of the sphere is: ', v)

# book_price = 24.95 * .04 + 3
# copies = 60 * .75
# total = book_price + copies
# print(total)

# start_time_hr = 6 + 52 / 60.0
# easy_pace_hr = (8 + 15 / 60.0 ) / 60.0
# tempo_pace_hr = (7 + 12 / 60.0) / 60.0
# running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
# breakfast_hr = start_time_hr + running_time_hr
# breakfast_min = (breakfast_hr-int(breakfast_hr))*60
# breakfast_sec= (breakfast_min-int(breakfast_min))*60 
# print ('breakfast_hr', int(breakfast_hr) )
# print ('breakfast_min', int (breakfast_min) )
# print ('breakfast_sec', int (breakfast_sec) )

# front = 'JKLMNOPQ'
# back = 'ack'

# for letter in front:
#     print(letter + back)

# b = "Hello, World!"
# print(b[2:5])
# fruit = 'banana'
# fruit [:] 
# print(fruit)
# 
#  def find(word, letter):
# def find(word, letter, prime):
#     for index in range(prime,len(word)+1):
#         if word[index] == letter:
#             return index
#     return -1


# sammy = {'username': 'sammy-shark', 'online': 'true', 'follwers': '987'}
# print (sammy)
# print(sammy['username'])
# print(sammy['follwers'])
# print(sammy['online'])
# print(sammy.keys())
# jesse = {'username': 'JOctopus', 'online': 'False', 'points': '723'}

# for commen_key in sammy.keys() & jesse.keys():
#     print(sammy[commen_key], jesse[commen_key])
# for key, value in sammy.items():
#     print(key, 'is the key for the value', value)
# usernames = {'Sammy': 'sammy-shark', 'Jamie': 'mantisshrimp54'}

# usernames['Drew'] = 'squidly'
# usernames['Rio'] = 'candy'
# print(usernames)
# drew = {'username': 'squidly', 'online': True, 'followers': 305}
# drew['followers'] = 342
# print(drew)

# usernames = {'sammy':'sammy-shark', 'jaime': 'mantisshrimp54'}
# while True:
#     print('name:')
#     name = input()
#     if name in usernames:
#         print(usernames[name] + ' is the username of ' + name)


#     else:
#         print('I don\t have' + name + '\'s username, what is it?')   
#         username = input()
#         username[name] = username
#         print('data updated.')    

# jesse = {'username': 'JOctopus', 'online': False, 'points': 723}

# jesse.update({'followers': 481})

# print(jesse)

# bad_guys = {'daredevils': 'kingpin', 'x-men': 'apocalypse', 'batman': 'bane'}
# print(bad_guys)

# bad_guys[0]
# d = { 
#     0: 'plane',
#     1: 'train',
#     2: 'automobile'
# }
# print(d[0])
pickle.dumps 