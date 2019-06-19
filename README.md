# conveyor-be

### Dockerized Postgresql DB (server and client), up and running

- Make sure docker deamon is running
- `docker-compose up -d` (d is for detached) should be enough to have postgresql set up. 
- there are two containers, one for postgres DB, and another for pgAdmin.
- If you already have installed postgresql on local machine please
 execute this command: `brew services stop postgresql` 
- execute `mkdir db-data` (in project root directory) to create directory that will be 
used as volume for the DB
- open local pgAdmin (http://localhost:5050), default credentials 
are `pgadmin4@pgadmin.org` and `admin` (see `docker-compose.yml`)
- create DB server, credentials are also in `docker-compose.yml`
    - Note: Instead of `localhost`, provide `postgres` as host name 
    (that's the bridged network connection name between two containers)
- create `db-data` database in pgAdmin
- To stop running docker container images execute: `docker-compose down`
 
 
#### PyCharm:
- Make sure that you have python3 and git installed: `python3 -V && git --version`
- PyCharm -> Check out from version control -> Git
- Select location where you want to clone and press 'Clone'
- Press 'Yes' if it asks you to create new directory
- PyCharm -> Preferences -> Project: <project_name> -> Project Interpreter
- Gear icon -> Add -> New Environment
- Make sure the path ends with `/<project_name>/venv` and press 'Ok'
- If it asks you to install packaging tools, press 'Install packaging tools'
- Open the terminal inside PyCharm and your terminal and it should start with `(venv)`
- Install dependencies: `pip3 install -r requirements.txt`
- Apply migrations: `python3 manage.py migrate`
- Run server: `python3 manage.py runserver`
- Visit: http://127.0.0.1:8000/ and you should see the application

### Starting an app for the first time

- Start docker containers with docker-compose (see above)

- `python3 manage.py migrate`
- `python3 manage.py createsuperuser --email admin@admin.com --username admin`
- `python3 manage.py runserver`


### Generating tokens for already created users
- `python3 manage.py drf_create_token <username>`


### Regenerating tokens
- `python3 manage.py drf_create_token -r <username>`


### Error: That port is already in use.
- `sudo lsof -t -i tcp:8000 | xargs kill -9`