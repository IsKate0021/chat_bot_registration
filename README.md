# tg_bot_registration
bot for saving and updating credentials

## Run bot
### Open in the terminal this repo
```bash
cd %project directory%
```

### Run docker compose from file 
```bash
docker compose up -d
```

### Get containers id
``` bash
docker container ls
```

### Open python container
``` bash
docker container exec -it %container id% bash
```

### Open script directory
``` bash
cd ./code
```

### Launch code
``` bash
python # python file name
```

# Work with MySQL
To work with DB manually

### Open MySQL container
``` bash
docker container exec -it %container id% bash
```

### Open mysql terminal
``` bash
mysql -u %user name% -p
```
then you need to input password

### Select DB
``` SQL
USE myDB;
```

### Get all rows from table
``` SQL
SELECT * FROM credentials;
```

### Delete all rows from table
``` SQL
DELETE FROM credentials;
```

# Push to github

### Add all the files to the given folder
``` bash
git add . 
```

### View all the files which are going to be staged to the commit
``` bash
git status
```

### Create a commit message
``` bash
git commit -m 'your message'
```

### Push to github
``` bash
git push
```

# Python proc
``` bash
pip freeze > requirements.txt
```