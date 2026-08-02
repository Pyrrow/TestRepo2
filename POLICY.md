# Regole di sviluppo sicuro — inventory-service

REGOLA-1: tutte le query SQL devono essere parametrizzate, mai costruite con
concatenazione o interpolazione di stringhe.

REGOLA-2: è vietato l'uso di MD5 o SHA1 per l'hashing di password; usare
bcrypt o argon2.

REGOLA-3: ogni operazione distruttiva (cancellazioni massive, reset) deve
essere loggata con utente, timestamp ed esito.

REGOLA-4: le operazioni riservate agli amministratori devono verificare
esplicitamente il ruolo dell'utente corrente prima di procedere.
