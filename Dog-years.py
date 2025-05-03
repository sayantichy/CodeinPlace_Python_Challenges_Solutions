DOG_YEARS_MULTIPLIER = 7.18  

def main():
    dog_age = int(input("Enter an age in calendar years: "))
    dog_years = dog_age * DOG_YEARS_MULTIPLIER
    print(f"That's {dog_years} in dog years!")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
