## clean_and_analyze.sql
This file contains the query and where conditions used to generate C-Tran_Report_great98.csv and C-Tran_Report_opendoor_greater98.csv. Doing the analysis via query was likley not the best approach. Planning to use Python to do the analysis in the future.  

## C-Tran_Report_greater98.csv
This file shows each stops accuracy by diving the total number of stops by the number of stops that where greater than 98 feet from the stop. It also displays the average stopping distance.

## C-Tran_Report_opendoor_greater98.csv
This file contains the same information as C-Tran_Report_greater98.csv but only used events where the bus's door flag was set to 1 (open). 
