text = 'hi'
number = 5
# doing a nasted function to define the data type of the variable
print(type(text))
print(type(number))
print(len(text))  # using nasted fun to get the len for the variable text
# using upper method in syntax value.method() that is used to make operation on classes like str
print(text.upper())
# using bit_lenght inorder to deal with the int class
print(number.bit_length())
# data type challange
age = 22  # store int
height = 1.80  # store float
name = 'mohamed adel'  # store str
student = True  # store bool
nothing = ''  # store nothing
# printing lines
print(age)
print(height)
print(name)
print(student)
print(nothing)
# printing data_types
print(type(age), type(height), type(name), type(student), type(nothing))
# printing lenghts
print(len(name), age.bit_length(), student.bit_length(), len(nothing))
