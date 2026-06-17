# Example 1: Copying using b = a

a = [5, 4, 3, 0, 0, 8, 1]

print("Raw value of a :")
print(a)

b = a

print("After copying using (b = a) the value of b :")
print(b)

b.append(10)

print("After append value in b :")
print(b)

print("After append value in b the value of a :")
print(a)


# Example 2: Copying using d = c.copy()

c = [1, 2, 3, 0, 5, 4]

print("Raw value of a :")
print(c)

d = c.copy()

print("After copying using (d = c.copy()) the value of d :")
print(d)

d.append(10)

print("After append value in d :")
print(d)

print("After append value in d the value of c :")
print(c)
