import re

def is_valid_contact_number(contact_number):
    # Defining  a regular expression pattern to match valid phone number formats based on given conditions
    pattern = r'^(\+?\d{1,2}\s?)?(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$'
    
    # Using re.match to check if the contact number matches the pattern
    if re.match(pattern, contact_number):
        return True
    else:
        return False

def main():
    
    contact_number = input("Enter the contact number: ")
    if is_valid_contact_number(contact_number):
        print("The contact number is valid.")
    else:
        print("The contact number is invalid.")

if __name__ == "__main__":
    main()

