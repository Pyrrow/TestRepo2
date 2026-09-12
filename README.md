# inventory-service

Repository di prova per Code Guardian. Simula un piccolo servizio di
gestione inventario (ricerca prodotti, autenticazione, report), con alcune
vulnerabilità introdotte deliberatamente per testare l'agente OWASP, e
alcune funzioni prive di documentazione per testare l'agente Docs.

Non è codice reale: non eseguirlo, serve solo come fixture di analisi.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)

## Features
- Simulazione di un servizio di gestione inventario
- Autenticazione fittizia
- Funzionalità di ricerca e report
- Vulnerabilità deliberate per test OWASP
- Documentazione mancante per test Docs agent

## Project Structure
Struttura del progetto con file principali:
```text
inventory-service/
├── .DS_Store
├── POLICY.md
├── README.md
└── src/
    ├── auth.py
    ├── db.py
    ├── reports.py
    └── utils.py
```

- **src/**: cartella principale contenente il codice sorgente
  - **auth.py**: gestisce l'autenticazione
  - **db.py**: gestisce le operazioni di persistenza
  - **reports.py**: genera report
  - **utils.py**: funzioni utili o helper

## License
Non definito.
