#age (integer) 
#is_employed (boolean) 
#credit_score (integer) 
#annual_income (float) 
#has_collateral (boolean) 

name = input('Name: ')
age = int(input("Age: "))
is_employed = input("Are you currently employed? (Yes/No) ")
credit_score = float(input("Your credit score "))
annual_income = float(input("Your annual income "))
has_collateral = bool(input("Do you have any collateral? (Yes/No) "))

base_rate = 0.0
if age >= 21 and is_employed == "Yes":
    print("Accepted base on age check")
    if credit_score >= 750:
        print("You have a great credit score")
        if annual_income >= 100000:
            base_rate = 4.5
            print("Your base rate is" , base_rate)
        else: 
            base_rate = 5.0
            print("Your base rate is" , base_rate)
    elif credit_score >= 600 and credit_score < 750:
        print("Your credit score is less than 750")
        if has_collateral == True:
            print("Since you have a collateral")
            base_rate = 7.0
            print("Your base rate is" , base_rate)
        elif annual_income <= 40000:
            print("Low annual income")
            base_rate = 9.0
            print("Your base rate is" , base_rate)
        else:
            base_rate = 8.0
            print("Yur base rate is" , base_rate)
    elif credit_score <= 600:
         print("Rejected due to low credit score")
else:
    print("Rejected due to invalid details")
elif age >65 and age < 60
print("Rejected due to age limit")
    