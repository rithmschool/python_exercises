# Hashing-Sessions

### Part 1

Continue building on the simple authentication app from the [curriculum](https://github.com/rithmschool/python_curriculum/blob/master/Unit-03/03-hashing_cookies_sessions.md). Add a `show` page and an `edit` page for your users. Make it so that you can view any user's show page, provided you're logged in, but you can only access your own edit page, not anyone else's.

### Part 2

Add authentication to your users and messages application! You should also have an additional route:

`GET /messages` - shows all of the messages for every user - a user does not need to be logged in to see this content.

- Make sure that users can not create, edit or delete other users AND that users can not create, edit or delete messages for other users! This will require you to write some custom decorators so you can successfully implement authorization. 
