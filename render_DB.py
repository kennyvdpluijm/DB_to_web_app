from flask import Flask, render_template, request, redirect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table
import urllib
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "yourKey"


def date(d):
    d = datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
    d.strftime("%d-%m-%y %H:%M:%S")
    return d


app.add_template_filter(date)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("mainpage.html")


@app.route("/locationwest", methods=["GET", "POST"])
def location_west():
    connection_string = (
        'Driver=;'
        'Server=;'
        'Database=;'
        'UID=;'
        'PWD=;'
        'Trusted_Connection=;')
    connection_uri = F"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
    engine = create_engine(connection_uri)
    table1meta = MetaData(engine)
    table1 = Table('yourDB', table1meta, autoload=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    results = session.query(table1).filter(table1.c.Location == 'West').order_by(table1.c.Completed_job.desc())
    return render_template("locationwest.html", items=results.all())


@app.route("/locationnord", methods=["GET", "POST"])
def location_west():
    connection_string = (
        'Driver=;'
        'Server=;'
        'Database=;'
        'UID=;'
        'PWD=;'
        'Trusted_Connection=;')
    connection_uri = F"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
    engine = create_engine(connection_uri)
    table1meta = MetaData(engine)
    table1 = Table('yourDB', table1meta, autoload=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    results = session.query(table1).filter(table1.c.Location == 'Nord').order_by(table1.c.Completed_job.desc())
    return render_template("locationnord.html", items=results.all())


@app.route("/searchref", methods=["GET", "POST"])
def search_reference():
    if request.method == "POST":
        form = request.form
        search_value = form['search_integer_ref']
        search_input = "%{}%".format(search_value)
        connection_string = (
            'Driver=;'
            'Server=;'
            'Database=;'
            'UID=;'
            'PWD=;'
            'Trusted_Connection=;')
        connection_uri = F"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
        engine = create_engine(connection_uri)
        table1meta = MetaData(engine)
        table1 = Table('yourDB', table1meta, autoload=True)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        results = session.query(table1).filter(table1.c.Reference.like(search_input)).order_by(table1.c.Completed_job.desc())
        return render_template("searchref.html", items=results, pageTitle="Search reference", legend="Search results")
    else:
        return redirect('/')


@app.route("/searchobject", methods=["GET", "POST"])
def search_object():
    if request.method == "POST":
        form = request.form
        search_value = form['search_integer_object']
        search_input = "%{}%".format(search_value)
        connection_string = (
            'Driver=;'
            'Server=;'
            'Database=;'
            'UID=;'
            'PWD=1;'
            'Trusted_Connection=;')
        connection_uri = F"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
        engine = create_engine(connection_uri)
        table1meta = MetaData(engine)
        table1 = Table('yourDB', table1meta, autoload=True)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        results = session.query(table1).filter(table1.c.Object.like(search_input)).order_by(table1.c.Completed_job.desc())
        return render_template("searchobject.html", items=results, pageTitle="Search object", legend="Search results")
    else:
        return redirect('/')


@app.route("/searchproduct", methods=["GET", "POST"])
def search_product():
    if request.method == "POST":
        form = request.form
        search_value = form['search_string_product']
        search_input = "%{}%".format(search_value)
        connection_string = (
            'Driver=;'
            'Server=;'
            'Database=;'
            'UID=;'
            'PWD=;'
            'Trusted_Connection=;')
        connection_uri = F"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
        engine = create_engine(connection_uri)
        table1meta = MetaData(engine)
        table1 = Table('yourDB', table1meta, autoload=True)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        results = session.query(table1).filter(table1.c.Product.like(search_input)).order_by(table1.c.Completed_job.desc())
        return render_template("searchproduct.html", items=results, pageTitle="Search product", legend="Search results")
    else:
        return redirect('/')


@app.route("/searchdate", methods=["GET", "POST"])
def search_date():
    if request.method == "POST":
        form = request.form
        search_value = form['search_string_date']
        search_input = "%{}%".format(search_value)
        connection_string = (
            'Driver=;'
            'Server=;'
            'Database=;'
            'UID=;'
            'PWD=;'
            'Trusted_Connection=;')
        connection_uri = F"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
        engine = create_engine(connection_uri)
        table1meta = MetaData(engine)
        table1 = Table('yourDB', table1meta, autoload=True)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        results = session.query(table1).filter(table1.c.Commenced_job.like(search_input)).order_by(table1.c.Completed_job.desc())
        return render_template("searchdate.html", items=results, pageTitle="Search date", legend="Search results")
    else:
        return redirect('/')


if __name__ == "__main__": app.run(host="yourIP")
