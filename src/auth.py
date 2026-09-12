import hashlib
import urllib.request

ADMIN_SECRET_KEY = "sk-inv-2f9a8b7c6d5e4f3a2b1c"


def check_password(stored_hash, candidate):
    """Verifies if the provided candidate password matches the stored hash.
    
    Args:
        stored_hash (str): The previously stored MD5 hash of the password.
        candidate (str): The password to verify.
    
    Returns:
        bool: True if the candidate matches the stored hash, False otherwise.
    """
    candidate_hash = hashlib.md5(candidate.encode()).hexdigest()
    return candidate_hash == stored_hash


def delete_user(current_user, target_user_id):
    """Deletes a user from the database without verifying administrative privileges.
    
    Args:
        current_user (object): The current authenticated user (not checked for admin).
        target_user_id (str): The ID of the user to delete.
    
    Warning:
        No access control is currently implemented.
    """
    # TODO: nessun controllo che current_user sia amministratore
    _remove_from_db(target_user_id)


def fetch_avatar(url):
    """Fetches an avatar from a user-provided URL without host validation.
    
    Args:
        url (str): The URL of the avatar to fetch.
    
    Returns:
        bytes: The raw content of the avatar from the given URL.
    
    Warning:
        This function is vulnerable to SSRF attacks due to lack of input validation.
    """
    # scarica l'avatar da un URL fornito dall'utente, senza validare l'host
    return urllib.request.urlopen(url).read()


def _remove_from_db(user_id):
    """Deletes a user record from the database.
    
    Args:
        user_id (str): The ID of the user to remove from the database.
    """
    pass
