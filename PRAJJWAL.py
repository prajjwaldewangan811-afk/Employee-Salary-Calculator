import math
def read_basic_salary():
    while True:
       try:
            basic = float(input("Enter basic salary: "))

            if not math.isfinite(basic) or basic <= 0:
                print("Invalid salary. Enter a positive number.")
                continue

            if not math.isfinite(basic * 1.30):
                print("Salary is too large. Enter a smaller number.")
                continue

            return basic
       
       except ValueError:
            print("Invalid salary. Enter a positive number.")
        
        

#calculating hra da gross
def calculate_gross(basic):
    """Calculate HRA, DA and gross salary from basic salary."""
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da
    return hra, da, gross

#calculating tax
def calculate_tax(gross):
    """Calculate tax according to the given tax slabs."""
    if gross <= 25000:
        tax = 0
    elif gross <= 50000:
        tax = gross * 0.05
    else:
        tax = gross * 0.10
    return tax

#calculating salary components
def calculate_salary(basic):
    hra,da,gross = calculate_gross(basic)
    pf = basic * 0.12
    tax = calculate_tax(gross)
    net_salary = gross - pf - tax
    return hra, da, gross, pf, tax, net_salary
#readind the text for employee name and id 
def read_required_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        print("This field cannot be empty. Please enter a valid value.")

#PRINTING THE SALARY SLIP
def print_salary_slip(name,basic,emp_id,hra,da,gross,pf,tax,net_salary):
    print("\n" + "="*48)
    print("EMPLOYEE SALARY SLIP".center(48))
    print("="*48)
    print(f"Employee Name: {name}")
    print(f"Employee ID: {emp_id}")
    print(f"Basic Salary: {basic:,.2f}")
    print("-"*48)
    details = [("Basic Salary", basic),
               ("HRA", hra),
               ("DA", da),
               ("Gross Salary", gross),
               ("PF", pf),
               ("Tax", tax),
               ("Total Deductions", pf + tax),
               ("Net Salary", net_salary),]
    for label, value in details:
        print(f"{label:<30}:{value:>10,.2f}")

    print("="*48)


#the main function to run the program
def main():
    print("EMPLOYEE SALARY CALCULATOR")
    while True:
        #checking for valid employee name
        name = read_required_text("enter the employee name:")
        while not name.replace(" ", "").isalpha():
            print("Invalid name. Please enter only alphabetic characters and spaces.")
            name = read_required_text("enter the employee name:")


        #checking for the valid employee id
        emp_id = read_required_text("enter the employee id(10 characters):")
        while len(emp_id)!=10:
            print("Invalid employee ID. It must be exactly 10 characters long.")
            emp_id = read_required_text("enter the employee id(10 characters):")


        basic = read_basic_salary()
        hra,da,gross,pf,tax,net_salary = calculate_salary(basic)
        print_salary_slip(name,basic,emp_id,hra,da,gross,pf,tax,net_salary)


        while True:
            choice = input("Calculate for another employee? (y/n): ").strip().lower()

            if choice in ("y", "n"):
                break

            print("Enter y or n.")


        if choice == "n":
                print("Thankyou for calculating.")

                break


if __name__ == "__main__":
    main()