age = int(input(Enter your age -->  ""))
monthly_revenue = float(input("Enter your monthly salary -->   "))
credit_score = int(input("Enter your Credit score -->  "))
business = float(input("How long have you been in the industry?   "))
has_defaults = bool(input("Do you have any bankcruptcy record? (Yes/No) "))
collateral_name = input("Collateral name -->    ")
collateral_value = float(input("Collateral value ---> "  ))

max_loan = 0
base_fee = 0

if age >= 21 and age < 21: #tier1
    print("MEET THE AGE REQUIRMENT")
    if credit_score >= 720:
        print("CREDIT SCORE CONSIDERED HIGH")
        max_loan = monthly_revenue * 3
        if monthly_revenue >= 50000:
            print("ABOVE 50K REVENUE")
            base_fee = max_loan * 0.015
            print("BASE FEE IS SET TO", base_fee)
        else:
            print("REVENUE BELOW 50K")
            base_fee = max_loan * 0.025
            print("BASE FEE IS SET TO", base_fee)

    elif 