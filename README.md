# EE629

Internet of Things

Spring 2020

Coding Contribution


This program requires you to have API keys in order to search tweets from Twitter's website

You will put in two search terms and the number or results you wish to pull from. The program will then create two .csv files of the found tweets and perform a TextBlob analysis on them to determine each tweet's polarity. The output of the program is four numbers, the highest and lowest polarization scores found for search term 1 and the highest and lowest polarization scores for search term 2

To run from terminal window: 
python3  tweets.py   --search_term1  mysearch1  --search_term2  mysearch2 --search_max  mymaxresults 
where mysearch1 is the first term the user wants to search for;  default = music
where mysearch2 is the second term the user wants to search for; default = movie
and mymaxresults is the maximum number of resulta;  default = 30
