# NLP-Workshop-Week-1

## How to connect to the Twitter API
### Create a Twitter developer account and create an application to obtain API credentials:
* Go to the Twitter Developer Portal.
* Sign in with your Twitter account or create a new one.
* Create a new project and fill in the required details.
* Once your project is created, go to the "Keys and tokens" tab.
* Note down the values for the following credentials: api_key, api_secret, access_token, access_token_secret.

### Store the API credentials securely:
* Create a file named .env in the same directory as your code.
* Open the .env file and add the following lines, replacing the placeholders with your API credentials:
```
api_key=your_api_key

api_secret=your_api_secret

access_token=your_access_token

access_token_secret=your_access_token_secret
```
### Install the necessary dependencies:

* Tweepy: pip install tweepy
* Pandas: pip install pandas
* python-dotenv: pip install python-dotenv


## How to connect to Mediastack API

### Create a MediaStack account and obtain an API access key:

* Go to the MediaStack website and create a new account.
* Once you have an account, log in and navigate to the API Dashboard section.
* Under the "Your Access Keys" tab, click on the "Create New Access Key" button to generate a new API access key.
* Note down the value of the access key, as you'll need it to authenticate your requests.

### Install the necessary dependencies:
* http.client: It is a built-in module in Python, so no additional installation is required.
* urllib.parse: It is a built-in module in Python, so no additional installation is required.
* python-dotenv: pip install python-dotenv

### Store the MediaStack API access key securely:
* Create a file named .env in the same directory as your code. Can be the same .env as the one used for the Twitter API.
* Open the .env file and add the following line, replacing your_access_key with your MediaStack API access key:
```
mediastack_access_key=your_access_key
