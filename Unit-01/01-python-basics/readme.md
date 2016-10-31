# Python Basics

### Python vs. JavaScript

Complete the exercises below by writing an expression in JavaScript and one in Python that complete the same task. The first example has been done for you. Feel free to consult the docs for these languages if you get stuck!

1. Declare a variable called `first` and assign it to the value `"Hello World"`.

	```js
	var first = "Hello World";
	```
	
	```py
	first = "Hello World"
	```

2. Write a comment that says "This is a comment."

	```js
	// This is a comment.
	```
	
	```py
	# This is a comment.
	```
	
3. Show a message to the console / terminal that says "I AM A COMPUTER!"

	```js
	console.log("I AM A COMPUTER!");
	```
	
	```py
	print("I AM A COMPUTER!")
	```
	
4. Write an if statement that checks if `1` is less than `2` and if `4` is greater than `2`. If it is, show the message "Math is fun."

	```js
	if(1<2 && 4>2){
		console.log("Math is fun.");
	}

	```
	
	```py
	if 1<2 and 4>2:
		print("Math is fun")
	```
	
5. Assign a variable called `nope` to an absence of value.

	```js
	var nope = null;
	```
	
	```py
	nope = None
	```
	
6. Use the language's "and" boolean operator to combine the language's "true" value with its "false" value.

	```js
	true && false;
	```
	
	```py
	True and False
	```
	
7. Calculate the length of the string "What's my length?"

	```js
	"hello".length;
	
	```
	
	```py
	len("hello")
	```
	
8. Convert the string "i am shouting" to uppercase.

	```js
	"i am shouting".toUpperCase();
	```
	
	```py
	"i am shouting".upper()
	```
	
9. Convert the string `"1000"` to the number `1000`.

	```js
	Number("1000");
	```
	
	```py
	int("1000")
	```
	
10. Combine the number `4` with the string `"real"` to produce `"4real"`.

	```js
	4+"real";
	```
	
	```py
	str(4)+"real"
	```
	
11. Record the output of the expression `3 * "cool"`.

	```js
	NaN
	```
	
	```py
	"coolcoolcool"
	```
	
12. Record the output of the expression `1 / 0`.

	```js
	Infinity
	```
	
	```py
	ZeroDivisionError: division by zero
	```
	
13. Determine the type of `[]`. 

	```js
	object
	```
	
	```py
	<class 'list'>
	```
	
14. Ask the user for their name, and store it in a variable called `name`.

	```js
	var name = prompt("Enter your name");
	```
	
	```py
	name = input("Enter your name")
	```
	
15. Ask the user for a number. If the number is negative, show a message that says `"That number is less than 0!"` If the number is positive, show a message that says `"That number is greater than 0!"` Otherwise, show a message that says `"You picked 0!`.

	```js
	var number = prompt("Enter a number");
	if(number<0){
		console.log("That number is less than 0!");
	} else if (number>0) {
		console.log("That number is greater than 0!");
	} else if(number == 0){
		console.log("You picked 0!");
	}
	```
	
	```py
	number = int(input("Enter a number"))
	if number<0:
		print("That number is less than 0!")
	elif number>0:
		print("That number is greater than 0!")
	elif number == 0:
		print("You picked 0!")
	```
	
16. Find the index of `"l"` in `"apple"`.

	```js
	"apple".indexOf("l");
	```
	
	```py
	"apple".find("l")
	```
	
17. Check whether `"y"` is in `"xylophone"`.

	```js
	if("xylophone".indexOf("y")!== -1){
		console.log("present");
	}

	```
	
	```py
	if "xylophone".find("y") != -1:
		print("present")
	```
	
18. Check whether a string called `str` is all in lowercase.

	```js
	if(str === str.toLowerCase()){
		console.log("str is all lowercase");
	}
	```
	
	```py
	if str == str.lower():
		print("str is all lowercase")
	```
	
19. Create two variables, `nums1` and `nums2`. Both should store an array / list of the values [1, 2, 3]. Check whether `nums1` and `nums2` refer to the same object.

	```js
	var nums1 = [1,2,3];
	var nums2 = [1,2,3];
	nums1 === nums2 // false, not the same object
	```
	
	```py
	nums1 = [1,2,3]
	nums2 = [1,2,3]
	print(nums1 is nums2) # false, not the same object
	```
	
20. Create two variables, `nums1` and `nums2`. Both should store an array / list of the values [1, 2, 3]. Check whether `nums1` and `nums2` have the same values.

	```js
	var nums1 = [1,2,3];
	var nums2 = [1,2,3];
	var theSame = true;
	nums1.forEach(function(arrayItem,idx){
		if(arrayItem!==nums2[idx]){
			theSame = false;
		}
	})
	console.log(theSame);
	```
	
	```py
	nums1 = [1,2,3]
	nums2 = [1,2,3]
	if nums1 == nums2:
		print("they are the same")
	```
