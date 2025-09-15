# Introduction to HTML for Kids

HTML (HyperText Markup Language) is what we use to make web pages. Think of it like building blocks for a website.

---

## 1. Basic Structure

Every HTML page starts like this:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My First Webpage</title>
  </head>
  <body>
    <!-- Content goes here -->
  </body>
</html>
```

**Explanation**
* `<!DOCTYPE html>` tells the browser this is an HTML page.
* `<html>` is the root of the page.
* `<title>` sets the name in the browser tab.
* `<body>` is where visible content goes.

## 2. Headers
```html
<h1>Big Header</h1>
<h2>Smaller Header</h2>
<h3>Even Smaller Header</h3>
```

## 3. Paragraphs
```html
<p>This is a paragraph.</p>
<p>Another paragraph with more text.</p>
```

## 4. Forms
```html
<form>
  <label for="name">Name:</label>
  <input type="text" id="name" name="name"><br><br>

  <label for="age">Age:</label>
  <input type="number" id="age" name="age"><br><br>

  <input type="submit" value="Submit">
</form>
```
**Explanation**
* `<form>` holds the inputs.
* `<label>` shows what to enter.
* `<input>` is where users type.
* `<input type="submit">` makes a button to submit.