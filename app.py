import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measure = Base.classes.measurement
Station= Base.classes.station

session = Session(engine)

# query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
# # print("Query Date: ", query_date)

# date = dt.datetime(2016,8,23)
# # Calculate the date 1 year ago from the last data point in the database

# # Perform a query to retrieve the data and precipitation scores

# results=session.query(Measure.tobs,Measure.date,Measure.id, Measure.prcp,Measure.station).\
                        # filter(Measure.date > date).order_by(Measure.date).all()


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available API calls:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/date<br/>"
        
        
    )


@app.route("/api/v1.0/precipitation")
def DatePecp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates and prcp"""
    # Query all dates and prcp

    results = session.query(Measure.date,Measure.prcp).all()

    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value.
    precip=[]
    for date, prcp in results:
        one_result={date:prcp}
        precip.append(one_result)

    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates and prcp"""
    # Query all dates and prcp

    results1 = session.query(Measure.station).distinct()

    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value.
    stat=[]
    for station in results1:
        one_result=[station]
        stat.append(station)

    return jsonify(stat)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates and prcp"""
    # Query all dates and prcp

    results2 = session.query(Measure.station,Measure.date,Measure.tobs).\
        filter(Measure.station == 'USC00513117').\
        filter(Measure.date > '2016-8-23').all() 

    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value.
    stat_temp=[]
    for each_row in results2:
        one_result={}
        one_result['station']= each_row[0]
        one_result['date']=each_row[1]
        one_result['tobs']=each_row[2]
        stat_temp.append(one_result)

    return jsonify(stat_temp)


@app.route("/api/v1.0/date/<start>")
@app.route("/api/v1.0/date/<start>/<end>")
def star_date(start=None, end=None):
    # print(f'start={start}')#test+
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of tmin , tmax, tavg
         for all dates between the date selected and the most resent date in the dataset"""
    # Get dates and temps
    find = [func.min(Measure.tobs), func.avg(
        Measure.tobs), func.max(Measure.tobs)]
    if not end:
        # calculate tmin, tmax, tavg for dates greater than start
        results3 = session.query(*find).filter(Measure.date >= start).all()
    else:
        # calculate tmin, tmax, tavg for dates between start and stop
        results3 = session.query(
            *find).filter(Measure.date >= start).filter(Measure.date <= end).all()

    # print(results3)
    session.close()

    # make returns into dic
    start_date=[]
    for each_row in results3:
        one_result={}
        one_result['min_temp']= each_row[0]
        one_result['avg_temp']=each_row[1]
        one_result['max_temp']=each_row[2]
        start_date.append(one_result)



    return jsonify(start_date)



if __name__ == '__main__':
    app.run(debug=True)