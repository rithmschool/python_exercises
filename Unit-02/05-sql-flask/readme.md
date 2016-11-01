# SQL With Flask

For this application you will be refactoring CRUD on the resouce `snacks`. Your application should:

- display all the `snacks`
- allow a user to create `snacks` 
    -  each snack should have a `name` and `kind`
- allow a user to edit a snack
- allow a user to delete a snack

Instead of using a list, your application should use postgres and the `psycopg2` module! 

### Bonus

Isolate your `psycopg2` related code into a file called `db.py` so that you do not have one large `app.py` file.
