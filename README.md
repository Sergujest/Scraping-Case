# Scraping-Case

A python program that scrapes Defacto product datas and write them on a google sheet document.

# How To Use

After cloning everything, write "python3 quickstart.py" to terminal. Authorize your google account.

Here is the google sheet document you are scraping to: https://docs.google.com/spreadsheets/d/1Ut5ObFO6cXEZaMAoRcZHwViaVDjuejoLQCd-4PsA7uQ/edit?usp=sharing

# Why Using Selenium

Inside of the div which has class attribute named dropdown-scrollable, somehow cannot be scene without browser request.
So I used chrome driver to solve it.
