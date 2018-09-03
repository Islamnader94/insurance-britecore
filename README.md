### Installing Dependencies

```
pip install -r requirements.txt
```
### Entity relationship Diagram

ERD-Diagram:

https://octodex.github.com/images/ERD.png

### Running the App

To run the app, first run the `models.py` file directly to create the database tables:

```
$ python models.py
```
### Running the tests

To run the Database test:

```
$ python test_base.py
```

To run the api test:

```
$ python test_api.py
```

To run the server test:

```
$ python test_server.py
```
### For pep8 checking:

To install autopep8:

```
$ pip install autopep8==0.8
```

run the following command as the example below ending with .py,
then copy & paste the code to check if there where changes:

```
$ autopep8 models.py
```

To run the app itself:

```
$ python app.py
```

Visit [http://localhost:5000/](http://localhost:5000/) in your browser to see the results.
