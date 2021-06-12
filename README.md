# BluePrintFlaskProject
Flask project with Blueprint and connection with multi database capability and runs using gunicorn

This Project has been build on Ubuntu 20.04

This project connects with a MySQL and a postgresql DB

The DB tables schemas are defined in the model.py file

The DB configs are in config.py file


create a virtual environment

```
python3 -m venv venv --clear
```

activate the environemt

```
source venv/bin/activate
```
install the packages

```
pip3 install -r requirements.txt
```
deactivate the environment

```
deactivate
```

Run the application by typing
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
