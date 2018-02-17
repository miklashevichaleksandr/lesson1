#weather1 = {"city": "Москва", "temperature": 23, "wind": "южный"}
#weather2 = {"city": "Москва", "temperature": 20, "wind": "восточный"}
#weather3 = {"city": "Москва", "temperature": 22, "wind": "западный"}
#peopleweather = {"Sasha": weather1, "Masha": weather2, "Petya": weather3}
#username = input("Enter your username: ")
#print('User ' + username + ' live in city ' + peopleweather[username]["city"] + ' where temperature is ' + str(peopleweather[username]["temperature"]) + ' and wind is ' + peopleweather[username]["wind"])

names = ['Оля', 'Петя', 'Вася', 'Маша']

names2=names

names2.append('Настя')

print(names2)

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}

#print(is_male['Оля'])

for i in names:
	print(i + ', число букв ' + str(len(i)) + ', пол ' + str(is_male[i]))

c='\n'.join(names)
d=''.join(names)
print(c)


#groups = [
#  ['Вася', 'Маша'],
#  ['Оля', 'Петя', 'Гриша'],
#]



