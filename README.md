# flask_db_select

*Updated April 11, 2023* for SQLAlchemy 2.0

*Updated April 15, 2023* for deployment at Render.com

[Live app here.](https://flask-sockmarket.onrender.com/)

## The select drop-down

See:

[Building a select menu in a form](https://bit.ly/mm-flask-select)

Sometimes you want to populate a drop-down menu as a means of selecting one record from your database. This can be a bit puzzling to figure out in combination with using Flask-WTF and Bootstrap-Flask and Flask-SQLAlchemy all together.

This is the simplest, most basic interface I could think of &mdash; it helps a lot if you take the time to understand how an HTML `<select>` element works.

How to use forms in Flask — [Flask: Web Forms](https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html)

## Deployment notes

This repo is the exact repo that has been successfully deployed at Render.com.

Instructions: [Deploy a Flask App to Render.com](https://bit.ly/mm-render-flask)

**Bootstrap5 error:** To get Bootstrap-Flask to work properly on the cloud server, you must edit your *requirements.txt* file after you generate it. Delete only one line from that file:

`Flask-Bootstrap4==4.0.2`

This is necessary because Bootstrap-Flask will install that on its own, and having the line already in the *requirements.txt* file creates a conflict that will prevent your app from deploying (*April 15, 2023*).

**Environment variable:** This app connects to a MySQL database on another server, using a connection string specific to that database. Never write your connection string into the code that you post to GitHub — it includes your username and password! Store the connection string in an environment variable. Test this first on your local computer to be sure that it works. See: [Set environment variable on MacOS](https://bit.ly/mm-env-variable).

**Enable database connections from Render.com:** On the server where the database resides, you will need to use the **Remote MySQL** feature to allow another server to make requests from the database. You do this by entering the IP address(es) from which the requests will come. The app is on Render.com, so you need to get the IP addresses from there.

## Using a MySQL database with Flask

See: [Using a MySQL database with Flask](http://bit.ly/mm-remote-mysql ).

**Adding the IP addresses:** See the last page of that document for instructions on how to find the IP addresses for your app at Render.com. 

.
