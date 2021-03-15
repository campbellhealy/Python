# key_value_swapper.py

# dict
choco = {10: "white", 20: "yellow", 30: "blue"}

# Function
dark_choco = {v: k for k, v in choco.items()}

# Output
print(choco)
print(dark_choco)
