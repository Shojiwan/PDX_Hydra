# Two conditions: 1) no dash (-1); and 2) two dashes
stns_bu <- stns

stns[[11]] <- 'Terminal 4 NE Rain Gage - 11040 N. Lombard St.'
stns[[35]] <- 'Portland Fire Bureau Rain Gage (Ankeny_02) - 55 SW. Ash St.'
stns[[36]] <- 'Sylvania PCC Rain Gage, SS Bldg - 12000 SW. 49th Ave.'

x <- data.frame(do.call("rbind", strsplit(stns, "\\b - \\b")), 
                stringsAsFactors = F)

x[35, 1] <- 'Portland Fire Bureau Rain Gage (Ankeny_02)'

x[35, 2] <- '55 SW. Ash St.'

x$X2 <- paste0(x$X2, ', Portland, OR')

library(ggmap)

y <- geocode(x$X2, output = 'latlon', source = 'google')

?register_google






