# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13psb4qiKec4_y6NUSF-sVRP6RXqKozRf

ML Assignment-1
Divya Sai Ajay jasti
700741296
"""

ages = [19,22,19,24,20,25,26,24,25,24]

#1.1 Sort the list and find the min and max age
ages.sort() #soring the ages
min_age = min(ages) #minimum age would be the first element in sorted ages
max_age = max(ages) #maximum age would be the last element in sorted ages
print(" 1.1) min_age = " , min_age , " max_age =" , max_age)

#1.2 Add the min age and the max age again to the list
ages.append(min_age) #adding min_age
ages.append(max_age) #adding max_age
print(" 1.2) ages = ", ages)

#1.3 Find the median age (one middle item or two middle items divided by two)
mid_value = len(ages) // 2 #finding the length for list and dividing by 2
median = (ages[mid_value] + ages[~mid_value]) / 2 # using negative in list to count items from the end and get average
print(" 1.3) median age = ", median)

#1.4 Find the average age (sum of all items divided by their number)
sum = 0 #assingning value 0 to varible named sum
length = len(ages)
for i in ages: #running for loop for list
    sum = sum + i # adding every element to sum and storing the value in sum
print(" 1.4) sum = ", sum/length)

#1.5 Find the range of the ages (max minus min)
ages.sort() #soring the ages
min_age = min(ages) #minimum age would be the first element in sorted ages
max_age = max(ages) #maximum age would be the last element in sorted ages
range_ages = max_age - min_age #max age minus min age gives range
print(" 1.5) range_ages = ", range_ages)

#2.1 Create an empty dictionary called dog
dog = {} #empty dictionary
print(" 2.1) dog = ", dog)

#2.2 Add name, color, breed, legs, age to the dog dictionary
dog = {'name' : 'sweety', 'breed' : 'golden retriver', 'legs' : 4, 'age' : 3} #adding keys and values to dictionary
print(" 2.2) dog = ", dog)

#2.3 Create a student dictionary and add first_name, last_name, gender, age, 
#marital status,skills, country, city and address as keys for the dictionary
student = {
    'first_name':'divya sai ajay',
    'last_name':'jasti',
    'gender':'male',
    'age': 21,
    'country':'India',
    'skills':['Python','machine learning'],
    'maritial status':False,
    'city':'hyderabad',
    'address':{
        'door no.' : 7-4-221,
        'area':'balanagar',
        'zipcode':'500011'
    }
    }
print(" 2.3) student = ", student)

#2.4 Get the length of the student dictionary
dict_length = len(student)
print(" 2.4) dict_length = ", dict_length)

#2.5 Get the value of skills and check the data type, it should be a list
value_skills = student['skills']
print(" 2.5) value_skills = ", value_skills, type(value_skills))

#2.6 Modify the skills values by adding one or two skills
student['skills'].append('java')
print(" 2.6) student = ", student['skills'])

#2.7 Get the dictionary keys as a list
keys = student.keys()
print(" 2.7) keys = ", keys)

#2.8 Get the dictionary values as a list
values = student.values()
print(" 2.8) values = ", values)

#3.1 Create a tuple containing names of your sisters and your brothers
sisters = ('siri', 'srilekha' , 'supraja')
brothers = ('varun','goutham','siddu')
print(" 3.1) sisters = ", sisters, ", brothers = ", brothers)

#3.2 Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(" 3.2) siblings = ", siblings)

#3.3 How many siblings do you have?
siblings_count = len(siblings)
print(" 3.3) siblings_count = ", siblings_count)

#3.4 Modify the siblings tuple and add the name of your father and mother and 
# assign it to family_members
siblings = list(siblings) #converting tuple to list to Modify
siblings.append("ramesh") #adding father name
siblings.append("kavitha") #adding mother name
family_members = tuple(siblings) #coverting list into tuple again and assingning
print(" 3.4) family_members = ", family_members)

#4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#4.1 Find the length of the set it_companies
print(" 4.1) length = ", len(it_companies))

#4.2 Add 'Twitter' to it_companies
it_companies.add('twitter')
print(" 4.2) it_companies = ", it_companies)

#4.3 Insert multiple IT companies at once to the set it_companies
s = {'cvs','mondo','infotech','cyient'}
it_companies.update(s)
print(" 4.3) it_companies = ", it_companies)

#4.4 Remove one of the companies from the set it_companies
it_companies.remove('Apple')
print(" 4.4) it_companies = ", it_companies)

#4.5 What is the difference between remove and discard
print(" 4.5) discard keyword does'nt give error even if the entered element does'nt exist in the list, but remove keyword give error in that case.")

#4.6 Join A and B
print(" 4.6) A Union B        = ", A.union(B))

#4.7 Find A intersection B
print(" 4.7) A intersection B = ", A.intersection(B))

#4.8 Is A subset of B
print(" 4.8) Is A subset of B ? ", A.issubset(B))

#4.9 Are A and B disjoint sets
print(" 4.9) A and B disjoint ? ", A.isdisjoint(B))

#4.10 Join A with B and B with A
print(" 4.10) A U B = ", A.union(B), ", B U A = ", B.union(A) )

#4.11 What is the symmetric difference between A and B
print(" 4.11) A symmetric difference B = ", A.symmetric_difference(B))

#4.12 Delete the sets completely
A.clear()
B.clear()
print( " 4.12) A = ", A, ", B = ", B)

#4.13 Convert the ages to a set and compare the length of the list and the set.
list_length = len(age)
age = set(age)
set_length = len(age)
print(" 4.13) list_length = ", list_length, ", set_length = ", set_length)

#5.1 Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
radius = 30
pi = 3.141592653589793238
_area_of_circle_ = pi*radius*radius
print(" 5.1) area of circle = ", _area_of_circle_)

#5.2 Calculate the circumference of a circle and assign the value to a variable name of
#_circum_of_circle_
_circum_of_circle_ = 2*pi*radius
print(" 5.2) _circum_of_circle_ = ", _circum_of_circle_)

#5.3 Take radius as user input and calculate the area
r = int(input("enter radius: "))
print(" 5.3) area = ", pi*r*r)

#6 How many unique words have been used in the sentence? Use the split methods and set
#to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people" #given sentence
ans = set(sentence.split(" ")) #splitting the given sentence where there is a space and adding them to set(sets does not have duplicate values so every value is unique).
print(" 6) unique words = ", len(ans))

#7 Use a tab escape sequence
print("Name\tAge\tCountry\tCity\nAsabench\t250\tFinland\tHelsinki")

#8 Use the string formatting method to display
radius = 10
area = 3.14*radius**2
print("radius = {radius}".format(radius = 10))
print("area = {pi}*radius**2".format(pi = 3.14))

#using string formatting method(format) to insert numerical values between string

answer="The area of the circle with radius {0} is {1} meters square".format(radius,area)
print(answer)

#9 Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
#kilograms in a separate list using Loop. N: No of students (Read input from user)

n = int(input(" Enter no. of students: "))
weights_lbs = [] #empty list
weights_kg = [] #empty lilst
lbs = 0.453592
for i in range(n): #using for loop
    w = int(input(" Enter weight in lbs: ")) #taking input
    weights_lbs.append(w) #adding input weights to list 
for i in weights_lbs: # for every value in list
    j = i*lbs #multiplying every value in list with lbs to convert it into kg
    weights_kg.append(j) # adding new values to empty list
print(weights_kg)