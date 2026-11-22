name = "mohamed"  # store str to variable
age = 22  # store int to variable
height = 1.80  # store float
print(type(name), type(age))  # using built in functions type
# using built in function str to change the int to str
print("Hi, my age is:" + str(age))
# age = str(age)
# checking the changinng in data type from int to str using built in fun called str
print(type(age))
print(len(name))  # using math built in fun to get the lenght of str
# using the count fun to detect the times that used in the text
text = '''Mohamed is learning python.
Mohamed is the grand delmondo de la python.
Mohamed is the father of this language.
'''
# applying the fun repalce on the phone number to remove the minus numbers
print(text.count('Mohamed'))
phone = "195-15-184"
print(phone.replace("-", ""))
#python challange
number='+49 (176) 123-4567'
print(number.replace('+','00').replace(' ','').replace('(176)','176').replace('-',''))