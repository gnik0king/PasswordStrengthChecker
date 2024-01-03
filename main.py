import string

def check_password(password):
    score = 0

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


"""
What to add:
- How long it would take for a hacker/computer to guess the password (seconds - years)
- Link to sites giving tips on how to create a strong password
- Link to trusted password managers (or site that lists top managers (in 2024))
"""

password = input("Enter your password: ")
check_password(password)