import random

def main():
    x=int(input("How many sides does your dice have? "))
    number=random.randint(1,x)
    print("Your roll is ",number)

if __name__ == '__main__':
    main()
