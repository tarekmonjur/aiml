a = range(10)
result = []

for i in a:
    if i % 2 == 0:
        result.append(i)

print(result)

# --------------- list comprehension ---------------
new_result = [i for i in a if i % 2 == 0]
print(new_result)

new_result2 = [i**2 if i%2 == 0 else i for i in a]
print(new_result2)

# --------------- list comprehension with function ---------------
def is_even(n):
    return n % 2 == 0

new_result_with_function = [i for i in a if is_even(i)]
print(new_result_with_function)