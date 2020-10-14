"This is a string."  # ?
"This is a string."
'This is also a string.'

'I told my friend, "Python is my favorite language！"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
# 2.3.1======================================================================================================================

name = "ada lovelace"
print(name.title())
# ---------------------------------------------------------------------------------------------------------------------
name = "ada lovelace"
print(name.upper())
print(name.lower())

# 2.3.2======================================================================================================================

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

# ---------------------------------------------------------------------------------------------------------------------
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print("Hello, " + full_name.title() + "!")

# ---------------------------------------------------------------------------------------------------------------------
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "Hello, " + full_name + "!"
print(message)

# 2.3.3======================================================================================================================
print("Python")
print("\tPython")

print("Language:\nPython\nC\nJavaScript")

print("Language:\n\tPython\n\tC\n\tJavaScript")


# 2.3.4======================================================================================================================
favorite_language = 'python '
favorite_language
favorite_language.rstrip()
favorite_language
# ---------------------------------------------------------------------------------------------------------------------
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
favorite_language
# ---------------------------------------------------------------------------------------------------------------------
favorite_language = ' python '
favorite_language.rstrip() #砍右邊的空格
favorite_language.lstrip() #砍左邊的空格
favorite_language.strip() #砍左右兩邊的空格
# 2.3.5======================================================================================================================
message = "One of Python's strengths is its diverse community"
print(message)

message = 'One of Python's strengths is its diverse community'
print(message)
# 2.3.6======================================================================================================================
"不想管python 2"
