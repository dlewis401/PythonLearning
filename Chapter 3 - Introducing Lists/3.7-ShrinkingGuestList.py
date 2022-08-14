dinnerList = ['Rex', 'Marley', 'Joey', 'Alex']

print(f"Hello, {dinnerList[0]}. You are invited to Dinner! Your code is #1")
print(f"Hello, {dinnerList[1]}. You are invited to Dinner! Your code is #2")
print(f"Hello, {dinnerList[2]}. You are invited to Dinner! Your code is #3")
print(f"Hello, {dinnerList[3]}. You are invited to Dinner! Your code is #4")

print("\n")

print("Wow! Looks like I got more space for friends! Your number might be changed as a result.")

print("\n")

Steve = dinnerList.insert(0, "Steve")
Person = dinnerList.insert(3, "Micheal")
Ian = dinnerList.append('Ian')

print(f"Hello, {dinnerList[0]}. You are invited to Dinner! Your code is #1")
print(f"Hello, {dinnerList[1]}. You are invited to Dinner! Your code is #2")
print(f"Hello, {dinnerList[2]}. You are invited to Dinner! Your code is #3")
print(f"Hello, {dinnerList[3]}. You are invited to Dinner! Your code is #4")
print(f"Hello, {dinnerList[4]}. You are invited to Dinner! Your code is #5")
print(f"Hello, {dinnerList[5]}. You are invited to Dinner! Your code is #6")
print(f"Hello, {dinnerList[6]}. You are invited to Dinner! Your code is #7")

## CHALLENGE 3.7 START!
##

print("\n")

print("Sorry! I can only invite 2 guests!!")


Steve = dinnerList.pop(0)
print(f"Sorry, {Steve}. You cannot be invited.")
Marley = dinnerList.pop(1)
print(f"Sorry, {Marley}. You cannot be invited.")
Micheal = dinnerList.pop(1)
print(f"Sorry, {Micheal}. You cannot be invited.")
Joey = dinnerList.pop(1)
print(f"Sorry, {Joey}. You cannot be invited.")
Ian = dinnerList.pop(-1)
print(f"Sorry, {Ian}. You cannot be invited.")


print(f"Hello! {dinnerList[0]}. I can invite you to dinner!!")
print(f"Hello! {dinnerList[1]}. I can invite you to dinner!!")

del dinnerList[0]
del dinnerList[-1]

print(f"The dinner list is here: {dinnerList}")