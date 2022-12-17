# Flask-Restful

Demo project utilizing SQLAlchemy, Migrate & Marshmallow
 
### Prerequisites:

To run the project python 3.x and git should be installed.

### Project Setup:

1. Clone the repo using following command:  
```
git clone https://github.com/javeriae/flask-restful.git
```

2. Create a python3 virtualenv and activate it:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install the project requirements from requirements.txt:
```
pip install -r requirements.txt
```

4. Run the project:
```
flask run
```

5. Use Basic Authentication in each request. A test user has already been added in the database.
```
username: javeria
password: 12345
```

### Decryption:

To decrypt the response from endpoints, use the following endpoint:
```
/decrypt
```

Add the encrypted text as a JSON raw-data in the request.
```
{
    "text": "ENCRYPTED TEXT"
}
```