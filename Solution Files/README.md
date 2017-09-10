# Solution Files
PLEXOS(R) solution files contain the results of PLEXOS simulations. Constructing reports 
based on these results is a common API activity.

The scripts herein use a combination of pandas, sqlite3, and the PLEXOS API to construct 
such reports and the extensibility to construct further reports.

#1. connect.py

Demonstrates connecting to a solution file and querying a set of results

#2. query_enums.py

Demonstrates listing out the possible values that each of the enumerations
related to solution queries can take. Useful for modifying 1.

#3. query_to_pandas.py

Demonstrates querying results into a pandas dataframe.

#4. query_to_sqlite3.py

Demonstrates pushing a solution query into a sqlite3 database.

For browsing SQLite3 data, you might want to install the DB Browser for SQLite.
http://sqlitebrowser.org/

#5. plotting_queries.py

Demonstrates using matplotlib to produce a plot of PLEXOS results.

#6. api_exploration.py

Use Python to explore the methods available to the Solution class.

#7. plotting_queries2.py

Introduces pivoting out by object name and plotting multiple series on the
same chart. Also introduces an important methodology for using pyDotNet with
methods with many parameters i.e., number of parameters > 10.

Three steps:

a. Alias the Query method with the arguments you plan to use.

b. Construct a tuple of values to send as parameters.

c. Use the __invoke__ method of the alias to call the method.
