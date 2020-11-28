def read_data(stID, strD, endD):

  # Read data from station for start date to end date
  
  import urllib

  # Look up URL from station ID
  link = "https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain"

  f = urllib.request(link)

  myfile = f.read()
  
  print(myfile)

  # Read the urls
  
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