"""
using a MySQL database here, not SQLite
updated and tested April 2023 for SQLAlchemy 2.0
"""
import pymysql
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SelectField, SubmitField
from flask_bootstrap import Bootstrap5


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=4999, debug=True)
