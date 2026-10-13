
# Online Shopping Discount Eligibility

order_amount = float(input("Enter the order amount: "))
membership = input("Are you a member? (yes/no): ").strip().lower()

if order_amount < 0 or order_amount > 100000:
    print("Invalid order amount.")

elif membership != "yes" and membership != "no":
    print("Invalid membership status. Please enter yes or no.")

else:
    discount_percentage = 0

    if order_amount >= 5000:
        discount_percentage = 15

    elif membership == "yes" and order_amount >= 2000:
        discount_percentage = 10

    discount_amount = order_amount * discount_percentage / 100
    final_amount = order_amount - discount_amount

    print("Original amount: ₹", order_amount)
    print("Discount percentage:", discount_percentage, "%")
    print("Discount amount: ₹", discount_amount)
    print("Final payable amount: ₹", final_amount)

    if discount_percentage > 0:
        print("Eligibility status: Eligible for a discount.")
    else:
        print("Eligibility status: Not eligible for a discount.")
