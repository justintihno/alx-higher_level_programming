# 0x13. JavaScript - Objects, Scopes and Closures
#### JavaScript

## Concepts
* JavaScript object basics
* Object-oriented JavaScript (read all examples!)
* Class - ES6
* super - ES6
* extends - ES6
* Object prototypes
* Inheritance in JavaScript
* Closures
* this/self
* Modern JS

### Objectives
* Why JavaScript programming is amazing
* How to create an object in JavaScript
* What this means
* What undefined means
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

## Requirements
* Editors: vi, vim, emacs
* Files interpreted on Ubuntu 20.04 LTS using node (version 14.x)
* Code is semistandard compliant. Rules of Standard + semicolons on top.
* The length of your files will be tested using wc
* Var not used

### More Info
* Install Node 14
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

* Install semi-standard

[Documentation](https://github.com/standard/semistandard)

$ sudo npm install semistandard --global

## Tasks
Files | Description
----- | -----------
[0-rectangle.js](./0-rectangle.js) | JS script that defines an empty class Rectangle
[1-rectangle.js](./1-rectangle.js) | JS script that defines a rectangle
					* Class notation used for defining class
					* The constructor must take 2 arguments, attr width  w and attr height h
[2-rectangle.js](./2-rectangle.js) | JS script that defines a rectangle:

* You must use the class notation for defining your class
* The constructor must take 2 arguments w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object
[3-rectangle.js](./3-rectangle.js) | JS script that defines a rectangle:

* You must use the class notation for defining your class
* The constructor must take 2 arguments: w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object
* Create an instance method called print() that prints the rectangle using the character X
[4-rectangle.js](./4-rectangle.js) | JS script that defines a rectangle:

* You must use the class notation for defining your class
* The constructor must take 2 arguments: w and h
* Initialize the instance attribute width with the value of w
* Initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object
* Create an instance method called print() that prints the rectangle using the character X
* Create an instance method called rotate() that exchanges the width and the height of the rectangle
* Create an instance method called double() that multiples the width and the height of the rectangle by 2
[5-square.js](./5-square.js) | JS script that defines a square and inherits from Rectangle of [4-rectangle.js](./4-rectangle.js)

* You must use the class notation for defining your class and extends
* The constructor must take 1 argument: size
* The constructor of Rectangle must be called (by using super())

[6-square.js](./6-square.js) | JS script that defines a square and inherits from Square of [5-square.js](./5-square.js)

* You must use the class notation for defining your class and extends
* Create an instance method called charPrint(c) that prints the rectangle using the character c
* If c is undefined, use the character X

[7-occurrences.js](./7-occurrences.js) | JS script that returns the number of occurrences in a list:

* Prototype: exports.nbOccurences = function (list, searchElement)

[8-esrever.js](./8-esrever.js) | JS script that returns the reversed version of a list:

* Prototype: exports.esrever = function (list)
* You are not allow to use the built-in method reverse

[9-logme.js](./9-logme.js) | JS script that prints the number of arguments already printed and the new argument value

* Prototype: exports.logMe = function (item)
* Output format: <number arguments already printed>: <current argument value>

[10-converter.js](./10-converter.js) | JS script that converts a number from base 10 to another base passed as argument:

* Prototype: exports.converter = function (base)
* You are not allowed to import any file
* You are not allowed to declare any new variable (var, let, etc..)

[100-map.js](./100-map.js) | JS script that imports an array and computes a new array.

* Your script must import list from the file [100-data.js](./100-data.js)
* You must use a map. [Tips](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=control)
* A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
* Print both the initial list and the new list

[101-sorted.js](./101-sorted.js) | JS script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

* Your script must import dict from the file [101-data.js](./101-data.js)
* In the new dictionary:
	* A key is a number of occurrences
	* A value is the list of user ids
* Print the new dictionary at the end

[102-concat.js](./102-concat.js) | JS script that concats 2 files.

* The first argument is the file path of the first source file
* The second argument is the file path of the second source file
* The third argument is the file path of the destination


## AUTHOR
Tihno
