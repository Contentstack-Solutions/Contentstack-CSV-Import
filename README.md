# Contentstack-CSV-Import
Import CSV files as entries to Contentstack.
Two examples, both using the Content Management API provided by Contentstack:
* A Postman Collection and Environment that can be used with Postman Runner or Newman
  * Only import and save (Not publish)
* Python scripts
  * Both import and publish

Entries created in this example are all the cities in Los Angeles county, USA.

##  Before we start
1. Create a stack in Contentstack or use an existing stack, suitable for testing.
2. Create a new content type, using the `Import` button in the Contentstack UI.
3. Create a Management Token in Contentstack Settings and safe it in a safe place.
4. The example assumes you're using the `en-us` locale in your stack. Make sure that is the case or change the code in this repo where needed.

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
  * Click `Run` and see the the City Entries appear in Contentstack.

### Using Newman, the command-line tool
1. Install [Newman](https://www.npmjs.com/package/newman): `npm install -g newman`
2. Under the `Postman` directory in this repo, replace the `<your stack api key>`,`<your management token>` and `api.contentstack.io` if you are in the EU region, in the `contentstack_csv_import__postman_environment.json` file.
3. In the Postman directory, run `newman` pointing to the `uscities.csv`, `contentstack_csv_import__postman_collection.json` and `contentstack_csv_import__postman_environment.json` files.
  * Example:
    * `newman run contentstack_csv_import__postman_collection.json -e contentstack_csv_import__environment2.json -d ../uscities.csv`
    * _(Optional)_ Add `--delay-request 100` to the command to avoid rate limiting by Contentstack.
    * _(Optional)_ Add `-n 10` to the end of the command if you want to limit Newman to create only 10 entries.
4. See the City Entries appear in Contentstack.
