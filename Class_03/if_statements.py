person_age = int(input("enter age: "))
AGE_OF_MAJ = 18
is_an_adult = person_age >= AGE_OF_MAJ

if is_an_adult:
    print("Person can vote")
    print("Thanks for using this system")
else:
    print("Person cannot vote")
    print("Try again")
print("Program finishing")

