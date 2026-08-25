name = input("Enter your name: ")

mark1 = int(input("Enter mark for Subject 1: "))
mark2 = int(input("Enter mark for Subject 2: "))
mark3 = int(input("Enter mark for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")