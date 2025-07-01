choice = int(input("enter your choice from 1-7 : \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.sqrt\n7.squre\n enter the input :")) #taking input from user

if choice == 6: # sqrt
    num = int(input("enter the number : ")) # taking input from user
    print("the sqrt of", num, "is", num**0.5)

else:
    num1 = int(input("enter the 1st number : ")) # taking input from user
    num2 = int(input("enter the 2nd number : ")) # taking input from user
    if choice == 1: # addition
        print("the addition of", num1,  "and", num2, "is", num1 + num2)
    elif choice == 2: # subtraction
        print("the Subtraction of", num1,  "and", num2, "is", num1 - num2)
    elif choice == 3: # multiplication
        print("the Multiplication of", num1,  "and", num2, "is", num1 * num2)
    elif choice == 4: # division
        print("the Division of", num1,  "and", num2, "is", num1 / num2)
    elif choice == 5: # modulus
        print("the Modulus of", num1, "and", num2, "is", num1 % num2)
    elif choice == 7: # squre
        print("the squre of", num1,  "and", num2, "is", num1**num2)
    else: # invalid choice
        print("enter a valid choice")
