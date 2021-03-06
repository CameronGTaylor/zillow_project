Our goal in this project is to use data retrieved from a Zillow database in order to predict likely house values for single unit properties selling in May and June.

Additionally, we need to find out which counties these houses reside in using outside data from FIPS. Using this county data, we should also find out the distribution of tax rates for each county.

In order to run this project, you must have a env.py file containing three variables: the host ip, username, and password used to access the zillow SQL data, along with the following function:

def get_db_url(db_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return url


We will be using 3 features: bedrooms, bathrooms, and square footage to predict house value. We also use propertylandusetypeid to only select single unit properties, and transactiondate to make sure the sale is in May or June.

zillow_main contains all the modeling and feature engineering for the 3 data points we were given, zillow_extended contains my attempt to find better features to use and the results of those features in their own model.