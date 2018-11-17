n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)     # div n by 2, result and remainder
    remainders.append(remainder)    # we keep track of remainders

# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)