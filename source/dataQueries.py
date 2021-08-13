from numpy import float64
import pandas

#Prints Postcodes with response time in ascending order
def responseByPostcode(dataFrame):
    print('\n--- Response times by Postcode --- \n')
    #convert to dates
    dataFrame['Implemented Date '] = pandas.to_datetime(dataFrame['Implemented Date '], format='%d/%m/%Y %H:%M')
    dataFrame['Request Date '] = pandas.to_datetime(dataFrame['Request Date '], format='%d/%m/%Y %H:%M')

    #calc response time
    dataFrame['Response Time'] = dataFrame['Implemented Date '] - dataFrame['Request Date ']
    dataFrame['Response Time'] = dataFrame['Response Time'].astype('timedelta64[D]')

    #calc and print median response time based on postcode
    results = dataFrame.groupby('Post Code ')['Response Time'].median().reset_index(name = 'Median Response Time (Days)')
    print(results.sort_values('Median Response Time (Days)'))


def topAgentByPostcode(dataFrame):
    print('\n--- Top Agent by Postcode --- \n')
    #convert to float64
    dataFrame['$ Amount '] = dataFrame['$ Amount '].astype(float64)

    #calc sum by postcode and agent, rank results, print (in order)
    results = dataFrame.groupby(['Post Code ','Agent ID '])['$ Amount '].sum().reset_index(name = 'Sum Amount')
    results['rank'] = results.groupby('Post Code ')['Sum Amount'].rank(method='min', ascending=False)
    filteredResults = results.loc[results['rank'] == 1]

    print(filteredResults.sort_values('Sum Amount',ascending=False))
