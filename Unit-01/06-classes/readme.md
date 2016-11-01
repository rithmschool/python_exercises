# Classes

### Part 1

Answer the following questions

- What is a class?
- What is an instance?
- What is inheritance?
- What is multiple inheritance?
- What is polymorphism?
- What is `method resolution order` or `MRO`?

### Part 2

Create a deck of cards class.  Internally, the deck of cards should use another class, a card class.  Your requirements are:

* The `Deck` class should have a `deal` method to deal a single card from the deck
* After a card is dealt, it is removed from the deck.
* There should be a `shuffle` method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
* The `Card` class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)


### Part 3

Make a the following 3 classes:

* `StreamReader`:  A stream reader should have a method `read` that reads data from the stream (a stream set of characters coming from some source).  Implement read so that it exists, but make it do nothing. You can just have it return `None`
* `FileStreamReader`: A class that inherits from `StreamReader` and implements the `read` method.  The `FileStreamReader` should be given a file name to open when the class is instantiated.
* `UrlStreamReader`: A class that inherits from `StreamReader` and implements the `read` method. The class should be given a url when the class is instantiated.  The `read` method should make a HTTP GET request and then read the data from the url.

Next, create a main script that creates an array of `FileStreamReaders` and `UrlStreamReaders`. Loop through the array and call `read` on each stream.  Print the results to the terminal.

__BONUS__

Figure out how to read command line arguments using a python script.  If the argument starts with `http`, create a `UrlStreamReader`.  If the argument does not start with `http`, assume it is a file path and create a `FileStreamReader`.
