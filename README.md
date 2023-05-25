# sqlalchemy-challenge
sqlalchemy-challenge

#                     CLIMATE Analysis for Honolulu, Hawaii

A dataset was provided for a long holiday vacation in Honolulu, Hawaii and to help with trip planning, a climate analysis about the area was done in advance.
 The following sections outline the steps that was needed to take to accomplish this task.

## Part 1: Analyze and Explore the Climate Data
    
    Python and SQLAlchemy was used to do a basic climate analysis and data exploration of climate database. Specifically, SQLAlchemy ORM queries, Pandas, and Matplotlib is used to expore the data and have a clear view of temperature and different stations. 

    SQLAlchemy was used to create_engine() function to connect to SQLite database.
    SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named station and measurement.
    Also linked Python to the database by creating a SQLAlchemy session.

    Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

###             Precipitation Analysis: 
            
            To find the  most recent date in the dataset.
            Using that date, got the previous 12 months of precipitation data by querying the previous 12 months of data.
            Only used the "date" and "prcp" values.
            All the query results were stored into a Pandas DataFrame.
            The results were  plotted by using the DataFrame plot method.

###             Station Analysis
            
            Designed a query to calculate the total number of stations in the dataset.
            Designed a query to find the most-active stations (that is, the stations that have the most rows). 
            All the stations and observation counts shown in descending order.
            Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

## Part 2: Design Your Climate App using FLASK API
    Below are all available API routes."""
        (
        "Available Routes:<br/>" ---------shows all available routes for API 
        "/api/v1.0/precipitation<br/>" ---shows percipitation anlysis for the last 12 months of data from latest date
        "/api/v1.0/stations<br/>" --------shows list of all staions in the dataset
        "/api/v1.0/tobs<br/>" ------------shows dates and temp observations of the most-active station for last 12 months
        "/api/v1.0/{start}<br/>" ---------shows the min, max and average temperature for a specified date
        "/api/v1.0/{start}/{end}<br/>")---shows the min, max and average temp for a specified start and end date 


    All of the above queries were returned in Jsonify

# Analysis 

Looking at the dataset and graphs for percipitaion and station analysis , it shows that following are the station in descending order that were most active 
[('USC00519281', 2772),
 ('USC00519397', 2724),
 ('USC00513117', 2709),
 ('USC00519523', 2669),
 ('USC00516128', 2612),
 ('USC00514830', 2202),
 ('USC00511918', 1979),
 ('USC00517948', 1372),
 ('USC00518838', 511)]




Tutoring session
Before and After hours  
Reviewed lot of class activites 
https://docs.sqlalchemy.org/en/20/orm/extensions/automap.html#sqlalchemy.ext.automap.automap_base
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/api/#module-flask_sqlalchemy
https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_connecting_to_database.html
https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91