# Initialize variables
pressure_holds = False
pump_on_loss = 0
pump_off_loss = 0
line_loses_pressure = False
suspected_pressure_side_leak = False
suspected_suction_side_leak = False
plugs_leaking = False
suction_side_pipe_sections = ['Skimmer lines', 'Vacuum line', 'Air bubbler lines', 'Venturi Chemical Feeder Systems', 'Main drains', 'Side suction units']
pressure_side_pipe_sections = ['Return lines', 'Auto cleaner lines', 'In-floor cleaner lines', 'Waterfall lines', 'Slide lines', 'Sprinkler lines']


print(r"""
| $$$$$$$                     /$$       /$$                           /$$             /$$$$$$$$                    /$$
| $$__  $$                   | $$      | $$                          | $$            |__  $$__/                   | $$
| $$  \ $$ /$$$$$$   /$$$$$$ | $$      | $$        /$$$$$$   /$$$$$$ | $$   /$$         | $$  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$
| $$$$$$$//$$__  $$ /$$__  $$| $$      | $$       /$$__  $$ |____  $$| $$  /$$/         | $$ /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$
| $$____/| $$  \ $$| $$  \ $$| $$      | $$      | $$$$$$$$  /$$$$$$$| $$$$$$/          | $$| $$$$$$$$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/
| $$     | $$  | $$| $$  | $$| $$      | $$      | $$_____/ /$$__  $$| $$_  $$          | $$| $$_____/ \____  $$  | $$ /$$| $$_____/| $$
| $$     |  $$$$$$/|  $$$$$$/| $$      | $$$$$$$$|  $$$$$$$|  $$$$$$$| $$ \  $$         | $$|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$
|__/      \______/  \______/ |__/      |________/ \_______/ \_______/|__/  \__/         |__/ \_______/|_______/    \___/   \_______/|__/

                """)



print("We understand, when your swimming pool has a leak, it can keep you up at night.")
print("That's why we made this program; to help you reason through fixing them.")
print("")
print("")
print("")


# Prompt the user to input the approximate square footage of the pool water
while True:
    try:
        square_footage_of_pool_surface = float(input("Please enter the approximate square footage of the pool water (16ft x 32ft rectangle pool = 512): "))
        if square_footage_of_pool_surface > 0:
            break
        else:
            print("Invalid input. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a positive number.")

# Prompt the user to input whether there is air in the pump when running or air/dirt blown back into the pool
while True:
    air_in_pump = input("Is there air in the pump when running or air/dirt blown back into the pool? (yes/no) ").lower()
    if air_in_pump == "yes":
        break
    elif air_in_pump == "no":
        break
    else:
        print("Invalid input. Please enter either 'yes' or 'no'.")

# If the user answered "yes" to whether there is air in the pump
if air_in_pump == "yes":
    # Prompt the user to input whether there is a blockage in a suction line
    while True:
        blockage_in_suction_line = input("Is there a blockage in a suction line? (yes/no) ").lower()
        if blockage_in_suction_line == "yes":
            # Print a message indicating that the blockage should be cleared and the program restarted
            print("Please clear the blockage and restart the program.")
            quit()
        elif blockage_in_suction_line == "no":
            # Print a message indicating that a suspected pressure side leak is present and instruct the user to perform the bucket test to confirm if leak exists
            print("There is a suspected pressure side leak. Please perform the bucket test to confirm if a leak exists.")
            suspected_pressure_side_leak = True
            break
        else:
            print("Invalid input. Please enter either 'yes' or 'no'.")
            # If the user answered "no" to the question about air in the pump
if air_in_pump == "no" or blockage_in_suction_line == "no":
    # Print a message instructing the user to perform the bucket test to determine if a leak is present
    print("Please perform the bucket test to determine if a leak is present. After 24 hours, check the water loss in the pool and the bucket.")
    print("Please perform the following bucket test to determine if a leak is present:")
    print("1. Fill the pool to the normal level.")
    print("2. Fill a bucket and place it in the pool, tied to something with rope if there is no good spot on the stairs.")
    print("3. Mark the level in the pool and bucket.")
    print("4. Operate the pool normally, as when the leak was reported.")
    print("5. Measure the water loss in the bucket and pool after 24 hours.")

    # Prompt the user to input the water loss in the pool and the bucket after 24 hours
    while True:
        try:
            pool_loss = float(input("Please enter the water loss in the pool after 24 hours: "))
            bucket_loss = float(input("Please enter the water loss in the bucket after 24 hours: "))
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")

    # If the water level in the pool has decreased more than the water level in the bucket, there is likely a leak present
if  pool_loss > bucket_loss:
    gallons_per_day = (float(pool_loss) - float(bucket_loss)) * 0.62 * float(square_footage_of_pool_surface)
    print(f"There is a leak... The pool is leaking {gallons_per_day:.2f} gallons per day. Please perform Pump on/off test to determine where the leak likely is.")
if pool_loss < bucket_loss:
    print ("The bucket data is invalid. Check for pranksters or young kids messing with the data and retry program!")
    quit()
