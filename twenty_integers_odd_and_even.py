#Separate even and odd numbers from numbers.txt

#Make a list for even and odd nums
even_numbers = []
odd_numbers = []

for line in file:
    num = int(num.strip())

    if num % 2 == 0:
        even_file.write(str(num) + "\n")
    else:
        odd_file.write(str(num) + "\n")
