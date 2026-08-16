```python
# Import necessary libraries for handling clipboard and regular expressions
import pyperclip
import re

# Regular expression pattern to match phone numbers
# This pattern matches 10-digit phone numbers, including area code, 
# separators, and optional extension
phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code (3-digit number or 3 digits in parentheses)
    (\s|-|\.)?  # Separator (space, hyphen, or period)
    (\d{3})  # First 3 digits
    (\s|-|\.)  # Separator (space, hyphen, or period)
    (\d{4})  # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension (optional)
    )''', re.VERBOSE)

# Regular expression pattern to match email addresses
# This pattern matches a username, @ symbol, domain name, and top-level domain
email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # Username (letters, numbers, or special characters)
    @  # @ symbol
    [a-zA-Z0-9.-]+  # Domain name (letters, numbers, or special characters)
    (\.[a-zA-Z]{2,4}){1,2}  # Top-level domain (dot followed by 2-4 letters)
    )''', re.VERBOSE)

# Get the text from the clipboard
text = str(pyperclip.paste())

# Initialize an empty list to store matches
matches = []

# Find all phone numbers in the text using the phone_re pattern
for groups in phone_re.findall(text):
    # Format the phone number with separators and optional extension
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    # Add 'x' and extension if it exists
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

# Find all email addresses in the text using the email_re pattern
for groups in email_re.findall(text):
    matches.append(groups[0])

# Check if any matches were found
if len(matches) > 0:
    # Copy the matches to the clipboard
    pyperclip.copy('\n'.join(matches))
    # Print the matches to the console
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    # Print a message if no matches were found
    print('No phone numbers or email addresses found.')
```