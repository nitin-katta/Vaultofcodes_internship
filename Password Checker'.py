import re
# Importin regex module for patterns

def valid_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*+!]).{8,}$" # This regular expression pattern enforces certain rules for a valid password:
# 1. ^ - Anchors the match to the start of the string.
# 2. (?=.*[A-Z]) - Requires at least one uppercase letter (A-Z).
# 3. (?=.*[a-z]) - Requires at least one lowercase letter (a-z).
# 4. (?=.*\d) - Requires at least one digit (0-9).
# 5. (?=.*[@#$%^&*+!]) - Requires at least one special character from the set [@#$%^&*+!].
# 6. .{8,} - Matches any character (.) of any kind, at least 8 times ({8,}) in total.
# 7. $ - Anchors the match to the end of the string.

# So, this pattern ensures a valid password:
# - Contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
# - Is at least 8 characters in length.
    
    if re.match(pattern, password): 
        if len(password) > 8:
            return "Password is Strong"
        elif len(password) in range(6,8) :
            return "Password is Medium"
        elif len(password) < 6:
            return "Password is Weak"
    else:
        return "Invalid Password"

# Example usage:
print(valid_password("MyPasswprd!2"))
print(valid_password("Msdjjehfui2"))
print(valid_password("My23"))

