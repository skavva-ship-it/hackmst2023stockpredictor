# hackmst2023stockpredictor

This code was written on April 22nd of 2023 during the annual HackMCST put on the Morris County School of Technology. This code is not extremely lengthy and annotated for an easier expierience for the reader. Additionally I had worked with two other students (Matthew Fieore and Lucas Abend) to develop the ideas and syntax of the code, whom of which were a huge help and inspiration to the end product.


Mission Statement:
  - The goal of this program is to aid investors and help guide them in the stock market by helping them debrief information about any stock. It allows the user to get easy access to all of the latest stories about a stock alongside the history of it. And, as an added bonus the users are also able recieve a calculated prediction of where the stock will go in the following market openings. 


Functions of Program:
  - Get Instant Opening and Closing Market Prices upon selecting a stock of your choice.
  - Recieve a debriefing of a stock by looking at the 9 AUTO-GENERATED articles given by Google's Custom Search API
  - Get insight on how a stock will do based off keywords found within all the articles (Point-Based) ****DISCLAIMER: STOCK PREDICTION MAY BE INNACTURATE DUE TO THE VOLITAL NATURE OF THE MARKET CURRENTLY AND SHOULD NOT BE USED TO INFLUENCE TRADING MOVES, ANY DESCISION MADE BY A TRADER SHALL SOLELY BE AT THEIR DISCRETION****
  - Recieve a neat graph detailing the stock price history from any two inputted dates.


How to Setup the API:
1. Headover to https://programmablesearchengine.google.com/controlpanel/create and create an API programmable search project
2. Scroll down to 'Search Features' and input any websites/newspage domains you would like search within
(Note API can only iterate 10,000 queries a day without billing)

How to use the Program:

1. Retrieve API_KEY and CSE_ID from the Programmable Search API, and input them into indicated variable placeholders in the code
2. Select a date using the date placeholder in the code
3. Be sure to pip install all of the necessary packages
4. Once running, enter the stock initals of the desired stock (Ex. Apple Stock is AAPL)
5. Values, Articles, Prediction and Graph will then initalize



Thank you and good luck learning! 
- Sanjay Avva, MCST CIS 2026
