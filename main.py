def calculate():
  try:
    first_number = float(input('Podaj pierwszą liczbę\n'))
    second_number = float(input('Podaj drugą liczbę\n'))
  except ValueError:
    print('Podane wartości nie są liczbami')
    return

  operation = input('Podaj operację (+, -, * lub /)\n')

  if operation == '+':
    result = first_number + second_number
  elif operation == '-':
    result = first_number - second_number
  elif operation == '*':
    result = first_number * second_number
  elif operation == '/':
    if second_number == 0:
      print('Nie można dzielić przez zero')
      return
    result = first_number / second_number
  else:
    print('Nieznana operacja')
    return

  print(f'Wynik: {result}')


def convert_temperature():
  unit = input('Podaj jednostkę (C lub F)\n').upper()

  try:
    temp = float(input('Podaj temperaturę\n'))
  except ValueError:
    print('Podana wartość nie jest liczbą')
    return

  if unit == 'C':
    print(f'{temp}°C = {temp * 1.8 + 32}°F')
  elif unit == 'F':
    print(f'{temp}°F = {(temp - 32) / 1.8}°C')
  else:
    print('Nieznana jednostka')


def calculate_grades():
  try:
    grades_count = int(input('Podaj liczbę ocen\n'))

    if grades_count <= 0:
      print('Liczba ocen musi być większa od zera')
      return

    grades = []
    for i in range(grades_count):
      grades.append(float(input(f'Podaj ocenę {i + 1}\n')))
  except ValueError:
    print('Podana wartość nie jest liczbą')
    return

  average = sum(grades) / len(grades)
  print(f'Średnia ocen: {average}')


try:
  exercise = int(input('Podaj numer ćwiczenia (1, 2, 3)\n'))
except ValueError:
  print('Podana wartość nie jest liczbą')
  exit()

match exercise:
  case 1:
    print('Wybrano ćwiczenie 1 - Prosty kalkulator dwóch liczb\n')
    calculate()
  case 2:
    print('Wybrano ćwiczenie 2 - Konwerter temperatury\n')
    convert_temperature()
  case 3:
    print('Wybrano ćwiczenie 3 - Średnia ocen ucznia\n')
    calculate_grades()
  case _:
    print('Nie wybrano żadnego ćwiczenia')
