# contain variables, operations, functions, and modifiers to format the value
price = 59
txt = f"The price is {price} dollars"
print(txt)


# modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals.
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


#Perform a math operation in the placeholde
txt = f"The price is {22 * 59} dollars"
print(txt)