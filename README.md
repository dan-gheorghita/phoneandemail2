# phoneAndEmail.py

**Description of the Python Code**

This Python script is designed to extract phone numbers and email addresses from a given text and copy them to the clipboard. The script uses regular expressions to match and format the phone numbers and email addresses.

**How the Script Works**

1. The script starts by importing the necessary libraries, `pyperclip` for handling the clipboard and `re` for regular expressions.
2. Two regular expression patterns are defined: `phone_re` to match phone numbers and `email_re` to match email addresses.
3. The script uses `pyperclip` to get the text from the clipboard and store it in the `text` variable.
4. It initializes an empty list `matches` to store the extracted phone numbers and email addresses.
5. The script uses the `findall` method of the `phone_re` pattern to find all phone numbers in the text and formats them with separators and optional extensions. The formatted phone numbers are added to the `matches`