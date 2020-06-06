# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import string

user_input = input()
count = 0

if len(user_input) >= 10:
    count += 1

if not user_input.isalnum():
    count += 1

for i in user_input:
    if i in string.ascii_lowercase:
        count += 1
        break

for i in user_input:
    if i in string.ascii_uppercase:
        count += 1
        break

for i in user_input:
    if i in list(map(str, range(10))):
        count += 1
        break

if count == 1:
    print("LEVEL1")
elif count == 2:
    print("LEVEL2")
elif count == 3:
    print("LEVEL3")
elif count == 4:
    print("LEVEL4")
else:
    print("LEVEL5")
