import pandas as pd
from env import get_db_url
import split_scale

def get_zillow_fips_data():
    url = get_db_url('zillow')
    query = ('''
    SELECT bathroomcnt AS bathroom, bedroomcnt AS bedroom, 
        calculatedfinishedsquarefeet AS square_feet, taxamount AS tax, 
        fips AS counties, taxvaluedollarcnt AS house_value 
    FROM properties_2017
    WHERE propertylandusetypeid = 261''')
    df = pd.read_sql(query, url)
    
    counties = pd.read_table('FIPS.txt', header=1)
    counties.columns = ['FIPS', 'county', 'state']
    
    df = pd.merge(df, counties, left_on='counties', 
                        right_on='FIPS', how='left')
    df.drop(columns='counties', inplace=True)
    return df

def clean_data(df):
    bathroom_std = df.bathroom.std()
    bedroom_std = df.bedroom.std()
    square_feet_std = df.square_feet.std()
    house_value_std = df.house_value.std()

    df.bedroom = df.bedroom[(df.bedroom <= bedroom_std * 10)]
    df.bathroom = df.bathroom[(df.bathroom <= bathroom_std * 10)]
    df.square_feet = df.square_feet[
        (df.square_feet <= square_feet_std * 10) &
        (df.square_feet >= square_feet_std * .1)]
    df.house_value = df.house_value[
        (df.house_value <= house_value_std * 10) & 
        (df.house_value >= house_value_std * .1)]
    
    ave_bedrooms = round(df.bedroom.mean())
    df.bedroom.replace(0, ave_bedrooms, inplace=True)
    ave_bathrooms = round(df.bathroom.mean())
    df.bathroom.replace(0, ave_bathrooms, inplace=True)

    df.dropna(inplace=True)
    df.county = df.county.astype(int)
    df.square_feet = df.square_feet.astype(int)
    df.bedroom = df.bedroom.astype(int)
    df.house_value = df.house_value.astype(int)

    train, test = split_scale.split_my_data(df, .8)
    return train, test

