# wiki-django 

Un sistema di scrittura in markdown, ideale per guide, tutorial e archivi di parti di codice usate occasionalmente. 

L'idea nasce per tenere ordinati pezzi di codice di programmazione scientifica utilizzati per analisi particolari, disorganizzati e persi all'interno delle proprie postazioni di lavoro, ma è estendibile a ogni situazione che richida un archivio di tutorial organizzato in categorie per una facile consultazione.


## Per iniziare

### Requisiti  

Il progetto è stato realizzato su ```Linux Mint 19.3```; per il funzionamento è necessaria una versione ```Python >= 3.6.9```.

### Installazione 

1. Clona il repository dentro la cartella di lavoro

```
git clone https://github.com/Leonardo-Bo/wiki-django.git
```

2. Crea un ambiente virtuale ```Python >= 3.6.9``` dentro la cartella di lavoro

```
python3.8 -m venv <nome_env>
```

3. Setta variabili di ambiente nel file ```active``` dentro la cartella ```<nome_env>/bin```. Alla fine del file aggiungi

```
export EMAIL_SYSTEM="<email_sistema>"
export EMAIL_PASS="<password_email_sistema>"
export EMAIL_ADMIN="<email_admin>"
export USER_ADMIN="<user_admin>"
```

Queste variabili vengono richiamate nel file ```settings.py```:

* ```EMAIL_SYSTEM``` invia un'email all'amministratore di sistema quando un utente invia una richiesta di iscrizione. Invia un'email all'utente quando l'amministratore attiva il suo account. Invia un'email a un utente quando il suo account viene eliminato

* ```EMAIL_PASS``` è la password di ```EMAIL_SYSTEM```

* ```EMAIL_ADMIN``` è l'email dell'amministratore

* ```USER_ADMIN``` è l'username dell'amministratore

4. Attiva l'ambiente virtuale

```
. <nome_env>/bin/activate
```

5. Aggiorna pip (opzionale) e installa i pacchetti richiesti

```
python -m pip install --upgrade pip
pip install -r requirement.txt
```

6. Effettua le migrazioni

```
cd wiki
python manage.py migrate
```

7. Crea l'amministratore di sistema. Email e password sono quelle settate al punto 3

```
python manage.py createsuperuser
```

8. Lancia il server!

```
python manage.py runserver
```

Il pannello di amministrazione si trova all'indirizzo ```http://127.0.0.1:8000/admin```

## Funzionalità 

1. Richiesta di iscrizione. Quando un utente effettua una richiesta di iscrizione viene inviata un'email all'amministratore di sistema e viene creato il profilo dell'utente. 

2. Una volta attivato dall'amministratore (dal pannello di amministrazione), l'utente può creare una categoria (ma non modificarla), creare una guida, modificare una guida da lui creata e modificare il proprio profilo.

3. L'autore di una guida può aggiungere dei collaboratori in grado di modificare la guida.

4. Un utente con privilegi di staff può modificare ogni guida.

5. Le guide vengono scritte in markdown. Sulla sidebar appare un'indice della guida formato dai tag \#.

## Prossimi obiettivi 

1. Una gestione accurata delle immagini. Deve essere possibile inserire e richiamare più immagini in una guida mentre questa viene scritta. Deve essere possibile selezionare le immagini già archiviate nel sistema (esempio: un'immagine del profilo che viene cambiata resta nel sistema, ma allo stato attuale non può essere reimpostata se non rifacendo l'upload).

## Riferimenti 

Questo progetto è stato sviluppato a partire da guide e tutorial reperiti dal web. In particolare sono stati fondamentali i tutorial di Corey Schafer e di Codemy su youtube.com.
