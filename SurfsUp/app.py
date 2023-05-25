from json import dump
import json
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import requests 
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
Base.classes.keys()

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def hawaii():
    """List all available API routes."""
    return (
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/{start}<br/>"
        "/api/v1.0/{start}/{end}<br/>"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #  """Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data)"""
    from datetime import datetime
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    recent_date = datetime.strptime(recent_date[0], '%Y-%m-%d').date()
    monthprcp = recent_date - dt.timedelta(365)
    prcpresults = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= monthprcp).all()

    session.close()
    # ""dictionary using date as the key and prcp as the value.""
    prcpyearresult = {}
    for x, y in prcpresults:
       prcpyearresult[x] = y
    return jsonify(prcpyearresult)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Return a JSON list of stations from the dataset"""
    station_rows = session.query(Station.station).all()
    station_list = [row.station for row in station_rows]
    
    session.close()

    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Query the dates and temperature observations of the most-active station for the previous year of data."""
    from datetime import datetime
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    recent_date = datetime.strptime(recent_date[0], '%Y-%m-%d').date()
    monthprcp = recent_date - dt.timedelta(365)
    active_station = session.query(Measurement.station).\
                            group_by(Measurement.station).\
                            order_by(func.count(Measurement.station).desc()).\
                            first()
    session.close()
    print(active_station)
    #Return a JSON list of temperature observations for the previous year.
    retobj = {}
    if active_station: 
        station = active_station[0]
        temperature_observations = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.station == station, Measurement.date >= monthprcp).\
            all()
        outputdata = []
        for k,v in temperature_observations:
            outputdata.append((k, v))
        retobj[station] = outputdata
    else:
        temperature_observations = {}
    return json.dumps(retobj)

@app.route("/api/v1.0/<start>")
def get_temperature(start):
# Create our session (link) from Python to the DB
    session = Session(engine)

    #calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    # start_date = requests.args.get('start_date') 
    temp_start_result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
                                       func.max(Measurement.tobs)).\
                                        filter(Measurement.date >= start).all()

    session.close()

    tmin = temp_start_result[0][0]
    tavg = temp_start_result[0][1]
    tmax = temp_start_result[0][2]

    temperature_data = {
        'start_date': start,
        'TMIN': tmin,
        'TAVG': tavg,
        'TMAX': tmax
    }
    
    return jsonify(temperature_data)


@app.route("/api/v1.0/<start>/<end>")
def startDateEndDate(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

#calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
    temp_startend_result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), \
                                         func.max(Measurement.tobs)).filter(Measurement.date >= start).\
                                            filter(Measurement.date <= end).all()
    
    session.close()

    tmin = temp_startend_result[0][0]
    tavg = temp_startend_result[0][1]
    tmax = temp_startend_result[0][2]

    temperature_data = {
        'start_date': start,
        'end_date': end,
        'TMIN': tmin,
        'TAVG': tavg,
        'TMAX': tmax
    }

    return jsonify(temperature_data)



if __name__ == '__main__':
    app.run(debug=True)
