table = int(input("Enter a Number for the Multiplication table:"))
print (f"Multiplication table for {table}:")

p = 1
while p <= 10:
    multiplication = table * p
    print(f"{table} x {p} = {multiplication}")
    p = p + 1