if pool_loss == bucket_loss:
    print("There is no leak! Enjoy your swims! You might be losing water to evaporation. Try turning down your heater at night or when the pool is not in use to limit evaporative cooling")
    quit()
        # Measure the water loss with the pump off and with the pump on to determine if the leak is on the suction or pressure side
pump_off_loss = input("Please measure in inches the water loss with the pump off for 24 hours and enter the result here: ")
pump_on_loss = input("Please measure in inches the water loss with the pump on and enter the result here: ")

        # If the water loss is greater with the pump off, suspect a suction side leak
if pump_off_loss > pump_on_loss:
    suspected_suction_side_leak = True
    print ("There is likely a suction side leak.")
        # If the water loss is greater with the pump on, suspect a pressure side leak
elif pump_on_loss > pump_off_loss:
    suspected_pressure_side_leak = True
    print ("There is likely a pressure side leak.")
        # If the water loss is the same with the pump off and on, suspect a broader plumbing problem
else:
    print()
    print()
    print()
    print("Although your lines are probably good because they are uneffected by the pump,")
    print("you should still hire a pool company and scuba diver to check the tile lines,")
    print("skimmer bonds to the pool, skimmer throats, equalizers, lights (including but not")
    print("limited to, conduits, grounding screws, niche bonds to the pool, ect.), pipe")
    print("openings into the pool, cracks, vinyl liners, stairs, ladder fittings, main drains,")
    print("hydrostatic valves, or the ever-dreaded automatic cleaning system.")
    print("Sorry for the bad luck.")
    quit()
# If there is a suspected suction side leak
if suspected_suction_side_leak:
    # Define a list of suction side pipe sections
    suction_side_pipe_sections = ['Skimmer lines', 'Vacuum line', 'Air bubbler lines', 'Venturi Chemical Feeder Systems,', 'Main drains', 'Side suction units']
    # Define a list of valid responses
    valid_responses = ['yes', 'no']
    # Iterate over suction side pipe sections
    for pipe_section in suction_side_pipe_sections:
        # Validate user input for line holding pressure
        while True:
            pressure_holds = input(f"Does the {pipe_section} pipe section hold pressure for 2 minutes when tested with 20 psi of water pressure? (yes/no)").lower()
            if pressure_holds in valid_responses:
                break
            else:
                print("Please enter 'yes' or 'no'.")
        # Check if pressure test kit plugs are leaking when tested with dye kit
        if pressure_holds == "no":
            plugs_leaking = input("Please check the pressure test kit plugs for leaks with the dye kit. Are they leaking? (yes/no) ").lower()
            # If the test kit plugs are not leaking, congratulate the user on finding the leak and print which pipe section should be repaired before quitting the program
            if plugs_leaking == "no":
                print("Congratulations! You have found the leak in the previous pipe section. Please repair the pipe section and restart the program.")
                quit()
            # If the test kit plugs are leaking, tell the user to replace and tigten them, and then restart the program
            elif plugs_leaking == "yes":
                print("Please replace and tighten the pressure test kit plugs and restart the program.")
                quit()
    # If all suction side pipe sections are holding pressure, print a message indicating that the user may need help from a pool company
    print("It seems that you might need some help from a pool company, because this seem logically impossible. Please call renovation experts to help find your leak.")


# If there is a suspected pressure side leak
if suspected_pressure_side_leak:
    # Define a list of pressure side pipe sections
    pressure_side_pipe_sections = ['Return lines', 'Auto cleaner lines', 'In-floor cleaner lines', 'Waterfall lines', 'Spa jet lines', 'Misc. Water features']
    # Define a list of valid responses
    valid_responses = ['yes', 'no']
    # Iterate over pressure side pipe sections
    for pipe_section in pressure_side_pipe_sections:
        # Validate user input for line holding pressure
        while True:
            pressure_holds = input(f"Does the {pipe_section} pipe section hold pressure for 2 minutes when tested with 20 psi of water pressure? (yes/no)").lower()
            if pressure_holds in valid_responses:
                break
            else:
                print("Please enter 'yes' or 'no'.")
        # Check if pressure test kit plugs are leaking when tested with dye kit
        if pressure_holds == "no":
            plugs_leaking = input("Please check the pressure test kit plugs for leaks with the dye kit. Are they leaking? (yes/no) ").lower()
            # If the test kit plugs are not leaking, congratulate the user on finding the leak and print which pipe section should be repaired before quitting the program
            if plugs_leaking == "no":
                print("Congratulations! You have found the leak in the previous pipe section. Please repair the pipe section and restart the program to make sure you found all the leaks!")
                quit()
            # If the test kit plugs are leaking, tell the user to replace and tigten them, and then restart the program
            elif plugs_leaking == "yes":
                print("Please replace and tighten the pressure test kit plugs and restart the program.")
                quit()
    # If all pressure side pipe sections are holding pressure, print a message indicating that the user may need help from a pool company
    print("It seems that you might need some help from a pool company, because this seem logically impossible. Please call renovation experts to help find your leak.")
    quit()