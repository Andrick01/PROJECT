def calculate_electricity_bill(units):
    fixed_charge = 50.00
    bill = fixed_charge

    if units <= 0:
        return 0.0

    if units <= 100:
        bill += units * 1.50
    elif units <= 200:
        bill += (100 * 1.50) + ((units - 100) * 2.50)
    elif units <= 300:
        bill += (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    else:
        bill += (
            (100 * 1.50)
            + (100 * 2.50)
            + (100 * 4.00)
            + ((units - 300) * 6.00)
        )

    return bill


units_used =float(input("Enter the units used:"))
total_bill = calculate_electricity_bill(units_used)
print(f"Units Consumed: {units_used} kWh")
print(f"Total Bill Amount: ${total_bill:.2f}")