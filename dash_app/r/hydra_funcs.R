

read_data <- function() {
  
  # Outputs to an list of data
  
  # Read the urls
  urls <- readLines(paste0('C:/Users/ryans/Desktop/RMS/002_projects/scripts/hy',
                           'dra_pdx/stations.csv'))
  
  # Remove the first entry of the URL file (column name)
  urls <- urls[-1]
  
  # Initialize the precip data object; station name vector, and the last date
  pDat <- list(); stns = NULL

  a <- Sys.time()
  
  for (i in 1 : length(urls)) {

    # Read the data from each gage 
    pDat[[i]] <- readLines(urls[i])
    
    # Rename the entry to the brief gage name
    names(pDat)[i] <- substr(urls[i], 40, nchar(urls[i]) - 5)
    
    # Process rainfall data - Extract full gage name & address
    stns[i] <- pDat[[i]][1]
    
    # Remove the header lines from the data
    pDat[[i]] <- pDat[[i]][-(1 : 11)]

    # Break out into list of each day per station
    pDat[[i]] <- strsplit(pDat[[i]], "\\s+")

    # Adjust the each row if it's incomplete; should be 26 entries
    for (j in 1 : length(pDat[[i]])) {
      pDat[[i]][[j]] <- append(pDat[[i]][[j]],
                               rep(NA, 26 - length(pDat[[i]][[j]])))
    }

    # bind into data frame
    pDat[[i]] <- data.frame(do.call("rbind", pDat[[i]]), stringsAsFactors = F)

    # Rename columns
    names(pDat[[i]]) <- c('DTE', 'TOT', paste0('H', addZ(0 : 23)))

    # Coerce the dates to POSIXct
    pDat[[i]]$DTE <- as.POSIXct(pDat[[i]]$DTE, '%d-%b-%Y', tz = 'America/Los_Angeles')

    # Convert '-' to NA and then to numeric and inches
    for (j in 2 : length(pDat[[i]])) {

      pDat[[i]][, j] <- ifelse(pDat[[i]][, j] == '-', NA, pDat[[i]][, j])

      pDat[[i]][, j] <- as.numeric(pDat[[i]][, j]) / 100

    }
  }
  
  b <- round(Sys.time() - a, 2); c <- units(b)

  cat(paste0('Completed in ', b, ' ', c, '.\n\n'))
  
  # Save the interim object
  # saveRDS(pDat, paste0('C:/Users/ryans/Desktop/RMS/002_projects/scripts/hydra_',
  #                      'pdx/pDat.RData'))
  # Load saved data
  # pdat <- readRDS(paste0('C:/Users/ryans/Desktop/RMS/002_projects/scripts/hydr',
  #                        'a_pdx/pDat.RData'))

  # Process some more
  for (i in 1 : length(pDat)) {
    
    # Process station names, addresses and coords
    
    # Separate daily and hourly into two different lists
    
    
    # Get the first & last dates of each station 
    
    
    # Get missing dates of eact station
   
    
     
  }
  
}

# RETURN DATE OF LAST UPDATE ----
get_last_date <- function() {
  
  
  
}

# UPDATE PRECIP DATA OBJECT ----
update_data <- function() {
  
  
  
}

# READ STATION DATA URLS ----
read_URLs <- function() {
  
  # Function that reads the front page of the USGS PDX Hydra website and scrubs
  # for the suffixes of each station URL.
  
  hURL <- readLines('https://or.water.usgs.gov/non-usgs/bes/')
  
  # Pull out the websites with .rain links
  hURL <- hURL[grep('\\.rain', hURL)]
  
  # Index location of quotes in each hURL element
  qInd <- do.call('rbind', gregexpr('\"', hURL))
  
  # Substring the bits between the " marks
  for (i in 1 : length(hURL)) {
    
    hURL[i] <- substr(hURL[i], qInd[i, 1] + 1, qInd[i, 2] - 1)
    
  }
  
  # Create the URLs
  hURL <- paste0('https://or.water.usgs.gov/non-usgs/bes/', hURL)
  
  # Output to text file
  write.csv(x = hURL, row.names = F, quote = F, 
            file = paste0('C:/Users/ryans/Desktop/RMS/002_projects/scripts/hydr',
                          'a_pdx/stations.csv'))

}

# ADD A LEADING ZERO ----
addZ <- function(v) {
  
  # Function to add a leading 0 to a vector of #s if a number is less than 10
  # This is for vectors of minutes, hours, days, and months where there are only 
  # one or two digits
  
  ifelse(v < 10, paste0(0, v), as.character(v))
  
}

# FIND COORDINATES ----
find_coords <- function(address = NULL) {
  
  ## geocoding function using OSM Nominatim API
  ## details: http://wiki.openstreetmap.org/wiki/Nominatim
  ## made by: D.Kisler 

  if(suppressWarnings(is.null(address)))
    
    return(data.frame())
  
  tryCatch(
    d <- jsonlite::fromJSON( 
      gsub('\\@addr\\@', gsub('\\s+', '\\%20', address), 
           'http://nominatim.openstreetmap.org/search/@addr@?format=json&addressdetails=0&limit=1')
    ), error = function(c) return(data.frame())
  )
  
  if(length(d) == 0) return(data.frame())
  
  return(data.frame(lon = as.numeric(d$lon), lat = as.numeric(d$lat)))

}

