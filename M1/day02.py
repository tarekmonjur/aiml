# ---------------- String Methods ----------------
course_title = " Python for Beginners - # AI & ML "
print(course_title.strip())  # Remove leading and trailing whitespace
print(course_title.lower())  # Convert to lowercase
print(course_title.upper())  # Convert to uppercase
print(course_title.title())  # Convert to title case
print(course_title.replace("#", ""))  # Replace substring

# -------------- Method Chaining --------------
clean_title = course_title.strip().replace("#", "").title()
print(clean_title)
print(clean_title.find("Ai"))  # Find the index of substring "AI"
print("1234".isdigit())  # Check if the string is a digit
print("1234".isnumeric())  # Check if the string is numeric
print("Hello".isalpha())  # Check if the string is alphabetic
print("133".isalnum())  # Check if the string is alphanumeric

# -------------- String Slicing --------------
text = "Hello, World!"
print(text[0])  # First character
print(text[-1])  # Last character
print(text[0:5])  # Substring from index 0 to 4
print(text[7:])  # Substring from index 7 to the end
print(text[:5])  # Substring from the start to index 4
print(text[::2])  # Every second character
print(text[::-1])  # Reverse the string

# -------------- Conditional Statements  --------------
# ----- If-Else Statement -----
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# ----- Elif Statement -----
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

age = 25
if age < 13:
    print("You are a child.")
elif age > 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 50:
    print("You are an adult.")
else:
    print("You are a senior.")

# ----- Nested If Statement -----
age = 30
has_license = True
if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")

# ------------------ While Loop ------------------
count = 0
while count < 5:
    print(count)
    count += 1

# ------------------ Palindrome Check ------------------
world = "madam"
# world = "racecar"
if world == world[::-1]:
    print(f"{world} is a palindrome.")
else:
    print(f"{world} is not a palindrome.")

# ------------------ Anagram Check  ----------------
word1 = "listen"
word2 = "silent"
if sorted(word1) == sorted(word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

# ------------------ Data Masking ------------------
nid_number = 1234567890
nid_number = str(nid_number)
masked_nid = nid_number[:2] + "*" * (len(nid_number) - 4) + nid_number[-2:]
print(masked_nid)
