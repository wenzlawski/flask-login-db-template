## To run the flask app

`python3 start-backend.py`

## Once running you can test in a seperate terminal

### Registration

Edit the file `test-register.py`, specifically the payload variable to change username and password to register a new user.

`python3 test-register.py`

### Login

Edit the file `test-login.py`, specifically the payload variable to change username and password to login a user.

`python3 test-login.py`

### Access to protected functions using the cookie

!For this method to work you first have to register and log in a user, as the cookie has to be saved to a file!

`python3 test-protected.py`

## Using the API

### Register

Registration is on url `localhost/register`, and expects json encoded data in format

```
{
    "username": "testuser",
    "password": "testuserpassword",
}
```

This will return a String indicating whether a user has successfully been created.

### Login

Login is on url `localhost/login`, and expects json encoded data in format

```
{
    "username": "testuser",
    "password": "testuserpassword",
}
```

This will return a String indicating whether a user has successfully been logged in and a session cookie.

### Accessing protected functions

Once a user has been logged in, they get a persistent session cookie, which they can use to make requests to protected functions in the backend.o

To do this, the cookie must be included in every request.
