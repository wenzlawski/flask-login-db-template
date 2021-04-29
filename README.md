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
