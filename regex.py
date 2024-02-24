import re

def regex():
    text = """
    Hello, my email is tufan@gmail.com and my phone number is 111-222-3333.
    You can also reach me at faltu@yahoo.com or call me at 9898989898.
    I live at Namma Bengaluru.
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    phone_regex = r'\b[1-9]\d{9}\b'
    address_regex = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'

    emails = re.findall(email_regex, text)
    print("Email addresses found =>", emails)

    phones = re.findall(phone_regex, text)
    print("Phone numbers found =>", phones)

    addresses = re.findall(address_regex, text)
    print("Addresses found =>", addresses)
