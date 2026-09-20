#my student resutls

name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = maths + science + english
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

if maths >= 35 and science >= 35 and english >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")