money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0
while money_capital >= 0:
  months += 1
  spend *= (1 + increase)  # Увеличиваем траты с учетом инфляции
  money_capital -= (spend - salary)

print("Количество месяцев, которое можно протянуть без долгов:", months)
