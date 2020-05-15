'''
A Python script using the Content Management API offered by Contentstack:
https://www.contentstack.com/docs/developers/apis/content-management-api/

2020-05-13
oskar.eiriksson@contentstack.com

Remember to define the following environmental variables:
 - CS_APIKEY: Stack API key
 - CS_HOST: hostname for either US (api.contentstack.io) or EU (eu-api.contentstack.com) region
 - CS_MANAGEMENTTOKEN: Contentstack Management Token with write permissions.
'''
from datetime import datetime
import os
from time import sleep
import requests

apiKey = os.getenv('CS_APIKEY', None)
cmaHost = os.getenv('CS_HOSTNAME', None)
manToken = os.getenv('CS_MANAGEMENTTOKEN', None)

def checkVars():
    '''
    Checking wether environmental variables have all ben defined.
    '''
    if all(v is not None for v in [apiKey, cmaHost, manToken]):
        return True
    return False

authHeader = {
    'api_key': apiKey,
    'authorization': manToken,
    'Content-Type': 'application/json'
}

def printError(httpStatus, res):
    print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)") + ' | Error: {httpStatus} - {error}'.format(httpStatus=httpStatus, error=res.json()))

def createEntry(contentType, locale, body):
    url = 'https://{cmaHost}/v3/content_types/{contentType}/entries?locale={locale}'.format(cmaHost=cmaHost, contentType=contentType, locale=locale)
    res = requests.post(url, headers=authHeader, json=body)
    httpStatus = res.status_code
    if httpStatus == 201:
        uid = res.json()['entry']['uid']
        title = res.json()['entry']['title']
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)") + ' | Entry created - Title: {title} - uid: {uid} - Content Type: {contentType} - Locale: {locale}'.format(title=title, uid=uid, contentType=contentType, locale=locale))
        return uid
    printError(httpStatus, res)
    return None


def publishEntry(contentType, uid, body):
    url = 'https://{cmaHost}/v3/content_types/{contentType}/entries/{uid}/publish'.format(cmaHost=cmaHost, contentType=contentType, uid=uid)
    res = requests.post(url, headers=authHeader, json=body)
    httpStatus = res.status_code
    if httpStatus == 201:
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)") + ' | Entry published ({uid}) - {notice}'.format(uid=uid, notice=res.json()['notice']))
        return True
    printError(httpStatus, res)
    return False


def bulkPublishEntries(contentType, body):
    url = 'https://{cmaHost}/v3/bulk/publish'.format(cmaHost=cmaHost)
    res = requests.post(url, headers=authHeader, json=body)
    httpStatus = res.status_code
    if httpStatus == 200:
        print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)") + ' | ' + res.json()['notice'])
        return True
    printError(httpStatus, res)
    return False
