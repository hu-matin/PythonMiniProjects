import re

pattern = r'^[a-zA-Z0-9._-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,7}$'
emails = ["matin@gmail.com","matin gmail.com"]

for i, email in enumerate(emails):
    
    validate = re.fullmatch(pattern, email)

    if validate:
        print(f"This email [{emails[i]}] is correct.\u2705")
    else:
        print(f"This email [{emails[i]}] is incorrect.\u274C")