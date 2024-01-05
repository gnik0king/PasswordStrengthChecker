import string

def check_password_strength(password: str) -> int:
    global x
    score = 0
    x = 0

    """
    Score tiers - reflection of how long a computer would take to guess it:
    00-10
    11-20
    21-30
    31-40
    41-50
    51-60
    61-70
    71-80
    81-90
    91-100
    """

    
    # CHARACTER #
    # Check if password contains at least one character from each required character class (ie. uppercase, lowercase, digit, or special character)
    if any(c.isupper() for c in password):
        score += 1
        x = 1
    if any(c.islower() for c in password):
        score =+ 1
        x += 1
    if any(c.isdigit() for c in password):
        score += 1
        x += 1
    if any(c in string.punctuation for c in password):
        score += 1
        x += 1

    if x < 4:
        return score
    


    # CHARACTER LENGTH #
    # 8-11       Level 1
    # 12-15      Level 2
    # 16-19      Level 3
    # 20+        Level 4
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if len(password) >= 20:
        score += 1

    return score

def check_password(password: str) -> None:
    # Read common passwords
    global y
    




"""
What to add:
- How long it would take for a hacker/computer to guess the password (seconds - years)
- Link to sites giving tips on how to create a strong password
- Link to trusted password managers (or site that lists top managers (in 2024))
"""

password = input("Enter your password: ")
check_password(password)