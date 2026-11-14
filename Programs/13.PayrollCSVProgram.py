#Payroll using CSV
import csv

FILE_NAME = "payroll.csv"

with open(FILE_NAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Employee", "Hours", "Hourly Rate", "Gross Pay"])

    while True:
        name = input("Employee name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        try:
            hours = float(input("Hours worked: "))
            rate = float(input("Hourly rate: "))
            if hours < 0 or rate < 0:
                print("Hours and rate cannot be negative.")
                continue
        except ValueError:
            print("Please enter numbers for hours and rate.")
            continue
        gross_pay = hours * rate
        writer.writerow([name, hours, rate, f"{gross_pay:.2f}"])
        print(f"Gross pay: {gross_pay:.2f}")

print(f"Payroll saved to {FILE_NAME}.")
