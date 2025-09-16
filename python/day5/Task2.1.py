num = int(input("Enter a number : "))
def sum_recursive(num):
    if num == 1:  # Base case
        return num
    return num + sum_recursive(num - 1)  # Recursive case

print(sum_recursive(num)) # 3 + 2 + 1 