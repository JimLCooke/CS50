# Start of script

# First, let's make sure the pool cover is removed
cover_removed = False
while not cover_removed:
  response = input("Have you removed the pool cover? (y/n) ")
  if response.lower() == "y":
    print("Great! Make sure to fan-fold the cover together for easier storage and consider enlisting a friend to help.")
    cover_removed = True
  elif response.lower() == "n":
    print("Please remove the pool cover before continuing. Remember to fan-fold the cover together for easier storage and consider enlisting a friend to help.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Next, let's make sure the cover anchors are in place
anchors_in_place = False
while not anchors_in_place:
  response = input("Have you put down the cover anchors in the deck to protect your toes and prevent tripping? (y/n) ")
  if response.lower() == "y":
    print("Great! Remember to use an impact gun to secure the anchors in place.")
    anchors_in_place = True
  elif response.lower() == "n":
    print("Please put down the cover anchors in the deck before continuing. Remember to use an impact gun to make quick work of putting them down, but do not impact them into the deck. Rather, use the impact gun to free stubborn anchors, and then gently lower them until completely flush with deck.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Now let's make sure the pool is full
pool_full = False
while not pool_full:
  response = input("Is the pool full to halfway up the skimmers? (y/n) ")
  if response.lower() == "y":
    print("Great! Let's move on to setting up the pool system.")
    pool_full = True
  elif response.lower() == "n":
    print("Please fill the pool before continuing. Make sure the water level is at least halfway up the skimmers.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Let's make sure the pump is ready
pump_ready = False
while not pump_ready:
  response = input("Is the pump hooked up to pipes, not seized, primed, and has the lid on tight? (y/n) ")
  if response.lower() == "y":
    print("Great! Make sure the drain plugs are in and the pump is ready to run.")
    pump_ready = True
  elif response.lower() == "n":
    print("Please make sure the pump is hooked up to pipes, not seized, primed, and has the lid on tight before continuing.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Let's make sure the filter is properly assembled
filter_ready = False
while not filter_ready:
  response = input("Is the filter properly assembled and the filter drain cap tight? (y/n) ")
  if response.lower() == "y":
    print("Great! Let's move on to checking the heater.")
    filter_ready = True
  elif response.lower() == "n":
    print("Please make sure the filter is properly assembled and the filter drain cap is tight before continuing.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Let's check the heater
heater_ready = False
while not heater_ready:
  response = input("Are the heater drain plugs and safety items in place and are you comfortable starting the heater? (y/n) ")
  if response.lower() == "y":
    print("Great! You can start the heater if you wish, but be careful as it is the leading cause of pool technician deaths most years. If you are not comfortable starting the heater, you may choose to leave it off.")
    heater_ready = True
  elif response.lower() == "n":
    print("Please make sure the heater drain plugs and safety items are in place and you are comfortable starting the heater before continuing. If you are not comfortable starting the heater, you may choose to leave it off.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Let's set up the pool system
system_ready = False
while not system_ready:
  response = input("Is the pool system ready to be set up? (y/n) ")
  if response.lower() == "y":
    print("Great! Set the pump timers to run 24/7 until the summerization process is complete, but make sure to leave the power off for now.")
    system_ready = True
  elif response.lower() == "n":
    print("Please make sure the pool system is ready to be set up before continuing. Set the pump timers to run 24/7 until the summerization process is complete, but make sure to leave the power off for now.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Let's remove the plugs from the returns, skimmers, and water features
plugs_removed = False
while not plugs_removed:
  response = input("Have you removed the plugs from the returns, skimmers, and water features? (y/n) ")
  if response.lower() == "y":
    print("Great! Let's move on to setting up the in-floor water cleaner system if equipped.")
    plugs_removed = True
  elif response.lower() == "n":
    print("Please remove the plugs from the returns, skimmers, and water features before continuing.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Let's set up the in-floor water cleaner system if equipped
cleaner_system_ready = False
while not cleaner_system_ready:
  response = input("Have you set up the in-floor water cleaner system by removing the plugs and assembling the cleaner unit? (y/n) ")
  if response.lower() == "y":
    print("Great! Let's move on to checking the valves.")
    cleaner_system_ready = True
  elif response.lower() == "n":
    print("Please set up the in-floor water cleaner system by removing the plugs and assembling the cleaner unit before continuing.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Let's check the valves
valves_ready = False
while not valves_ready:
  response = input("Are the valves ready to be turned on? (y/n) ")
  if response.lower() == "y":
    print("Great! Let's turn on the power and see if the system primes and does not leak.")
    valves_ready = True
  elif response.lower() == "n":
    print("Please make sure the valves are ready to be turned on before continuing.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Let's turn on the power and see if the system primes and does not leak
power_on = False
while not power_on:
  response = input("Has the power been turned on and is the system priming and not leaking? (y/n) ")
  if response.lower() == "y":
    print("Great! Let's shock the pool hard with triple the amount as normal and brush the pool thoroughly, attempting to brush every square inch with an appropriate brush.")
    power_on = True
  elif response.lower() == "n":
    print("Please make sure the power is on and the system is priming and not leaking before continuing. Shock the pool hard with triple the amount as normal and brush the pool thoroughly, attempting to brush every square inch with an appropriate brush.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# Let's backwash or clean the filter once per day for 3 days or until clear
filter_cleared = False
while not filter_cleared:
  response = input("Has the pool cleared after backwashing or cleaning the filter once per day for 3 days or until clear? (y/n) ")
  if response.lower() == "y":
    print("Great! Let's balance the pool, execute your weekly maintenance protocol, and enjoy your swims.")
    filter_cleared = True
  elif response.lower() == "n":
    print("If the pool is still cloudy or green, use another triple dose of shock, brush thoroughly again, and continue backwashing/cleaning once per day. Once the pool clears, balance the pool, execute your weekly maintenance protocol, and enjoy your swims.")
  else:
    print("Sorry, I didn't understand your response. Please enter 'y' for yes or 'n' for no.")

# End of script
