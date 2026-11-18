intro_decoration = "=" * 50
middel_decoration = "-" * 50
print(intro_decoration,
      "\nLOBAL EXPRESS LOGISTICS  |  AUTOMATED WAYBILL SYSTEM v1.0\n", intro_decoration)
sender_name = input('Enter sender name :\n')
countery_shiping = input('Enter sender countery :\n')
sender_company = input('Enter sender company ;\n')
receiver_name = input('Enter reciver name :\n')
receiver_countery = input('Enter reciver countery :\n')
description = input('Enter the description of the package ;\n')
weight = input("Enter the weight of the package in kg ;\n")
note = input('Enter any handeling note\n')
print(intro_decoration,
      "\nLOBAL EXPRESS LOGISTICS  |  AUTOMATED WAYBILL SYSTEM v1.0\n", intro_decoration)
# using end= to avoid new line and making the next print statment in the same line in output but another line in the code
print('Tracking Code :\t\t', countery_shiping, end='')
print("", receiver_countery, "8492", "EXP", sep="-")
print(middel_decoration, "\n")
print('[1] SENDER DETAILS\n')
print('Name:\t\t', sender_name, "\nCompany;\t",
      sender_company, "\nCountery:\t", countery_shiping)
print(middel_decoration, "\n")
print('[2] RECEIVER DETAILS\n')
print('Name:\t\t', receiver_name, "\nCountery:\t", receiver_countery)
print(middel_decoration, "\n")
print('[3] PACKAGE DETAILS\n')
print('Description:\t\t', description, "\nWeight:\t\t",
      weight, "kg\nHandling Note:\t", '"', note, '"', sep='')
print(middel_decoration, "\n")
