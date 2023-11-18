print("The Love Calculator is calculating yourt score...")
name1 = input("What is your name?")
name2 = input("What is there name?")

name1lower = name1.lower()
name2lower = name2.lower()
# true counter
truecounterT = name1lower.count("t")
truecounterR = name1lower.count("r")
truecounterU = name1lower.count("u")
truecounterE = name1lower.count("e")

truecounterT2 = name2lower.count("t")
truecounterR2 = name2lower.count("r")
truecounterU2 = name2lower.count("u")
truecounterE2 = name2lower.count("e")

truetotal = truecounterT + truecounterR + truecounterU + truecounterE + truecounterT2 + truecounterR2 + truecounterU2 + truecounterE2

# love counter
lovecounterL = name1lower.count("l")
lovecounterO = name1lower.count("o")
lovecounterV = name1lower.count("v")
lovecounterE = name1lower.count("e")

lovecounterL2 = name2lower.count("l")
lovecounterO2 = name2lower.count("o")
lovecounterV2 = name2lower.count("v")
lovecounterE2 = name2lower.count("e")

lovetotal = lovecounterL + lovecounterO + lovecounterV + lovecounterE + lovecounterL2 + lovecounterO2 + lovecounterV2 + lovecounterE2

lovescore = int(str(truetotal) + str(lovetotal))

if lovescore < 10 or lovescore > 90:
  print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore >= 40 and lovescore <= 50:
  print(f"Your score is {lovescore}, you are alright together.")
else:
  print(f"Your score is {lovescore}.")
