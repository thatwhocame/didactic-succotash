salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев
increase = 0.03  # Ежемесячный рост цен

total_spend = 0
for month in range(1, months + 1):
    total_spend += spend * (1 + increase) ** (month - 1)

total_income = salary * months
safety_cushion = int(total_spend - total_income)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {safety_cushion}")