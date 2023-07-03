import re

email = input("What's your email? ").strip()

# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9.]+\.edu$", email):
# if re.search(r"^\w[.?]+@\w+\.(edu|com)$", email, re.IGNORECASE)
if re.search(r"^(\w|\.?)+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
