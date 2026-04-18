# -------------- while loop --------------
# while loop -> is used when the number of iterations is not known beforehand.
# while loop -> is condition dependent loop.
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("-" * 100)

hello_text = "Hello"
while len(hello_text):
    print(hello_text[0])
    hello_text = hello_text[1:]

print("-" * 100)

hello_text = "Hello"
hello_text_count = 0
while hello_text_count < len(hello_text):
    print(hello_text[hello_text_count])
    hello_text_count += 1

print("-" * 100)

# -------------- for loop --------------
# for loop -> is used when the number of iterations is known beforehand.
for i in range(5):
    print(i)

print("-" * 100)

# for item in container:
#     print(item)

for char in "Hello":
    print(char)

for i in range(5):
    print(i)

print("-" * 100)

# -------------- while loop example --------------
# guess_number = 7
# while True:
#     user_input = int(input("Guess the number (between 1 and 10): "))
#     if user_input == guess_number:
#         print("Congratulations! You guessed the number.")
#         break
#     else:
#         print("Try again!")

# print("-"*100)

# -------------- range function --------------
# range(start, stop, step) -> generates a sequence of numbers from start to stop (exclusive) with a step.

print(list(range(5)))  # Output: [0, 1, 2, 3, 4]
print(list(range(1, 6)))  # Output: [1, 2, 3, 4, 5]
print(list(range(0, 10, 2)))  # Output: [0, 2, 4, 6, 8]

print("-" * 100)

# -------------- word count --------------
text = "Hello world, I am learning Python programming!"
word_count = len(text.split())
print("Word count:", word_count)

print("-" * 100)

word_count = 0
for char in text:
    if char == " ":
        word_count += 1
word_count += 1  # Add 1 to count the last word
print("Word count:", word_count)

print("-" * 100)

word_count = 0
for char in text.split():
    word_count += 1
print("Word count:", word_count)

print("-" * 100)

# -------------- nested loops --------------
for i in range(3):
    for j in range(2):
        print(f"outer i: {i}, inner j: {j}")

print("-" * 100)

shirts = ["T-Shirt", "Shirt", "Polo"]
pants = ["Jeans Pant", "Khaki Pant", "Cargo Pant"]
for shirt in shirts:
    for pant in pants:
        print(f"Shirt: {shirt}, Pant: {pant}")

print("-" * 100)

# -------------- continue statement --------------

user_emails = [
    {"email": "user1@example.com", "send": True},
    {"email": "user2@example.com", "send": False},
    {"email": "user3@example.com", "send": True},
]
for user in user_emails:
    if user["send"] == True:
        print(f"Email already sent to: {user['email']}")
        continue

    print(f"Sending email to: {user['email']}")

print("-" * 100)

# -------------- pass statement --------------
for i in range(5):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(f"Odd number: {i}")

# -------------- break statement --------------
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(f"Number: {i}")

students = ["Alice", "Bob", "Charlie", "David"]
for student in students:
    if student == "Charlie":
        print("Found Charlie! Stopping the search.")
        break
    print(f"Checking student: {student}")

