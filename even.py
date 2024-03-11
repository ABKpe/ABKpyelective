nbers = input("Enter a list of nbers separated by spaces: ").split()
nbers = [int(n) for n in nbers]
even_nbers = [n for n in nbers if n % 2 == 0]
even_nbers.sort()
print("The list of even nbers in ascending order are:", even_nbers)