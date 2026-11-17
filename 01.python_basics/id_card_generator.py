# this program is designed to generate an id card from the user input and save it as an image file

top_line_decoration = "="*50  # top line separator
bottom_line_decoration = "-" * 50  # boottom line separator
# wellcome message
github_address = "https://github.com/"
print(top_line_decoration, '\n\tTECH CONFERANCE 2026 PASS\n', top_line_decoration)
name = input("Enter your Name :")  # getting user input for name
track = input('Enter your Track :')  # getting user input for track
city = input('Enter your City :')  # getting user input for city
# getting user input for github username
github_username = input('Enter your Github username :')
# getting user input for favorite quote
quote = input('Enter your favorite quote :')

print('Name ;\t\t', name, '\nTrack :\t\t', track, '\nCity :\t\t',
      # printing the user input in a formatted way
      city, '\nGithub :\t', github_address, github_username, '\nQuote :\t\t', '"', quote, '"', sep='')
print("Saved at ;\t\tC:\\Users\\passes\\ticket.txt")
print(bottom_line_decoration)  # printing the bottom line separator
# printiong the confirmation message with the user name
print("Status: Confirmied! Welcome to the event!", name,'\n\n')
