# StopSpot
StopSpot is a project to focuse on the quality assurance of static transit stop gps coordinates. These static coordinates will be checked against the dynamic stop data coordinates of transit vehicle. What we are looking for in the data is how far of a distance between when the vehicle stop and where the actual transit stop. Once we have analyze the data, C-Tran will take a look at our findings to determine if our analysis are valid. If the analysis are valid then they will come up with a plan and take actions that can help traffic congestions and provide a better service to customers.

# Development
Developed by: Hui-Yu Sim, Marcus Kwong, Brian Allen, Tarun Singh

# MidPoint Report 
https://github.com/hui2018/SmartCity_StopSpot/blob/master/MidPoint%20Report.pdf

# Delivery
Our delivery to the Ctran is a report with a list of top stop locations that the bus does not stop at the stop location within 30ft.
Some of our analysis including checking the average and median of the distances if both are within 30ft, then we want to flag it as a problematic stop for Ctran to take a look at.

# Backlog
There are number of ideas our team has come up with
1. Create a map that shows all of the locations that are problematic
2. Use a better analysis system such as standard deviation and P-wave to compare with our current analysis to see which is better
3. Create a webpage that allows user to select a bus stop they want to look at and do a playback of all the occurance stops.
4. Create a program that can clean the data first before generating a report

