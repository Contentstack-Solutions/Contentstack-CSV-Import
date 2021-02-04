# Contentstack-CSV-Import

**Not officially supported by Contentstack**

Import CSV files as entries to Contentstack.
Two examples, both using the Content Management API provided by Contentstack:
* A Postman Collection and Environment that can be used with Postman Runner or Newman
  * Creates an entry and publishes it to an environment
* Python scripts
  * Creates an entry and publishes it. Also offers bulk publish.

Entries created in this example are all the cities in Los Angeles county, USA.

##  Before we start
1. Create a stack in Contentstack or use an existing stack, suitable for testing.
2. Create a new content type, using the `Import` button in the Contentstack UI. Choose the `contenttype_definition_us_cities.json` file from this repo. Then confirm the content type has been created successfully.
3. Create a Management Token with Write Permissions under Settings and store it in a safe place.
4. The example assumes you're using the `en-us` locale in your stack. Make sure that is the case or change the code in this repo where needed.
5. For publishing, create an environment in Contentstack. In this example the environment is called `development`.

## Postman Example

Download and install [Postman](https://www.postman.com/) on your computer.

### Using Postman UI
1. In Postman, import the collection from `postman/contentstack_csv_import__postman_collection.json` file in this repository.
  * A new Postman collection will be created: `Contentstack - CSV Import`
2. In Postman, import the environment from `postman/contentstack_csv_import__postman_environment.json` file in this repository.
  * A new Postman environment will be created: `Contentstack - CSV Import`
3. Put the correct value in the Environment variables:
  * `HOST` - Either the US region (api.contentstack.io) or the EU region (eu-api.contentstack.com).
  * `APIKEY` - Contentstack's stack API key, available from the Contentstack web UI.
  * `AUTHORIZATION` - Your management token created above.
4. Click on `Runner`
  * Find the Collection just created.
  * Choose the environment created just before.
  * _(Optional)_ For debugging purposes in the beginning, it could be good to limit the iterations done in the import, e.g. 10.
  * _(Optional)_ To lower the risk of being rate limited by Contentstack, it could be a good idea to input `100` in the `Delay` field (Especially if you are not limiting the iterations).
  * Select the `uccities.csv` file in `Data`.
  * _(Optional)_  We recommend checking in the `Save Responses`, to get a better understanding of errors, if/when they arise.
  * Notice it is possible to uncheck the publishing request, if you only want to create the entry.
  * Click `Run` and see the the City Entries appear in Contentstack.

### Using Newman, the command-line tool
1. Install [Newman](https://www.npmjs.com/package/newman): `npm install -g newman`
2. Under the `Postman` directory in this repo, replace the `<your stack api key>`,`<your management token>` and `api.contentstack.io` if you are in the EU region, in the `contentstack_csv_import__postman_environment.json` file.
3. In the Postman directory, run `newman` pointing to the `uscities.csv`, `contentstack_csv_import__postman_collection.json` and `contentstack_csv_import__postman_environment.json` files.
    * *Example:*
      * `newman run contentstack_csv_import__postman_collection.json -e contentstack_csv_import__environment.json -d ../uscities.csv`
      * _(Optional)_ Add `--delay-request 100` to the command to avoid rate limiting by Contentstack.
      * _(Optional)_ Add `-n 10` to the end of the command if you want to limit Newman to create only 10 entries.
4. See the City Entries appear and publish in Contentstack.

## Python Example
1. This script was developed using Python 3.7.6 and utilises e.g. the `requests` package, installed using pip.
    * `pip install requests`
2. Define following environmental variables on your computer:
    * `CS_APIKEY` - The API key of your Contentstack stack.
    * `CS_HOST` - Contentstack Region. Either api.contentstack.io (US) or eu-api.contentstack.com (EU)
    * `CS_MANAGEMENTTOKEN` - Contentstack Management Token with write permissions.
3. Move into the `python` directory and run the `start.py` file.
    * `python start.py`
4. The script asks you if you want to try to bulk publish the entries.
    * Note that bulk publishing only works if it's included in your organisation's plan.
5. Watch output logs of the script and see the City Entries appear in Contentstack.
