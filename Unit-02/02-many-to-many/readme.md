# Many To Many Example

A departments and employees app that illustrates many to many.

### Setup

* Make a virtual environment

```sh
mkvirtualenv m2m
```

* Make the `many-many-example` database:

```sh
createdb many-many-example
```

* pip install requirements.txt:

```sh
pip install -r requirements.txt
```

* Upgrade the database so that your tables are created correctly:

```sh
python manage.py db upgrade
```

### Testing

Unit tests are located in `project/tests`.  To run all the tests as once, type `green` in the root of the project.

To run a specific tests (if you want to debug with ipython):

```sh
python -m project.tests.<name_of_test> # no .py at the end
```
