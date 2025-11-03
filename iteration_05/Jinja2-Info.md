# Jinja2

## Definition
* Text Based Templating System
* Populate and render a template using:
  * Variable replacement
  * Tags
    * conditionals
    * loops
    * inheritance / inclusion
    * macros
  * Filters
    * Modify variable data on the fly

## Setup for Jinja2
* First create your directory folder for your flask app
* Setup virtual environment for flask and jinja2 install (Steps Below)
```python
python3 -m venv venv
source venv/bin/activate
pip3 install flask jinja2
```

## Blocks 
* Blocks are utilized as spaceholders for content to be substituted in when extending a base template  

`base.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>
        {% block title %}Flask UI{% endblock %}
    </title>
</head>
<body>
    {% block content %} {% endblock %}
</body>
</html>
```

`home.html`
```html
{% extends 'base.html' %}
{% block title %} Home {% endblock %}
{% block content %}
<h1>Welcome to the Flask UI App!</h1>
{% endblock %}
```

## Variables and Logic

* We can pass variables into the `render_template( )` function and allow usage of python variables and logic inside of our html code.
* Here is a simple route example which takes in an author, a list of tools, and a boolean variable.

`app.py`

```python
@app.route("/tools_used")
def tools_used():
    tools = ["Flask", "Python", "HTML", "Jinja2"]
    return render_template("tools_used.html", author="Kevin Santos", tools=tools, is_student = False)
```

* In our template, we can see that any Jinja2 logic will need to be done in a `{%       %}` container. For example, when we extend a template, when we start or end a new block, and also conditionals like 'if' statements or 'for' loops.
* In any instances where we want to use a variable directly, whether or not we are inside of a logic container, we need to use `{{    }}`. Examples can be seen below.

`tools_used.html`  

```html
{% extends 'base.html' %}
{% block title %}About{% endblock %}
{% block content %}
<h2>About This App</h2>
<p>Created by {{ author }}</p>

{% if is_student %}
<p>This site was built by students learning Flask!</p>
{% else %}
<p>This site was built by teachers.</p>
{% endif %}

<ul>
    {% for tool in tools %}
        <li>{{ tool }}</li>
    {% endfor %}
</ul>
{% endblock %}
```


## Assignment (Homework if not completed by end of class)

1. **Complete About Page (`about.html`)**
   - Must extend `base.html` using `{% extends 'base.html' %}`.
   - Include your name and a short paragraph describing:
     - Who you are, and
     - What interests you about programming or technology.
   - Use at least **one variable** passed from your Flask route (for example, your name or favorite programming language).
   - Include at least one **Jinja2 conditional** (`{% if ... %}`) or **loop** (`{% for ... %}`).

2. **Complete Contact Page (`contact.html`)**
   - Must also extend `base.html`.
   - Display at least **two contact methods** (for example: email, GitHub, or social media handles).
   - Use a **variable** or **dictionary** passed from Flask to show your contact details.
   - Include a conditional that displays a message if one piece of info is missing (e.g., “Phone number not available”).

---

### Submission Guidelines

1. Save your work in your project folder.
2. Make sure your Flask app runs without errors.
3. Check that all links in your navigation bar work.
4. If you do not finish in class, this becomes homework due by beginning of next class.