# Scraping-Case

A python program that scrapes Defacto product datas and write them on a google sheet document.

# How To Use

After cloning everything, write "python3 quickstart.py" to terminal. Authorize your google account, then the program will 
start to scrape. Be sure to change spreadsheetID in writeonsheet file. 

# Why Using Selenium

Inside of the div which has class attribute named dropdown-scrollable, somehow cannot be scene without browser request.
So I used chrome driver to solve it.
