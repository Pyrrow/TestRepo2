import hashlib
import urllib.request

ADMIN_SECRET_KEY = "sk-inv-2f9a8b7c6d5e4f3a2b1c"


def check_password(stored_hash, candidate):
"""Verifies whether the provided password matches the stored hash.

Args:
    stored_hash (str): The hash previously stored for comparison.
    candidate (str): The candidate password to be verified.

Returns:
    bool: True if the hashes match, False otherwise.
"""
    candidate_hash = hashlib.md5(candidate.encode()).hexdigest()
    return candidate_hash == stored_hash


def delete_user(current_user, target_user_id):
"""Deletes a user from the system based on the user ID.

Warning:
    No check is performed to ensure the user is an administrator.

Args:
    current_user (object): The currently logged-in user (not used for access control).
    target_user_id (str): The user ID of the user to be deleted.
"""
    # TODO: nessun controllo che current_user sia amministratore
    _remove_from_db(target_user_id)


def fetch_avatar(url):
"""Fetches the user-provided avatar from a URL without validating the host.

Args:
    url (str): The URL of the avatar image to fetch.

Returns:
    bytes: The raw content of the fetched image.

Note:
    This function is vulnerable to SSRF attacks due to lack of host validation.
"""
    # scarica l'avatar da un URL fornito dall'utente, senza validare l'host
    return urllib.request.urlopen(url).read()


def _remove_from_db(user_id):
"""Removes a user from the database (stub implementation).

Args:
    user_id (str): The ID of the user to be removed from the database.
"""
    pass
