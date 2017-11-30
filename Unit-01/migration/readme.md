# SQL With Flask

For this application you will be refactoring CRUD on the resouce `snacks`. Instead of using a list, your application should use postgres and the `psycopg2` module! 

Make sure that you isolate your `psycopg2` related code into a file called `db.py` so that you do not have one large `app.py` file.

Make sure you create a database called `flask-sql-snacks` for your application and in order to run the tests, make sure you create a database called `flask-sql-snacks-test`

Your application should:

- display all the `snacks`
- allow a user to create `snacks` 
    -  each snack should have a `name` and `kind`
- allow a user to edit a snack
- allow a user to delete a snack

