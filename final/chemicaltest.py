# Prompt the user to identify their pool as either a chlorine or bromine pool
pool_type = input("Is your pool a chlorine pool or a bromine pool? ")

# Test for chlorine in the pool
if pool_type == "chlorine":
  print("Perform the Free, Combined, and Total Chlorine test:")
  print("1. Rinse and fill small comparator tube to 9mL mark with water to be tested.")
  print("2. Add 5 drops R-0001 and 5 drop R-0002. Cap and invert to mix.")
  print("3. Match color with color standard*. Record as parts per million (ppm) free chlorine.")
  print("4. Add 5 drops R-0003. Cap and invert to mix.")
  print("5. Match color immediately. Record as ppm total chlorine.")
  print("6. Subtract free chlorine (FC) from total chlorine (TC). Record as ppm combined chlorine (CC). Formula: TC - FC = CC.")
  input("Press Enter to continue...")

# Test for bromine in the pool
elif pool_type == "bromine":
  print("Perform the Total Bromine test:")
  print("1. Rinse and fill small comparator tube to 9 ml mark with water to be tested.")
  print("2. Add 5 drops R-0001 and 5 drops R-0002. Cap and invert to mix.")
  print("3. Match color with color standard*. Record as parts per million (ppm) total bromine (TB).")
  print("*If color is off-scale: Repeat test using 4.5 mL sample diluted to 9mL mark with tap water. Multiply reading by 2 to obtain approximate sanitizer level.")
  print("If color is still off-scale: Repeat test using 1.8mL sample diluted to 9mL mark with tap water. Multiply reading by 5 to obtain approximate sanitizer level.")
  input("Press Enter to continue...")

# If the user did not input "chlorine" or "bromine"
else:
  print("Please enter either 'chlorine' or 'bromine'.")

# Test the pH of the pool
print("Perform the pH test:")
print("1. Rinse and fill large comparator tube to 44 mL mark with water to be tested.")
print("2. Add 5 drops R-0004. Cap and invert to mix.")
print("3. Match color with color standard. Record as pH units and save sample if pH needs adjustment. If sample color is between two values, pH is average of the two.")
print("To LOWER pH: See Acid Demand Test. To RAISE pH: See Base Demand Test.")
input("Press Enter to continue...")

# Test for acid demand in the pool
print("IF required, perform the Acid Demand test:")
print("1. Use treated sample from pH test.")
print("2. Add R-0005 dropwise. After each drop, count, cap and invert to mix, and compare with color standards until desired pH is matched. See Treatment Tables to continue.")
input("Press Enter to continue...")

# Test for base demand in the pool
print("If required, perform the Base Demand test:")
print("1. Use treated sample from pH test.")
print("2. Add R-0006 dropwise. After each drop, count, cap and invert to mix, and compare with color standards until desired pH is matched. See Treatment Tables to continue.")
input("Press Enter to continue...")

# Test for total alkalinity in the pool
print("Perform the Total Alkalinity (TA) test:")
print("1. Rinse and fill large comparator tube to 25 mL mark with water to be tested*.")
print("2. Add 2 drops R-0007. Swirl to mix.")
print("3. Add 5 drops R-0008. Swirl to mix. Sample will turn green.")
print("4. Add R-0009 dropwise, swirling and counting after each drop, until color changes from green to red.")
print("5. Multiply drops in step 4 by 10. Record as parts per million (ppm) total alkalinity.")
print("*When high TA is anticipated: Use 10mL sample, 1 drop R-0007, 3 drops R-0008, and multiply drops in step 4 by 25.")
input("Press Enter to continue...")

# Test for calcium hardness in the pool
print("Perform the Calcium Hardness (CH) test:")
print("1. Rinse and fill large comparator tube to 25 mL mark with water to be tested*.")
print("2. Add 20 drops R-0010. Swirl to mix.")
print("3. Add 5 drops R-0011L. Swirl to mix. If calcium hardness is present, sample will turn red.")
print("4. Add R-0012 dropwise, swirling and counting after each drop, until color changes from red to blue.")
print("5. Multiply drops in step 4 by 10. Record as parts per million (ppm) calcium hardness.")
print("*When high CH is anticipated: Use 10 mL sample, 10 drops R-0010, 3 drops R-0011L, and multiply drops in Step 4 by 25.")
input("Press Enter to continue...")

# Test for cyanuric acid in the pool
print("Perform the Cyanuric Acid (CYA) test:")
print("1. Rinse and fill bottle (#9191) to 7 mL mark with water to be tested.")
print("2. Add R-0013 to 14 mL mark. Cap and mix vigorously for 30 seconds.")
print("3. Slowly transfer cloudy solution to small comparator tube until black dot on bottom just disappears when viewed from top.")
print("4. Read tube at liquid level on back of comparator block. Record reading as parts per million (ppm) cyanuric acid (CYA).")
input("Press Enter to continue...")

# Test for sodium chloride (salt) in the pool
print("Perform the Sodium Chloride (Salt) Test:")
input("Press Enter to continue...")
print("For 1 drop = 200 ppm")
print("1. Rinse and fill sample tube (#9198) to 10 mL mark with water to be tested.")
print("2. Add 1 drop R-0630. Swirl to mix. Sample will turn yellow.")
print("3. Add R-0718 dropwise, swirling and counting after each drop, until color changes from yellow to a milky salmon (brick red).")
print("NOTE: A white precipitate will form as R-0718 Silver Nitrate Reagent is added to the sample. Do not add enough R-0718 Silver Nitrate Reagent to give a brown color. First change from yellow to a milky salmon (brick red) is the endpoint.")
print("4. Multiply drops of R-0718 by 200. Record as parts per million (ppm) salt (sodium chloride).")
input("Press Enter to end program.")


