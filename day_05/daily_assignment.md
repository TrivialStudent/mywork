# Lesson: Reading Data Files in Python

## Objective
- Learn how to read data from a file in Python.
- Practice modular programming by writing functions.
- Use the `random` module to select items from a file.

---

## 1. Introduction

Have you ever wanted your program to have *dynamic content*, like random movie quotes? Instead of typing each quote in your code, we can store them in a **file** and read them in.

Example file: `quotes.txt` which is located in this directory.

---

## 2. Reading a File

### Basic File Reading

Python makes it simple to read a file:

```python
# Open a file and read all lines
file = open("quotes.txt", "r")
lines = file.readlines()  # reads every line into a list
file.close()

print(lines)
```
### Notes
* `"r"` means that is is only set to read the document
* `readlines()` returns a ***list*** with each line from the document as a string
* Don't forget to close the file to free resources.

### Recommended File Reading

```python
with open("quotes.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

### Notes
* `with` automatically closes the file when done with commands. Safer and cleaner way of programming with files.

---
## 3. Writing to a File

### Objective
* Learn how to write to files in python
* Practice appending, saving, and organizing data
* Extend programs to be more interactive

```python
# Open a file as a writeable file.
with open("favorite_quotes.txt", "w")
    file.write("This is just a test")
```

### Notes
* `"w"` creates the file or overwrites it if it already exists.
* `"a"` creates the file or appends new content at the end if the file exists.
* `"x"` will only ever create a new file. If the file exists already, it will raise an error.
* ***Don't forget to close the file if you are not using the `with` feature.***

# Assignment
* Objective: In the file `random_quote_generator.py`, read lines from `quotes.txt` use the random `package` to generate random quotes for a user.
    * Create a function load_quotes()
        * *Parameter: file_name_1.txt* 
        * *Return Value: List of quotes from file_name_1.txt*
    * Create a function get_random_quote()
        * *Parameter: list of quotes*
        * *Return Value: random quote string*
    * Create a function add_to_favorites()
        * *Parameter: file_name_2.txt and random_quote*
        * *Doesn't have a return value, but should create a new file and add quotes if user chooses quote as a favorite.  
    * Create a function view_favorites()
        * *Parameter: file_name_2*
        * *Return Value: List of quotes from file_name_2.txt*

    * Challenge: Create a new file called  `authors.txt` with the authors of each quote on the same line number as the quote.  
    Modify your code to print `"Quote" - Author`

### Tips and Hints
* Always use `.strip()` to remove `\n` from lines. (new line markers)
* Test your functions independently.