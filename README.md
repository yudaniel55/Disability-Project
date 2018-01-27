# Disability-Project

This project performs some exploratory data analysis to demonstrate skills needed for data analysis in Python by importing, manipulating, analyzing, and visualizing disability data in the US.  The data for this exercise comes from the 2011-2015 American Community Survey (ACS) 5-year Public Use Microdata Samples (PUMS).  The survey data can be translated using the 2011-2015 ACS 5-year PUMS Data Dictionary.  Data files for the states of California, Illinois, and Massachusetts were used.  To reduce processing time, only the first thousand entries of each file were loaded.  (The files have been truncated to allow upload to GitHub.  The truncated files only contain the first ten thousand entries of each file.)

Some scalability has also been built into the code.  Additional state data files can be loaded by simply dropping them into the same directory and using a naming convention that begins with 'ss'.  The column data to be imported can be changed by editing the 'Dictionaries' Excel file.  

The 'Dictionaries' Excel file has also been used to store the relevant information in the ACS Data Dictionary.  The key translating the relevant survey data has been copied into the Excel file to be read into Python. 

