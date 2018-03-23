# Roommate-finder-roomster

The project scrapes listings of people with a room for rent looking for roommates.

The first program applys searches for all listings within 20 miles of Dallas, TX. It then applys a filter of males only and copies all the listings to separate html files. There are many files because you have to scoll down the page to see them all, and when you scroll you lose the previous results. So copies of the web page are made at several points along the way to avoid data loss. 
  
The second program looks just scrapes all the links from the multiple files of listings. 

The third program opens up the link to every individual listing, and saves it in it's own html file. In each listing is all the important important information which will be used to fill the database. 

The fourth program creates the database from all the listings that were copied.

1-get all room links.py

2-extract all room links.py

3-copy each room offer.py

4-extract all information for searching rooms.py

The "output databse.csv" is the output of the 4th program. 

The "current_database.xlsx" is the "output database.csv" after some formatting changes, and filtered for my desired rooms. 
