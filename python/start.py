'''
Creates and (bulk)publishes entries in Contentstack from a CSV file.

2020-05-13
oskar.eiriksson@contentstack.com
'''
from time import sleep
import csv
import contentstack

contentType = 'us_cities'
locale = 'en-us'
environments = ['development']
csvFile = '../uscities.csv'

def checkBulk():
    bulk = None # Determining whether to bulk publish entries
    while bulk not in ('Y', 'y', 'N', 'n'):
        bulk = input("Do you want to try to bulk publish? (Y/N) ")
    return bool(bulk in ('y', 'Y'))

# Same body for all entries when publishing one entry at a atime
singleEntryPublishBody = {
    'entry': {
        'environments': environments,
        'locales': [locale]
    },
    'locale': locale
}

def constructBulkandPublish(uids):
    chunk = 10 # Bulk publsh allows 10 entries at a time to be published
    while uids: # While we haven't emptied the array
        entriesArr = []
        for entryUid in uids[:chunk]:
            singlebulkEntry = {
                'uid': entryUid,
                'content_type': contentType,
                'locale': locale
            }
            entriesArr.append(singlebulkEntry)
        bulkBody = {
            'entries': entriesArr,
            'locales': [locale],
            'environments': environments
        }
        try:
            sendBulk = contentstack.bulkPublishEntries(contentType, bulkBody)
            sleep(1) # To prevent rate limiting
            if not sendBulk:
                return False, uids
        except Exception as e:
            print('Failed bulk publishing... Publishing one entry at a time.', e)
            return None
        uids = uids[chunk:] # Delete all the items from the array that have been sent to publish queue
    return True, 'ok'

if contentstack.checkVars():
    reader = csv.DictReader(open(csvFile))
    entries = []
    for entry in reader:
        d = {}
        for field in entry:
            d[field] = entry[field]
        entries.append(d)
    bulkPublish = checkBulk() # Does the user want to bulk publish entries?
    uidArr = []
    for entry in entries:
        entry = {'entry': entry}
        uid = contentstack.createEntry(contentType, locale, entry)
        if uid:
            uidArr.append(uid)
            if not bulkPublish:
                contentstack.publishEntry(contentType, uid, singleEntryPublishBody)

    if bulkPublish:
        bulkPublishEntries = constructBulkandPublish(uidArr)
        if not bulkPublishEntries[0]:
            for i in uidArr:
                contentstack.publishEntry(contentType, i, singleEntryPublishBody)
        else:
            print('Bulk publishing finished. Check publishing queue to confirm.')
else:
    print('You need to define the environmental variables before running this script.')
