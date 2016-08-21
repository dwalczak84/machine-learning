from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Read train data
F, N = map(int, raw_input().strip().split(' '))
Feats = []
Targs = []

for i in range(N):
    L = map(float, raw_input().strip().split(' '))
    Feats.append(L[:-1])
    Targs.append(L[-1])

# Use Pipeline class from sklearn.pipeline.
# Create linear model trained on polynomial of degree F features.
# Fit the date with the model
model_poly_regression = Pipeline([('poly', PolynomialFeatures(degree = F)), ('linear', LinearRegression(fit_intercept = False))])
model_poly_regression.fit(Feats, Targs)

# Number of test cases
T = int(raw_input())

# Read test data and run it with regression model built before
# Round each prediction result to 2 decimal places
for i in range(T):
    Feats_test = map(float, raw_input().strip().split(' '))
    print round(model_poly_regression.predict(Feats_test)[0], 2)
