# Cas pratique Diduenjoy


# Installation

## Package python

Le cas pratique a été réalisé en python. Les packages qui doivent être installés se trouvent dans le fichier `requirements.txt`.

```bash
pip install pandas psycopg2
```

## PostgresSQL

Installation de postgreSQL :
```
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
sudo apt-get install libpq-dev
```

Installation de la base de données :

```bash
sudo -u postgres psql
```

puis :

```sql
CREATE DATABASE diduenjoy;
```

enfin :
```sql
\i init.sql
```

Création d'un utilisateur :

```sql
CREATE USER test WITH PASSWORD 'test';
GRANT ALL PRIVILEGES ON DATABASE diduenjoy TO test;
GRANT ALL ON TABLE public.orders TO test;
GRANT ALL ON TABLE public.packages TO test;
GRANT ALL ON TABLE public.items TO test;
```

# Utilisation du script

```bash
 python3 main.py -f Orders.xlsx -H localhost -d diduenjoy -u test -p "test"
```

plus d'aide avec :
```bash
 python3 main.py -h
```

Le script ne fonctionne pas dans les cas suivants :

    - Il existe déjà un élément "order" en ID égal à 0 dans la base de données ;

    - Il existe déjà des packages d'id égals à 0 ou 1 dans la base de données ;