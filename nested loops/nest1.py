#  Create  a  python  program  to  print  the  multiplication  tables  of  different numbers


numbers = [2, 3, 5, 7]
for num in numbers:
    print(f"Multiplication table for {num}:")
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()

