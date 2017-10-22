# csc326-project
-------------------------------------------------
HOW TO USE:
-------------------------------------------------
DOWNLOADING EXTERNAL PACKAGES:
-------------------------------------------------
Enter the following commands in:
  Terminal (Mac)
  Command Prompt (Windows)

1. Installing Bottle Framework:
  $ pip install bottle

2. Installing BeautifulSoup Library (V 4.6.0)
  $ pip install beautifulsoup4
  
3. Installing NumPy (V 1.13.3)
  $ pip install numpy

4. Installing Beaker
  $ pip install beaker
-------------------------------------------------
RUNNING WEB APPLICATION:
-------------------------------------------------
1. Enter ' $ python MainApp.py ' in:
  Terminal (Mac)
  Command Prompt (Windows)
2. Open up web browser. Navigate to 'localhost:8000'
3. Enter search string in input box.
  - The results and history data tables will then be displayed to you.
  - To return to the search page, click on the logo in the top left hand corner of the web page.

-------------------------------------------------
TESTING:
-------------------------------------------------
- There are three files used for testing the application, one for front-end and
two for back-end.

Front-end:
- Lab 1: Tests the results obtained from the user's input query
    (ie words and their word counts)
- Lab 1: Tests the history of user inputs
    (ie correctness of the top twenty searched keywords)

Back-end:
- Lab 1: Tests get_inverted_index() and get_resolved_inverted_index() functions.
- Lab 2: Tests functionality of session management class
------------------------------------------------
How to Test:
------------------------------------------------
1. On the command line, navigate to the project directory.
    $ cd /path/to/project/directory
2. Testing Front-end and Back-end functionalities
   Run the following commands:
-  Front-end:
    $ python -m UnitTests.ResultsPageServicesTest
-  Back-end:
    $ python -m UnitTests.WebScrapingServicesTest
-  Session Management: 
    $ python -m UnitTests.UserSessionManagerTests
-----------------------------------------
IMPORTANT: before run Back-end unit test, start application by running (from project root): 
- $ python MainApp.py &
