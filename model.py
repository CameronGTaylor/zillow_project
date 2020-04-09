import evaluate
import pandas as pd
# from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from statsmodels.formula.api import ols
from math import sqrt

def model_fit(train):
    X = train[['bathroom', 'square_feet']]
    y = train.house_value

    simple_lm_k2 = LinearRegression()
    simple_lm_k2.fit(X, y)

    return simple_lm_k2

def model_predict(fitted_training_model, test):
    X = test[['bathroom', 'square_feet']]
    y_test_predictions_k2 = fitted_training_model.predict(X)
    return y_test_predictions_k2

def model_evaluate(predictions, test):
    X = test[['bathroom', 'square_feet']]
    y = test.house_value
    rmse = sqrt(mse(y, predictions))
    
    model = ols('y ~ X', data=test).fit()
    r2, p = evaluate.model_significance(model)

    return rmse, r2, p

