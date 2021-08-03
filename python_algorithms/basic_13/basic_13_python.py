# Print 1-255
def print_1_255():
    for i in range(1,256):
        print(i)

print_1_255()

sum = 0
for x in range(1,500001,3):
    sum = sum + x
print(sum)