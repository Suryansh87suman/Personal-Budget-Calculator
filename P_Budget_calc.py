import csv
#It lets us read from and write to CSV files easily.

import os
#It provides a way of using operating system-dependent functionality like checking if a file exists.

from datetime import datetime
#It allows us to work with dates and times, useful for timestamping our budget entries.

print("💰|------  Personal Buget Calculator  ------|💰\n")
# -------- Income Section -----------

print("📈|--- Income Section ---|📈\n")
# -------- Income Categories -----------
Monthly_salary=float(input("\t💵 Enter your Monthly Salary : "))
Other_income=float(input("\t💵 Enter your Other Income (freelance, rent, interest, etc.) : "))
total_income=Monthly_salary+Other_income

# -------- Expense Section -----------
print("\n📉|--- Expense Section ---|📉\n")
# -------- Expense Categories -----------
print("\tEnter the following expenses : ")
housing=float(input("\t🏠 Housing Expense (rent, EMI, maintenance) : "))
Utlities=float(input("\t💡 Utlities Expense (electricity, water, gas, internet, phone) : "))
Food_Groceries=float(input("\t🍎 Food & Groceries Expense : "))
Transport=float(input("\t🚗 Transport Expense (fuel, public transport, vehicle maintenance) : "))
Healthcare=float(input("\t⚕️ Healthcare Expense (medicines, doctor visits, insurance) : "))
Education=float(input("\t📚 Education Expense (fees, books, courses) : "))
Entertainment_Shopping=float(input("\t🎉🛍️ Entertaintment & Shopping Expense : "))
Miscellaneous=float(input("\t📝 Miscellaneous : "))
total_expense=housing+Utlities+Food_Groceries+Transport+Healthcare+Education+Entertainment_Shopping+Miscellaneous
# -------- Balance Calculation -----------

print("\n📊|--- Balance Calculation ---|📊\n")
# ---------- Summary Section ------------
print("\t💵 Your Total Income is : ", total_income)
print("\t\t💼 Monthly Salary :", Monthly_salary, "(", Monthly_salary*100/total_income, "%)")
print("\t\t🪙 Other Income :", Other_income, "(", Other_income*100/total_income, "%)")
# -------- Expense Summary -----------
print("\n\t💸 Your Total Expense is :", total_expense)
print("\t\t🏠 Housing :", housing, "(", housing*100/total_expense, "%)")
print("\t\t💡 Utlities :", Utlities, "(", Utlities*100/total_expense, "%)")
print("\t\t🍎 Food & Groceries :", Food_Groceries, "(", Food_Groceries*100/total_expense, "%)")
print("\t\t🚗 Transport :", Transport, "(", Transport*100/total_expense, "%)") 
print("\t\t⚕️ Healthcare :", Healthcare, "(", Healthcare*100/total_expense, "%)")
print("\t\t📚 Education :", Education, "(", Education*100/total_expense, "%)")
print("\t\t🎉🛍️ Entertaintment & Shopping :", Entertainment_Shopping, "(", Entertainment_Shopping*100/total_expense, "%)")
print("\t\t📝 Miscellaneous :", Miscellaneous, "(", Miscellaneous*100/total_expense, "%)")

balance_calculation=(total_income)-(total_expense)
# ------------ Saving or Deficit Calculation ------------
if balance_calculation>=0:
    print("\n\t✅ ||  Your Saving  || :", balance_calculation)
    print("\n\tGreat! You are saving money.")
    if total_income!=0:
        print("\n\t📊 ||  Your Saving %  || :", (balance_calculation*100)/total_income)
    else:
        print("\n\t📊 ||  Your Saving %  || : 0")
    if balance_calculation>=10000:
        print("\n\t||  Your Saving Status  || : 🌟 Excellent")
    elif balance_calculation>=5000:
        print("\n\t||  Your Saving Status  || : 👍 Good")
    elif balance_calculation>=1000:
        print("\n\t||  Your Saving Status  || : 🙂 Average")
    else:
        print("\n\t||  Your Saving Status  || : ⚠️ Poor")    
else:
    print("\n\t🚨 ||  Your Deficit  || 🚨 :", balance_calculation)
    print("\n\tYou are in Deficit, Please Reduce your Expense")
    if total_income!=0:
        print("\n\t📊 ||  Your Deficit %  || :", (balance_calculation*100)/total_income)
    else:
        print("\n\t||  Your Deficit %  || : 0")

# ----------------- Advice Section -----------------
print("\n|--- Advice Section ---|\n")

expenses = {
    "Housing": housing,
    "Utilities": Utlities,
    "Food & Groceries": Food_Groceries,
    "Transport": Transport,
    "Healthcare": Healthcare,
    "Education": Education,
    "Entertainment & Shopping": Entertainment_Shopping,
    "Miscellaneous": Miscellaneous
}

# --------- Check savings health -----------
if balance_calculation > 0 and (balance_calculation*100/total_income) < 20:
    print("⚠️ Your savings are less than 20% of income. Try to save more.")
elif balance_calculation > 0:
    print("✅ Good job! You are saving enough.")

if balance_calculation < 0:
    print("⚠️ You are in deficit. Cut down on unnecessary expenses.")

# ----------------- Save Data to CSV -----------------
filename = "budget_data.csv"
file_exists = os.path.isfile(filename)

with open(filename, mode="a", newline="") as file:
    writer = csv.writer(file)
    
    # Write header if file is new
    if not file_exists:
        writer.writerow([
            "Date", "Monthly Salary", "Other Income", "Total Income",
            "Housing", "Utilities", "Food & Groceries", "Transport",
            "Healthcare", "Education", "Entertainment & Shopping", "Miscellaneous",
            "Total Expense", "Balance"
        ])
    
    # Write data row
    writer.writerow([
        datetime.now().strftime("%Y-%m-%d"),
        Monthly_salary, Other_income, total_income,
        housing, Utlities, Food_Groceries, Transport,
        Healthcare, Education, Entertainment_Shopping, Miscellaneous,
        total_expense, balance_calculation
    ])

print("\n✅ Your data has been saved to 'budget_data.csv'")
print("\nThank you for using the Personal Budget Calculator! 💰")
# ----------------- End of Program -----------------

"""
📌 Personal Budget Calculator

This program helps you calculate your total income, expenses, and savings/deficit.
It also gives you advice on how well you are saving.

Modules used:
1. csv       → To save all budget data into a CSV file.
2. os        → To check if the CSV file already exists (so headers are not duplicated).
3. datetime  → To record the current date for each entry.

Features:
- Takes user input for income and expenses.
- Shows income & expense breakdown with percentages.
- Calculates savings or deficit and gives status (Excellent, Good, Average, Poor).
- Provides advice based on savings/deficit.
- Saves all data into 'budget_data.csv' for future reference.

Author: (Suryansh suman ✍️)
1st year, B.Tech CSE-DS
"""
