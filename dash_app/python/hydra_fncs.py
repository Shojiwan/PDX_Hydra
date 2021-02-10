#2345678901234567890123456789012345678901234567890123456789012345678901234567890

import urllib.request
import pandas as pd
import re
from io import StringIO

def read_data(stID, strD, endD):

  # Function to read data from HYDRA station for start date to end date

  # Look up URL from station ID
  

  # Read the urls  
  link = "https://or.water.usgs.gov/non-usgs/bes/open_meadows.rain"

  f = urllib.request.urlopen(link)

  pDat = str(f.read())

  # Split header text, header line and data
  pDat = re.split("Daily  Hourly data -->\\\\n   |-{114}\\\\n", pDat)
  
  # For the header line, insert an "H" in front of the number
  pDat = re.sub('\s+', ' H', pDat[1]) + pDat[2]

  # Fix the carriage returns
  pDat = re.sub('\\\\n', '\\n', pDat)

  pDat = StringIO(pDat)

  pDat = pd.read_csv(pDat, sep = "\s+")

  # pDat.to_csv('C:/Users/ryans/Desktop/RMS/002_projects/pdx_hydra/dash_app/data/test.csv',index = False)
  
  return(pDat)








  
  # Remove the first entry of the URL file (column name)
  
  # Initialize the precip data object; station name vector, and the last date
  
  # for i in range(1 : len(urls)):

    # Read the data from each gage 
    
    # Rename the entry to the brief gage name
    
    # Process rainfall data - Extract full gage name & address
    
    # Remove the header lines from the data

    # Break out into list of each day per station

    # Adjust the each row if it's incomplete; should be 26 entries

    # bind into data frame

    # Rename columns

    # Coerce the dates to POSIXct

    # Convert '-' to NA and then to numeric and inches
  
    # Process some more
    
    # Process station names, addresses and coords
    
    # Separate daily and hourly into two different lists
    
    # Get the first & last dates of each station 
    
    # Get missing dates of eact station