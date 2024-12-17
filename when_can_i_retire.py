import datetime
current_year = datetime.date.today().year

def main():
  age = int(input("\nWhat is your age? "))
  name = input("\nWhat is your name? ")
  target_year = current_year + (65 - age)
  print(f"\n\nHello {name} in the year {target_year} you will be 65 years old!")

if __name__ == "__main__":
  main()
