is_morning_selected = False
is_snack_selected = False
is_afternoon_selected = False
is_evening_selected = False


morning_activity = ""
snack_choice = ""
afternoon_activity = ""
evening_idea = ""


def morning_options():
   print("\nChoose a morning activity:")
   print("1: Stretch and do yoga")
   print("2: Swim at the pool")
   print("3: Take a stroll in your neighborhood")


def snack_options():
   print("\nChoose a summer snack:")
   print("1: Watermelon")
   print("2: Popsicles")
   print("3: Starbucks refresher")


def afternoon_options():
   print("\nChoose an afternoon activity:")
   print("1: Go biking")
   print("2: Have a picnic")
   print("3: Watch a movie")


def evening_options():
   print("\nChoose an evening idea:")
   print("1: Watch the sunset")
   print("2: Do a bonfire")
   print("3: Go skygazing")


def pick_morning(option):
   global is_morning_selected
   global morning_activity


   if option == 1:
       morning_activity = "Stretch and do yoga"
   elif option == 2:
       morning_activity = "Swim at the pool"
   elif option == 3:
       morning_activity = "Take a stroll in your neighborhood"
   else:
       print("Please pick an option that is given.")
       return
   is_morning_selected = True
   print("Awesome! Your morning activity is: " + morning_activity)


def pick_snack(option):
   global is_snack_selected
   global snack_choice


   if option == 1:
       snack_choice = "Watermelon"
   elif option == 2:
       snack_choice = "Popsicles"
   elif option == 3:
       snack_choice = "Starbucks refresher"
   else:
       print("Please pick an option that is given.")
       return
   is_snack_selected = True
   print("That sounds yummy! You chose to eat: " + snack_choice)


def pick_afternoon(option):
   global is_afternoon_selected
   global afternoon_activity


   if option == 1:
       afternoon_activity = "Go biking"
   elif option == 2:
       afternoon_activity = "Have a picnic"
   elif option == 3:
       afternoon_activity = "Watch a movie"
   else:
       print("Please pick an option that is given.")
       return
   is_afternoon_selected = True
   print("Sounds fun! Your afternoon activity is: " + afternoon_activity)


def pick_evening(option):
   global is_evening_selected
   global evening_idea


   if option == 1:
       evening_idea = "Watch the sunset"
   elif option == 2:
       evening_idea = "Do a bonfire"
   elif option == 3:
       evening_idea = "Go skygazing"
   else:
       print("Please pick an option that is given.")
       return
   is_evening_selected = True
   print("Nice! Your evening idea is: " + evening_idea)


while is_morning_selected == False:
   morning_options()
   try:
       user_input = int(input("Enter your selection (1-3): "))
       pick_morning(user_input)
   except ValueError:
       print("Please enter a number (1, 2, or 3).")


while is_snack_selected == False:
   snack_options()
   try:
       user_input = int(input("Enter your selection (1-3): "))
       pick_snack(user_input)
   except ValueError:
       print("Please enter a number (1, 2, or 3).")


while is_afternoon_selected == False:
   afternoon_options()
   try:
       user_input = int(input("Enter your selection (1-3): "))
       pick_afternoon(user_input)
   except ValueError:
       print("Please enter a number (1, 2, or 3).")


while is_evening_selected == False:
   evening_options()
   try:
       user_input = int(input("Enter your selection (1-3): "))
       pick_evening(user_input)
   except ValueError:
       print("Please enter a number (1, 2, or 3).")


print("\n🎀 𝓗𝓮𝓻𝓮 𝓲𝓼 𝔂𝓸𝓾𝓻 𝓹𝓮𝓻𝓯𝓮𝓬𝓽 𝓼𝓾𝓶𝓶𝓮𝓻 𝓭𝓪𝔂 𝓹𝓵𝓪𝓷!🌴")
print("\n Morning: " + morning_activity)
print("\n Snack: " + snack_choice)
print("\n Afternoon: " + afternoon_activity)
print("\n Evening: " + evening_idea)

