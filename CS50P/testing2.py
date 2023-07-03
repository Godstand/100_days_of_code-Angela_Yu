import re

url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username: {matches.group(3)}")
print(f"Username: {username}")

# name = input("What's your name? ").strip()
# if matches := re.search(r"^(.+), *(.+)$", name):
#     last = matches.group(1)
#     first = matches.group(2)
#     name = f"{first} {last}"
# print(f"hello, {name}")
