# sqlalchemy

In this repo there are two components. First is an analysis of precipitation in Hawaii. The second is an app for this data.

Section 1 - Climate Analysis and Exploration  
This is all contained in the jupyter notebook titled climate starter. It retrieves the last year of data, station data and produces the results in various data frames and includes two visualizations.

Section 2 - Climate App
This is all contained in the app.py file. This consists of python code to operate an app that produces the following, included are the calls for the api below. 

--(host) is commonly http://127.0.0.1:5000 --

1.The Home page returns a list of all the api call tags for reference
To call tis page use the host address commonly http://127.0.0.1:5000

2.Precipitation by date and volume
To call this page use: (host)/api/v1.0/precipitation

3.	List of all the stations included in this dataset
To call this page use: (host)/api/v1.0/stations

4.	Returns a list of dates and temps for the most active station over the most resent 12 months.
To call this page use: (host)/api/v1.0/tobs

5.	Provides a list of minimum, average, and maximum temps recorded from the date included to the most resent recording
To call this page use: (host)/api/v1.0/(date desired in 000-00-00 format)

6.	Provides a list of minimum, average, and maximum temps recorded from between two dates
To call this page use: (host)/api/v1.0/(date desired in 000-00-00 format)/ (date desired in 000-00-00 format)
