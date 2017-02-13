# Flask Templating

Create a new Flask application with the following:

### Part 1

- A `base.html` template for others to inherit from
- A route for `/person/<name>/<age>` which renders a template that displays the name and age entered for the URL. That template should inherit from `base.html` 

### Part 2

Refactor your calculator application from before! 

- have a route for `/calculate` which renders a template called `calc.html`
- in `calc.html`, build a form which has two inputs (one with a name of `num1` and another with the name of `num2`for numbers and a select field with the name of `calculation` with options for "add", "subract", "multiply" and "divide". 
- When the form is submitted it should make a request to a route called `/math`
- In your python file, accept the values from the form and depending on what the request contains, respond with the sum, difference, product or quotient.

### Part 3

Create a small application which grabs headlines from Google News by keyword. (This application is based on the [Google News web scraper](https://www.rithmschool.com/courses/python-fundamentals-part-2/python-web-scraping-exercises) from the web scraping exercises.)

- This application should consist of two routes, `/` and `/results`
- When the server receives a request to `/`, it should render an HTML page with a form prompting the user for a keyword (e.g. "California"). Submitting the form should result in a request to `/results`, with the form input passed in the [query string](https://en.wikipedia.org/wiki/Query_string).
- When the server receives a request to `/results`, it should do the following:
    1. Grab the keyword from the query string;
    2. Make a request to `https://news.google.com`, and scrape the respose HTML for all news articles (links and headlines);
    3. Filter out articles whose headlines do not match the keyword passed in from the query string;
    4. Render an HTML page with matching articles (links and headlines) in a list.

