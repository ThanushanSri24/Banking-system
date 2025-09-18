#Variables
Customers=[]
Count=2


while(Count>1):
    print("                        ABC Bank")
    print("                        Main Menu")
    print("1. Add  a new customer")
    print("2. View details of a customer including  bank balance")
    print("3. View details of all the customers with their bank balances")
    print("4. Deposit money to account")
    print("5. Withdraw money from account")
    print("6. Update Customer Details")
    print("7. Exit")
    choice=input("                                      Your Choice")


    
    if choice=="1":
       print("                        ABC Bank")
       print("                   Add a New Customer.")
       if len(Customers)<5:
           Account_Number= input("Enter Account Number: ")
           Nic= input("Enter NIC: ")
           First_Name= input("Enter First Name: ")
           Last_Name= input("Enter Last name: ")
           Birth_Date= input("Enter Birth date: ")
           Address= input("Enter permanent Address: ")
           Telephone_Number= input("Enter Telephone number: ")
           Balance= 0.0
           Command1=input("Do you want to save the account  (yes/no)? : ")
           if (Command1=="yes"):
               Customers.append([Account_Number,Nic,First_Name,Last_Name,Birth_Date,Address,Telephone_Number,Balance])
               print("Account oppened sucessfully!")
           else:
               print("Account opened Unsuccessful!")
       else:
           print("Maximum number of customers reached!")
           break
        
         
    elif choice=="2":
        print("                        ABC Bank")
        print("               View details of a customer")
        Account_Number = input("Enter Account Number")
        for Customer in Customers:
            if Customer[0] == Account_Number:
                print("Account Number:", Customer[0])
                print("NIC:", Customer[1])
                print("Telephone:", Customer[6])
                print("First Name:", Customer[2])
                print("Last Name:", Customer[3])
                print("Balance:", Customer[7])
                Command2=input("Do you want to view another account details (yes/No)?: ")
                if (Command2=="yes"):
                    print()
                else:
                    print("End of the details!")
                    break
                break
        else:
            print("Error can't Find Account!")
              
    elif choice=="3":
         print("                        ABC Bank")
         print("            View details of all customers")
         for Customer  in Customers:
            print("NIC: ",Customer[1])
            print("Account Number: ",Customer[0])
            print("First Name: ",Customer[2])
            print("Last Name: ",Customer[3])
            print("Balance: ",Customer[7])
         Command3=input("Do you want to update the account details (yes/No)? ")
         if(Command3=="yes"):
             Account_Number = input("Enter the Account Number: ")
             for Customer in Customers:
                 if Customer[0] == Account_Number:
                     Customer[1] = input("Enter the new NIC number: ")
                     Customer[2] = input("Enter the new First Name of customer: ")
                     Customer[3] = input("Enter the new Last Name of customer: ")
                     Customer[4] = input("Enter the new Birth Date: ")
                     Customer[5] = input("Enter the new Permanent Address: ")
                     Customer[6] = input("Enter the new Phone Number: ")
                     Command6=input(" Do you want to save the new details (Yes/No)?")
                     if(Command6=="yes"):
                         print("Customer details updated successfully.")
                     else:
                         print("End of the Details!!")
                     break
             break        
         else:
             print("End of the Details!!")       
                    
    elif choice == "4":
        print("                        ABC Bank")
        print("           Deposit Money to a given account")
        Account_Number = input("Enter Account Number: ")
        for Customer in Customers:
            if Customer[0] == Account_Number:
                Amount = float(input("Enter the amount to Deposit: "))
                Customer[7] += Amount
            Command4=input("Do you want to save (Yes/No)?")
            if(Command4=="yes"):
                print("Deposit successful. New balance:", Customer[7])
                break
            else:
                print("Deposit Unsuccessful!!")

            
    elif choice=="5":
        print("                        ABC Bank")
        print("          Withdraw money from a given account")
        Account_Number = input("Enter Account Number: ")
        for Customer in Customers:
            if Customer[0] == Account_Number:
                Amount = float(input("Enter the amount to Withdraw: "))
                if Customer[7]>=Amount:
                    Customer[7] -= Amount
                    Command6=input("Do you want to save (Yes/No)?")
                    if(Command6=="yes"):
                        print("Withdraw successful. New balance: ",Customer[7])
                    else:
                        print("Transaction was canceled")
                else:
                    print("Insufficient Balance.")
            else:
                print("Error: can't find the account")

    elif choice == "6":
        print("                        ABC Bank")
        print("                Update Customer Details")
        Account_Number = input("Enter the Account Number: ")
        for Customer in Customers:
                 if Customer[0] == Account_Number:
                     Customer[1] = input("Enter the new NIC number: ")
                     Customer[2] = input("Enter the new First Name of customer: ")
                     Customer[3] = input("Enter the new Last Name of customer: ")
                     Customer[4] = input("Enter the new Birth Date: ")
                     Customer[5] = input("Enter the new Permanent Address: ")
                     Customer[6] = input("Enter the new Phone Number: ")
                     Command6=input(" Do you want to save the new details (Yes/No)?")
                     if(Command6=="yes"):
                         print("Customer details updated successfully.")
                     else:
                         print("End of the Details!!")
                     break
                        
        else:
            print("Error  can't  Find Account")
    elif choice=="7":
        print("________________________________________________________________________________")
        print("EXIT")
        print("________________________________________________________________________________")
        break
    else:
        print("Different   Choice")

   

