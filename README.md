Our goal in this project is to use data retrieved from a Zillow database in order to predict likely house values for single unit properties.

Additionally, we need to find out which counties these houses reside in using outside data from FIPS. Using this county data, we should also find out the distribution of tax rates for each county.

In order to run this project, you must have a env.py file containing three variables: the host ip, username, and password used to access the zillow SQL data.

We will be using 3 features: bedrooms, bathrooms, and square footage to predict house value. We also use propertylandusetypeid to only select single unit properties.
There are multiple columns related to square footage; I chose calculatedfinishedsquarefeet because all of the others had much more NULL data, and did not include anything this column didn't also include. We included the fips column because that's what we use to find the county. We use taxvaluedollarcnt as property value because it includes land and structure, and we use taxamount to later calculate tax rates per county.