import dataQueries as dq
import dataIO as dio

import os

from pathlib import Path
from datetime import datetime

#Test cleanUpOut function
def cleanOut():
    print("\n---Test cleanOut Start---")
    #data path
    jsonPath = 'test/out/'
    
    success = dio.cleanUpOut(jsonPath)
    files = os.listdir(Path(jsonPath))
    fileCount = len(files)

    #Removal of all files in directory success
    assert success == True
    assert fileCount == 0

    print("\n---Test cleanOut Passed---")

#Test missing or invalid file errors are handled
def invalidFormat():
    print("\n---Test invalidFormat Start---")
    #data paths
    csvPath = 'test/in/incorrect.csv'
    jsonPath = 'test/out/'

    #convert and validate data; build dataset from generated JSON files
    success = dio.csvJsonPanda(csvPath,jsonPath, 1000)

    #Load failed due to incorrectly formatted file
    assert success == False

    print("\n---Test invalidFormat Passed---")

def validLoad():
    print("\n---Test validLoad Start---")
    #data paths
    csvPath = 'test/in/test_data.csv'
    jsonPath = 'test/out/'

    #convert and validate data; build dataset from generated JSON files
    success = dio.csvJsonPanda(csvPath,jsonPath, 10)
    files = os.listdir(Path(jsonPath))

    #Load into JSON successful
    assert success == True

    #(37 valid records / 10 file row limit) 4 data + 1 reject
    assert len(files) == 5

    print("\n---Test validLoad Passed---")

def validRead():
    print("\n---Test validLoad Start---")
    #data paths
    csvPath = 'test/in/test_data.csv'
    jsonPath = 'test/out/'

    #convert and validate data; build dataset from generated JSON files
    success = dio.csvJsonPanda(csvPath,jsonPath, 10)
    collectedFrame = dio.collectJsonSet(jsonPath)

    #Load into JSON successful
    assert success == True

    #there are 37 valid rows in test_data.csv
    assert len(collectedFrame) == 37

    print("\n---Test validLoad Passed---")

cleanOut()
invalidFormat()
validLoad()
validRead()    