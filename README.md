# the \<wit\> project workshop: "flask & sql-alchemy"


_Anytime you see a 🖥, follow the instructions below. Anytime you see a 💡, click the toggles to find more information._
<br><br>


### 🖥 Install this project locally
1. Clone this repo: `git clone <this repo's remote url>`
2. Change directories: `cd workshop_flask_sqlalchemy`
3. Create a virtual environment for this project and activate it:
```
mkdir env
python3 -m venv env
source env/bin/activate
```
4. Install the requirements: `pip install -r requirements.txt`
5. If you haven't done so already, create a database named `todo`
6. Run `python app/db.py` to create and seed your database tables
7. Run the application as needed: `python app/app.py`
<br>





# HTML

<details><summary>💡 What is HTML?</summary>
<hr>

### HTML


### Accessibility


<hr>
</details><br>





# Templating

<details><summary>💡 What is templating?</summary>
<hr>

### Templating


### Jinja


### `render_template()`


<hr>
</details><br>


### 🖥 Review files
1. `app/app.py`<br>
This is where the basic boilerplate for your app is set up. As mentioned above, the boilerplate for SQlAlchemy is slightly different than what we wrote last week when we used SQLAlchemy on its own. The URI for your database is stored as a configuration attribute on the `app` object. On line 8, we run the `SQLAlchemy` function with `app` passed in to instantiate an database object that acts as both our enginer, sessionmaker, and declarative base. Confirm that the URI on line 6 correctly points to your database.<br>
On line 13, we invoke the `run` method on `app` to start our development server. If you run this file (`python app/app.py)`, you'll see some feedback in your terminal saying you are now running a local server on port 5000. You can now access this web app or its endpoints at http://localhost:5000/.
2. `app/models.py`<br>
Your models are defined by `app/models.py`. You'll notice that all of the table definitons extend `db.Model` as do any Flask-SQLAlchemy helpers, like `Column` or `String` or `Integer`. You might also notice that each model definition has a `serialize` mehtod in order to return data about our models in JSON. In the future, we might want to utilize a Python package that handles serialization for us.
3. `app/db.py`<br>
Our tables are created and seeded in this file. If you run this file (`python app/db.py`), you'll see some feedback in your terminal and then be able to see changes to your database using `psql` or your chosen GUI.
<br>





### 🖥 Let's add more HTML to our template in `tasks.html`
In `app/api.py`, write a simple route to get all tasks from your database. You can use the `Task.query.all()` method. When you are done, test your route by sending a `GET` request to `localhost:5000/tasks` in Postman.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py

```

<hr>
</details>
<br>





### 🖥 Let's create a new template in `projects.html` and render it from our `/projects` routes
In `app/api.py`, write a simple route to get all tasks from your database. You can use the `Task.query.all()` method. When you are done, test your route by sending a `GET` request to `localhost:5000/tasks` in Postman.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py

```

<hr>
</details>
<br>




# CSS

<details><summary>💡 What is CSS?</summary>
<hr>

### CSS


### CSS Flex


### CSS Grid


### CSS Media Queries


<hr>
</details><br>


### 🖥 Let's use CSS Grid to style `layout.html`
In `app/api.py`, write a simple route to get all tasks from your database. You can use the `Task.query.all()` method. When you are done, test your route by sending a `GET` request to `localhost:5000/tasks` in Postman.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py

```

<hr>
</details>
<br>


### 🖥 Let's use media queries to style `layout.html` for phone browsers
In `app/api.py`, write a simple route to get all tasks from your database. You can use the `Task.query.all()` method. When you are done, test your route by sending a `GET` request to `localhost:5000/tasks` in Postman.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py

```

<hr>
</details>
<br>


### 🖥 Let's use CSS Flex to style `tasks.html`
In `app/api.py`, write a simple route to get all tasks from your database. You can use the `Task.query.all()` method. When you are done, test your route by sending a `GET` request to `localhost:5000/tasks` in Postman.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py

```

<hr>
</details>
<br>





# Styling Libraries

<details><summary>💡 What is a styling library?</summary>
<hr>

### Styling Libraries


### Bootstrap


<hr>
</details><br>


### 🖥 Let's enable Bootstrap for our project
In `app/api.py`, write a simple route to get all tasks from your database. You can use the `Task.query.all()` method. When you are done, test your route by sending a `GET` request to `localhost:5000/tasks` in Postman.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```py

```

<hr>
</details>
<br>





# That's it! You did it! Great job! 👏
Feel free to make your project yours by adding more styles! You can do it on your own or use Bootsrap to assist you!
