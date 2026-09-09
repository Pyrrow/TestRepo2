# inventory-service

> Repository di prova per Code Guardian. Simula un piccolo servizio di gestione inventario (ricerca prodotti, autenticazione, report), con alcune vulnerabilità introdotte deliberatamente per testare l'agente OWASP, e alcune funzioni prive di documentazione per testare l'agente Docs.

## Features
- Simulazione di funzionalità di un servizio di gestione inventario
- Implementazione di un sistema di autenticazione (file `src/auth.py`)
- Logica per la gestione del database (file `src/db.py`)
- Generazione di report (file `src/reports.py`)
- Utilizzo di utility comuni (file `src/utils.py`)
- Inclusione intenzionale di vulnerabilità per scopi di testing
- Documentazione limitata di alcune funzioni per testare l'analisi

## Prerequisites
- Python 3.x

## Installation
```bash
# Clona il repository
git clone https://github.com/example/inventory-service.git
cd inventory-service
```

## Configuration
Il progetto non richiede alcuna configurazione estesa, ma i file presenti in `src` dipendono da un set di funzionalità Python standard.

## Usage
Non è prevista un'esecuzione reale di questo codice. Puoi esaminarlo localmente per comprenderne la struttura e scoprire le funzionalità o vulnerabilità nascoste.

## Project Structure
Il codice risiede interamente nel directory `src`. Di seguito una sintesi:

```
src/
├── auth.py       # Gestione autenticazione utente con vulnerabilità simulate
├── db.py         # Simulazione logica di accesso al database
├── reports.py    # Moduli di generazione report con funzioni scarsamente documentate
└── utils.py      # Funzioni utilità condivise
```

## License
Non viene specificata alcuna licenza per il codice, e non è applicabile poiché il progetto non ha una destinazione d'uso reale.
