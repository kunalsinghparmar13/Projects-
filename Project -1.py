# Project 1 – Expense Tracker

# Question / Problem Statement: Create a console-based Expense Tracker 
# program in Python that allows the user to record daily expenses and view 
# summaries like total spending. 

# You are required to build a simple personal finance management tool. 
# The program should allow the user to: 
# ● Add an expense with details like date, category, description, and amount. 
# ● View all recorded expenses in a clean format. 
# ● Calculate total spending so far. 
# ● Exit the program gracefully when the user chooses to.

# ----------------------------------- 
# 💰 EXPENSE TRACKER (No Functions) 
# ----------------------------------- 



expense = []

while True :
    print("Welcome to Expense Tracker 💸")

    print("\n --------- MENU ---------")
    print("1⃣ Add Expense")
    print("2⃣ View All Expenses")
    print("3⃣ View Total Spending")
    print("4⃣ Exit")
    print("----------------------------")
    num = int(input("Enter your choice from 1 to 4: "))
    
    # 1⃣ Add Expense
    if(num == 1):
        date = input("Enter the date in (DD-MM-YYYY) : ")
        category = input("Enter the category (Foods , Travel etc.) : ")
        description = input("Enter the small description : ")
        amount = float(input("Enter the amount (₹) : "))

        dict = {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expense.append(dict)
        print("\n Your Expense is added successfully ✅")


    # 2⃣ View All Expenses
    elif(num == 2):
        if( len(expense) == 0):
            print("No Expense is added right now !!!❌")
        else:
            print("------ All Expense ------")
            i = 1
            for e in expense:
                print(f"{i}. {e["date"]} | {e["category"]} | {e["description"]} | {e["amount"]}")
                i += 1
                print("-------------------------------------")

    # 3⃣ View Total Spending
    elif(num == 3):
        sum = 0
        for a in expense:
            sum += a["amount"]
        print(f"\n Total Spending : ₹ {sum}")

    # 4⃣ Exit
    elif(num == 4):
        print("\n Now You are exit from Expense Tracker 👋👋.")
        break

    else :
        print("\n ❌ invaild choice please choose from 1 - 4  !! .") 