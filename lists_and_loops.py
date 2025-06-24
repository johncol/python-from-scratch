names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])
print(names[1:2])

names.append('Jenny')
print(names)

names.insert(3, False)
print(names)

print("Bob" in names)
names.remove('Bob')
print("Bob" in names)
print(names)

print("for loop:")
for name in names:
    print(f"  name: {name}")

print("while loop:")
index = 0
while index < len(names):
    print(f"  name: {names[index]}")
    index += 1