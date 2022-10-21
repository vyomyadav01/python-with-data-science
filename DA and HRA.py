basic_salary = float(input("Enter your basic salary:\n"))
if basic_salary <= 10000:
    hra = 0.1 * basic_salary
    da = 0.9 * basic_salary
    print("Your hra according to your basic salary is:\n",hra)
    print("Your da according to your basic salary is:\n",da)
elif basic_salary <=20000:
    hra = 0.2 * basic_salary
    da = 0.8 * basic_salary
    print(" Your hra according to your basic salary is:\n",hra)
    print(" Your da according to your basic salary is:\n",da)
elif basic_salary > 20000:
    hra = 0.25 * basic_salary
    da = 0.75 * basic_salary
    print("Your hra according to your basic salary is:\n",hra)
    print(" Your basic da according to your basic salary is:\n",da)