# Payment Websocket API

This project aims to create a Payment API using Websocket and [Flask](https://flask.palletsprojects.com/en/3.0.x/).

## Requirements

- The API must to persist Payment data on database;
- The Payment must to have the attributes:

  - id
  - value
  - paid
  - bank_payment_id
  - qr_code
  - expiration_date

- The API must to have the following endpoints:
  - Create Payment
  - Get QR Code
  - Pix Confirmation

## Create and Activate Virtual Env

Open terminal and run the scripts:

```python
python -m virtualenv venv
source venv/Scripts/activate
```

## Install dependencies

```python
pip3 install -r requirements.txt
```

## Database commands

```python
flask shell
>>> db.drop_all()
>>> db.create_all()
>>> exit()
```

## Run project

```python
python app.py
```

## References

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/3.1.x/)
