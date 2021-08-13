# ea-test-public

This is a simple application which:
    1. Reads from a specified csv file
        a. .\data\in\Transaction.csv
    2. Validates the data and stores it in JSON format (1000 records/events per file)
        a. .\data\out\transactions_x.json <-- valid data file x replaced by partition number
        b. .\data\out\transactions_reject.json <-- rejected data file
    3. Loads the generated JSON into a data frame
    4. Prints a list of postcodes with their median response times
    5. Prints a list of postcodes with their top agent based on amount of dollars

Source Files:
    1. dataIO.py - handles file reading, transform/write, and delete
    2. dataQueries.py - contains the data queries described above
    3. dataValidation.py - contains data validation functions called by dataIO.py
    4. execute.py - runs the application against '.\data\in\Transaction.csv' and prints out the results (plus some tracking/logging details)
    5. execute_tests.py - runs the application test suite against '.\test\in\*'

Data Files:
    1. .\data\in\Transacion.csv - data file provided
    2. .\test\in\test_data.csv - test data file containing subset and invalid rows
    3. .\test\in\incorrect.csv - contains an incorrectly formatted CSV

GIT:
    To download the latest version of the code run the below:

        git clone https://github.com/robnoprob/ea-test-public.git

Execution -- run all commands from the ea-test-pubic directory:
    Python 3.9.6 - version installed.
    
    To get all required imports run the below:

        pip install -r requirements.txt

    To run the application once cloned run the below:

        python .\source\execute.py
