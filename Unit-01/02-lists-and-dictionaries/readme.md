# Lists and Dictionaries

### List Comprehension

Write the following Python code to do the following (complete ALL of these using `list comprehension`)

1. Given a list `[1,2,3,4]` print out all the values in the list
2. Given a list `[1,2,3,4]` print out all the values in the list multiplied by 20
3. Given a list `["Elie", "Tim", "Matt"]`, return a new list with only the first letter (`["E", "T", "M"]`)
4. Given a list `[1,2,3,4,5,6]` return a new list of all the even values
5. Given two lists `[1,2,3,4]` and `[3,4,5,6]`, return a new list that is the intersection of the two `[3,4]`
6. Given a list of words `["Elie", "Tim", "Matt"]` return a new list with each word reversed and in lower case `['eile', 'mit', 'ttam']` (google how to reverse a string in python for help)
7. Given two strings "first" and "third", return a new string with all the similar letters
8. For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12
9. Given the string "amazing", return a list with all the vowels removed `['m', 'z', 'n', 'g']`
10. Generate a list with the value `[[0, 1, 2], [0, 1, 2], [0, 1, 2]]`
11. Generate a list with the value: 
```py
[
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 ]
```


### Dictionary Comprehension

Write the following Python code to do the following (Complete ALL of the following using `dictionary comprehension`)

1. Given a list `[("name", "Elie"), ("job", "Instructor")]`, create a dictionary that looks like this `{'job': 'Instructor', 'name': 'Elie'}` (the order does not matter)
2. Given two lists `["CA", "NJ", "RI"]` and `["California", "New Jersey", "Rhode Island"]` return a dictionary that looks like this `{'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}`. You can research the `zip` method to help you.
3. Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this `{'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}`. (Do not use the `fromkeys` method).
4. Create a dictionary starting with the key of the position of the letter and the value as the letter in the alphabet. You should return something like this (hint - use `chr(65)` to get the first letter):

```py
{1: 'A',
 2: 'B',
 3: 'C',
 4: 'D',
 5: 'E',
 6: 'F',
 7: 'G',
 8: 'H',
 9: 'I',
 10: 'J',
 11: 'K',
 12: 'L',
 13: 'M',
 14: 'N',
 15: 'O',
 16: 'P',
 17: 'Q',
 18: 'R',
 19: 'S',
 20: 'T',
 21: 'U',
 22: 'V',
 23: 'W',
 24: 'X',
 25: 'Y',
 26: 'Z'}
```

### Super Bonus

Given the string "awesome sauce" return a dictionary with the keys as vowels and the values as the count of vowels. Your dictionary should look like `{'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}`

