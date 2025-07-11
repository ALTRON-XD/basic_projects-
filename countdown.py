import time
user_input = int(input("enter the number of seconds for countdown : "))
while user_input!= 0:
    time.sleep(1)
    print(user_input)
    user_input=user_input-1

print("your time is over")
