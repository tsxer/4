from pathlib import Path
import re

def total_salary(file_path:Path):
  salary_formatted = []
  total = 0
  try:
    with open(file_path, "r", encoding="utf-8") as salary:
        for line in salary:
            digits = re.findall(r'\d+', line)  
            for digit in digits:
                salary_formatted.append(digit)
  except Exception as e:
    print(f"Произошла ошибка: {e}")

  for salary in salary_formatted:
    total += int(salary)
    average = total // len (salary_formatted)
  
  print(f"Общая сумма заработной платы: {total}, Средняя заработная плата: {average}")
  
  
total_salary(Path("salary_file.txt"))

