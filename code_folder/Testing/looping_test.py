# while True:
#     try:
#         b = int(input("enter a value: "))
#         break
#     except  ValueError:
#         print("Value is not valid")

list_test = ["road", "sea"]

user_input = input("Road or Sea? ")
while user_input.lower() not in list_test:
    print("Try Again")
    user_input = input("Road or Sea")

if user_input.lower() == "road":
    print("ROADY")
elif user_input.lower() == "sea":
    print("SEASY")
