def main():
    incomes_list = []
    months = int(input("How many months: "))
    for i in range(1, months + 1):
        monthly_income = float(input("Enter income for Month {}: ".format(i)))
        incomes_list.append(monthly_income)
    print_income_report(incomes_list)


def print_income_report(incomes_list):
    print("Income Report" '\n' "_ _ _ _ _ _ _")
    total = 0
    for j in range(1, len(incomes_list) + 1):
        income = incomes_list[j - 1]
        total += float(income)
        print("Month {:>2} - Income: ${:>10.2f} Total: ${:>10.2f}".format(j, float(income), float(total)))

main()
