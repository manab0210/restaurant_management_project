import re
def is_valid_phone_number(phone_string):
    phone_regex=r'^(\+?\d{1,3})?[ \.-]?\(?\d{3}\)?[ \.-]?\d{3}[ \.-]?\d{4}$'
    if re.match(phone_regex,phone_string):
        return True
    return False