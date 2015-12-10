"""
Routes and views for the flask application.
""" 
from __future__ import print_function
from datetime import datetime
from flask import render_template
from FlaskWebProject10 import app

import pymysql
from geopy.geocoders import Nominatim
from geopy.geocoders import GeocoderDotUS


connection = pymysql.connect(host='localhost', user='root', passwd='ajqdatabase', db='njdb',charset='utf8', cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.',
    )

@app.route('/charts')
def charts():
    """Pull RANK NUMBERS DATA"""
    try:
        rank_numbers = connection.cursor()
        # Read from cases
        rank_numbers.execute("select `njdb`.`ranks`.`rank_name` AS `rank_name`,`njdb`.`ranks`.`rank_id` AS `rank_id`,count(`njdb`.`polices`.`p_id`) AS `NumberOfficers` from (`njdb`.`ranks` join `njdb`.`polices` on((`njdb`.`ranks`.`rank_id` = `njdb`.`polices`.`rank_id`))) group by `njdb`.`ranks`.`rank_name`,`njdb`.`ranks`.`rank_id`")
        rank_number = rank_numbers.fetchall()
    finally:
        rank_numbers.close()

    """Renders the contact page."""
    return render_template(
        'charts.html',
        title='Charts',
        year=datetime.now().year,
        message='Your chart page.',
        rank_number = rank_number
    )

@app.route('/maps')
def maps():
    """Pull RANK NUMBERS DATA"""
    try:
        map_data = connection.cursor()
        # Read from cases
        map_data.execute("select `njdb`.`locations`.`loc_id` AS `loc_id`,`njdb`.`locations`.`city` AS `city`,`njdb`.`locations`.`zip` AS `zip`,`njdb`.`crimes`.`c_type` AS `c_type` from (((`njdb`.`crimes` join `njdb`.`incidents` on((`njdb`.`crimes`.`crime_id` = `njdb`.`incidents`.`crime_id`))) join `njdb`.`polices` on((`njdb`.`incidents`.`p_id` = `njdb`.`polices`.`p_id`))) join `njdb`.`locations` on((`njdb`.`polices`.`loc_id` = `njdb`.`locations`.`loc_id`)))")
        mapping_data = map_data.fetchall()
    finally:
        map_data.close()

    #myziptemp = []
    #mylat = []
    #mylon = []

    #for i in mapping_data:
    #    myziptemp.append(i['city'])

    #geolocator = Nominatim()
    #for i in range(len(myziptemp)):
    #    location = geolocator.geocode(myziptemp[i] + ",nj")
    #    print(location)
    #    #mylat.append(location.latitude)


    #print(mylat)


    #for x in myziptemp:
     #   myzip = zipcode.isequal(x)

    #print(myzip)
    #print(mapping_data.zip)
    #lat = myzip.lat
    #lon = myzip.lon

    #print(lon)
    #print(lat)

    """Renders the MAPS page."""
    return render_template(
        'maps.html',
        title='Maps',
        year=datetime.now().year,
        message='Your application description page.',
        mapping_data = mapping_data,
        #lat = lat,
        #lon = lon
        )

@app.route('/dataTables')
def dataTables():
    """Pull CASES DATA"""
    try:
        case = connection.cursor()
        # Read from cases
        case.execute("SELECT * FROM `cases`")
        cases = case.fetchall()
    finally:
        case.close()

    """Pull LOCATION DATA"""
    try:
        location = connection.cursor()
        # Read from cases
        location.execute("SELECT * FROM `locations`")
        locations = location.fetchall()
    finally:
        location.close()

     
      

    return render_template(
        'data-tables.html',
        title='DataTables',
        year=datetime.now().year,
        message='Your application dataTables page.',
        locations = locations,
        cases = cases,
        )
