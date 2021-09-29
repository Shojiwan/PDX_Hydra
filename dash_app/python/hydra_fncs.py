#2345678901234567890123456789012345678901234567890123456789012345678901234567890

import urllib.request
import pandas as pd
import re
from io import StringIO
import datetime

def read_data(stID):

  # Function to read data from HYDRA station for start date to end date

  # Look up URL from station ID
  # TBD

  # Read the urls  
  link = "https://or.water.usgs.gov/non-usgs/bes/" + stID + ".rain"

  f = urllib.request.urlopen(link)

  pDat = str(f.read())

  # Split header text, header line and data
  pDat = re.split("Daily  Hourly data -->\\\\n   |-{114}\\\\n", pDat)
  
  # For the header line, insert an "H" in front of the number
  pDat = re.sub('\s+', ' H', pDat[1]) + pDat[2]

  # Fix the carriage returns
  pDat = re.sub('\\\\n', '\\n', pDat)

  pDat = pd.read_csv(StringIO(pDat), sep = "\s+")

  # Remove null entries (with ' as the date)
  pDat = pDat.loc[pDat['Date'] != '\'', :]

  return(pDat)

