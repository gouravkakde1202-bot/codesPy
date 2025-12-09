import random
s = random.randint(0, 100)
print("Guess 0-100.")

while True:
    try:
        g = int(input("Guess: "))
    except:
        print("Error.")
        continue
    
    if g == s:
        print("Correct!")
        break
    print("Too low." if g < s else "Too high.")