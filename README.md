# Disability-Project

This project performs some exploratory data analysis to demonstrate skills needed for data analysis in Python by importing, manipulating, analyzing, and visualizing disability data in the US.  The data for this exercise comes from the 2011-2015 American Community Survey (ACS) 5-year Public Use Microdata Samples (PUMS).  The survey data can be translated using the 2011-2015 ACS 5-year PUMS Data Dictionary.  Data files for the states of California, Illinois, and Massachusetts were used.  To reduce processing time, only the first thousand entries of each file were loaded.  (The files have been truncated to allow upload to GitHub.  The truncated files only contain the first ten thousand entries of each file.  The file 'csv writer.py' was used to truncate the original files.)

"Disability" for this project is defined to be "difficulty" with regular physical activities as asked on the survey.

Some scalability has also been built into the code.  Additional state data files can be loaded by simply dropping them into the same directory and using a naming convention that begins with 'truncss'.  The column data to be imported can be changed by editing the 'Dictionaries' Excel file.  

The 'Dictionaries' Excel file has also been used to store the relevant information in the ACS Data Dictionary.  The key translating the relevant survey data has been copied into the Excel file to be read into Python. 

https://www.census.gov/programs-surveys/acs/

** 2/12/18
Planning to expand this project and tie it together with Tableau.  
Objective: Use Python to munge and analyze the full 2011-2015 ACS dataset by utilizing chunksize processing.  Generate a flat file with data from all states within the US.  Use the flat file to visualize data using Tableau.
