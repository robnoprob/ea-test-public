import dataQueries as dq
import dataIO as dio

from datetime import datetime

#data paths
csvPath = 'data/in/Transaction.csv'
jsonPath = 'data/out/'


#execute
print('Execution started: ' + str(datetime.now()))

#convert and validate data; build dataset from generated JSON files
success = dio.csvJsonPanda(csvPath,jsonPath, 1000)

if success:
    #load data from JSON to data frame
    collectedFrame = dio.collectJsonSet(jsonPath)
    print('\n--- json conversion complete and data collected into single frame ---\n')

    #execute queries
    dq.responseByPostcode(collectedFrame)
    dq.topAgentByPostcode(collectedFrame)
   
print('\nExecution ended: ' + str(datetime.now()))