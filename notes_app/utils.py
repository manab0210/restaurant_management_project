import logging
from email.utils import parseaddr
logger=logging.getLogger(__name__)
def is_valid_email(email:str) -> bool:
    try:
        if not email or not isinstance(email,str):
            return False
        name,addr=parseaddr(email)

        if '@' in addr and '.' in addr.split('@')[-1]:
            return True
        return False
    except Exception as e:
        logger.error(f"Error validation email '{email}':{e}")
        return False