import json
import pandas
import os
import re
from pathlib import Path
import dataValidation as dv

#Process input CSV
#csvPath -- location and name of csv file
#jsonPath -- save location of json files
#fileBreak -- how many records per json file
def csvJsonPanda(csvPath, jsonPath, fileBreak):
    #exclued two unnamed columns as they held no known value
    try:
        cleanUpOut(jsonPath)
        
        csvData = pandas.read_csv(Path(csvPath)
            ,usecols=['Account_ID ','CODE ','Implemented Date ','Active Indicator ','Account Type ','Service ','BU','Request Date ','Account status ','Status Code ','$ Amount ','Version ','Agent ID ','FIBRE ','last Updated Date ','Property TYPE ','Post Code ']
            ,dtype={'Account_ID ':str,'CODE ':str,'Implemented Date ':str,'Active Indicator ':str,'Account Type ':str,'Service ':str,'BU':str,'Request Date ':str,'Account status ':str,'Status Code ':str,'$ Amount ':str,'Version ':str,'Agent ID ':str,'FIBRE ':str,'last Updated Date ':str,'Property TYPE ':str,'Post Code ':str})

    except:
        print('\nERROR --- Input file could not be loaded!')
        return False

    #loop through data set row by row
    cleanData = []
    rejectData = []
    rowCount = 0
    fileCount = 0
    for index, csvRow in csvData.iterrows():
        #create hash id
        csvRow['hash'] = hash(csvRow.values.tobytes)

        #validate key/important data attributes
        validAgent = dv.validateNumeric(csvRow['Agent ID '])
        validPC = dv.validatePostcode(csvRow['Post Code '])
        validImplementedDT = dv.validateDate(csvRow['Implemented Date '])
        validRequestDT = dv.validateDate(csvRow['Request Date '])
        validAmount = dv.validateDollarAmount(csvRow['$ Amount '])

        validationResults = True
        if not validAgent or not validPC or not validImplementedDT or not validRequestDT or not validAmount:
            validationResults = False

        #if valid data load into cleanData
        if validationResults:
            rowCount += 1
            cleanData.append(csvRow.to_dict())
            #if at max records for file - save.
            if rowCount == fileBreak:
                with open(Path(jsonPath + 'transactions_' + str(fileCount) + '.json'), 'w', encoding='utf-8') as jsonFile:
                    jsonFile.write(json.dumps(cleanData, indent=2))
                    print('Loop Generated ' + str(Path(jsonPath + 'transactions_' + str(fileCount) + '.json')))
                    cleanData = []
                    rowCount = 0
                    fileCount += 1
        
        #capture rejected rows in rejectData
        else:
            rejectData.append(csvRow.to_dict())
    
    #Save unsaved clean rows
    with open(Path(jsonPath + 'transactions_' + str(fileCount) + '.json'), 'w', encoding='utf-8') as jsonFile:
        jsonFile.write(json.dumps(cleanData, indent=2))
        print('Final Generated ' + str(Path(jsonPath + 'transactions_' + str(fileCount) + '.json')))

    
    #Save rejects for investigation
    with open(Path(jsonPath + 'transactions_reject.json'), 'w', encoding='utf-8') as jsonFile:
        jsonFile.write(json.dumps(rejectData, indent=2))
        print('Final Generated ' + str(Path(jsonPath + 'transactions_reject.json')))

    return True


#makes a dataframe of all the json files (excluding rejects)
def collectJsonSet(jsonPath):
    files = os.listdir(Path(jsonPath))

    jsonFrames = []
    for jsonFile in files:
        validFile = re.match('^transactions\_\d{1,}\.json$',jsonFile)

        if validFile is not None:
            #print('Collected ' + jsonFile)
            jsonData = pandas.read_json(Path(jsonPath + jsonFile)
                ,dtype={'Account_ID ':str,'CODE ':str,'Implemented Date ':str,'Active Indicator ':str,'Account Type ':str,'Service ':str,'BU':str,'Request Date ':str,'Account status ':str,'Status Code ':str,'$ Amount ':str,'Version ':str,'Agent ID ':str,'FIBRE ':str,'last Updated Date ':str,'Property TYPE ':str,'Post Code ':int,'hash':str})
            jsonFrames.append(jsonData)

    jsonDataComplete = pandas.concat(jsonFrames, sort=False) 
    jsonDF = pandas.DataFrame(jsonDataComplete)
    jsonDF = jsonDF.reset_index()

    return jsonDF

#Clean output dir
def cleanUpOut(jsonPath):
    try:
        files = os.listdir(Path(jsonPath))

        for jsonFile in files:
            os.remove(Path(jsonPath + jsonFile))

        print('jsonPath Directory Emptied')
        return True

    except:
        print('Something went wrong cleaning ' + str(Path(jsonPath)))
        return False

