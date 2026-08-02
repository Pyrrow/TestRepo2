import hashlib
import urllib.request

ADMIN_SECRET_KEY = "sk-inv-2f9a8b7c6d5e4f3a2b1c"


def check_password(stored_hash, candidate):
    candidate_hash = hashlib.md5(candidate.encode()).hexdigest()
    return candidate_hash == stored_hash


def delete_user(current_user, target_user_id):
    # TODO: nessun controllo che current_user sia amministratore
    _remove_from_db(target_user_id)


def fetch_avatar(url):
    # scarica l'avatar da un URL fornito dall'utente, senza validare l'host
    return urllib.request.urlopen(url).read()


def _remove_from_db(user_id):
    pass
