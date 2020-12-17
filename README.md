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
HTML, which stands for **HyperText Markup Language**, is the most basic building block for the content on a webpage. HTML uses markup to annotate pieces of content (such as text, links, images) for the purpose of defining the meaning/structure of that content to a web browser. This markup is composed of a defined set of "elements" which may or may receive additional "attributes".

`<p>` is a paragraph element used to annotate body text. It typically does not receive attributes besides `class` or `id` for styling purposes.

```html
<p>Some text!<p>
```

`<a>` is an anchor element and is typically used to markup links on a web page. It recieves an `href` attribute with a reference to some url.

```html
<a href="www.google.com">Let me google that for you!</a>
```

You can read more about other HTML elements [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

### Accessibility
It's important to use elements correctly for the purpose of web accessibility: use `<section>` to define sections on a webpage, `<nav>` to highlight navigation links, and `<h>` to highlight heading text. This makes it easier for assistive technology to parse your page. It also optimizes your SEO!


<hr>
</details><br>





# Templating

<details><summary>💡 What is templating?</summary>
<hr>

### Templating
Templating allows us to break up HTML in smaller and reusable pieces that we can then inject data into. Take a look at the pages for [Princess Diana](https://en.wikipedia.org/wiki/Diana,_Princess_of_Wales) and [Princess Margaret](https://en.wikipedia.org/wiki/Princess_Margaret,_Countess_of_Snowdon) on Wikipedia and note of how similar they are! Do you think engineers at Wikipedia just copy-and-paste a bunch of HTML from other similar Wikipedia entries? No way! They use templates and load them with the appropriate data.

This has a couple of benefits:
- It makes it easier to add content to Wikipedia because maintainers don't need to add new HTML every time.
- If someone decides Wikipedia needs to revamped, styles only have to be changed on the template and not the millions of individual entries.


### Jinja
Flask is built on top of Jinja, a templating engine that allows us to serve HTML templates and optionally any data they need. Jinja uses its own markup language to denote variables and expressions where templates and data will later be loaded.

For example, `{% block <block_name> %}{% endblock %}` is used on one template to designate a block that another template will later fill. The other template then extends the first template and reuses the same markup syntax to highlight the exact block that will take up that space. Check out `app/templates/layout.html` and `app/templates/tasks.html` to see this in action. `layout.html` renders a sidebar and defines a block for content; `tasks.html` renders some content that will go in that block. If you navigate to `localhost:5000/tasks`, you'll see that the HTML from these templates is combined! You can even inspect the HTML on your browser if you right click and select "Inspect."

Some more useful Jinja syntax:
- You can loop over lists passed to your template, `{% for task in tasks %} ... {% endfor %}` to loop over a list `tasks`
- You can directly reference data in your template: `{{ task.name }}` to print the value for `task.name`

Check out more Jinja syntax [here](https://jinja.palletsprojects.com/en/2.11.x/templates/#synopsis) or use the prewritten examples in your repo to guide you!


### `render_template()`
To render a template, we use the `render_template()` method from Flask and return a chosen template and optionally any data it needs. For example:

```py
@app.route('/', methods=['GET'])
def get_home():
    return render_template('home.html')
```

```py
@app.route('/tasks', methods=['GET'])
def all_tasks():
    data = Task.query.all()
    all_tasks = [item.serialize() for item in data]
    return render_template('tasks.html', tasks=all_tasks) <-- the key here is the variable name you can use in your template
```

Read more about this method [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates).

<hr>
</details><br>


### 🖥 Review files
1. `app/app.py`<br>
This is where the basic boilerplate for your app is set up. As mentioned above, the boilerplate for SQlAlchemy is slightly different than what we wrote last week when we used SQLAlchemy on its own. The URI for your database is stored as a configuration attribute on the `app` object. On line 8, we run the `SQLAlchemy` function with `app` passed in to instantiate an database object that acts as both our enginer, sessionmaker, and declarative base. Confirm that the URI on line 6 correctly points to your database. **You might need to supply a username and password:** `postgres+psycopg2://<USERNAME>:<PASSWORD>@localhost:5432/todo`<br>
On line 13, we invoke the `run` method on `app` to start our development server. If you run this file (`python app/app.py)`, you'll see some feedback in your terminal saying you are now running a local server on port 5000. You can now access this web app or its endpoints at http://localhost:5000/.
2. `app/models.py`<br>
Your models are defined by `app/models.py`. You'll notice that all of the table definitons extend `db.Model` as do any Flask-SQLAlchemy helpers, like `Column` or `String` or `Integer`. You might also notice that each model definition has a `serialize` mehtod in order to return data about our models in JSON. In the future, we might want to utilize a Python package that handles serialization for us.
3. `app/db.py`<br>
Our tables are created and seeded in this file. If you run this file (`python app/db.py`), you'll see some feedback in your terminal and then be able to see changes to your database using `psql` or your chosen GUI.
4. `app/api.py`<br>
You'll notice we already got started rendering some templates in the `/tasks` routes. You can find the corresponding templates in the `/app/templates` directory.
<br>





### 🖥 Let's add more HTML to our template in `tasks.html`
In `app/templates/tasks.html`, write some more HTML to render this additional information about your task:
- the task name
- the task description
- the project associated with that task
- the person assigned to that task

If you're having trouble figuring out how to reference this data, check out the `serialize` methods in `app/models.py`.

After you have done that, try converting the task name into a link that directs you to a page showing only that task.
<br>
<details><summary>Click here for the solution.</summary>
<hr>
  
```html
                <h5>
                    <a href="/tasks/{{task.id}}">
                        {{ task.name }}
                    </a>
                </h5>
                <p>{{ task.description }}</p>
                <p>Project: {{ task.project }}</p>
                <p>Assignee: {{ task.person }}</p>

```

<hr>
</details>
<br>





### 🖥 Let's create a new template in `projects.html` and render it from our `/projects` routes
If you click "All Projects" in the sidebar links, you're taken to a page displaying JSON data. Let's display this data within a template instead. There's a template already set up in `app/templates/projects.html`. Use the `render_template()` method inside the projects routes to render the correct template and data. Then write some HTML to render more data in `app/templates/projects.html`
<br>
<details><summary>Click here for the solution.</summary>
<hr>
 
```py
@app.route('/projects', methods=['GET'])
def all_projects():
    data = Project.query.all()
    all_projects = [item.serialize() for item in data]
    return render_template('projects.html', projects=all_projects)


@app.route('/projects/<int:project_id>', methods=['GET'])
def get_one_project(project_id):
    data = Project.query.get(project_id)
    one_project = data.serialize()
    return render_template('projects.html', projects=[one_project]) <- BONUS: why is this passed as a list?

```

```html
    {% for project in projects %}
        <div class="projects_card">
            <h5>
                <a href="/projects/{{project.id}}">
                    {{ project.name }}
                </a>
            </h5>
            <h5>Tasks:</h5>
            {% for task in project.tasks %}
                <ul>
                    <li>
                        <a href="/tasks/{{task.id}}">
                            {{ task.name }}
                        </a>
                    </li>
                </ul>
            {% endfor %}
        </div>
    {% endfor %}
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


# 🚨 Your CSS is being cached. `Ctrl+Shift+R` or `Cmd+Shift+R` to hard refresh and reload new CSS from the server. Otherwise, you will not see your changes!


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
