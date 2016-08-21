from sklearn.linear_model import LinearRegression

# Read train data
F, N = map(int, raw_input().strip().split(' '))
Feats = []
Targs = []

for i in range(N):
    L = map(float, raw_input().strip().split(' '))
    Feats.append(L[:-1])
    Targs.append(L[-1])

# Use Linear Regression class from sklearn.linear_model to fit the data
regression = LinearRegression()
regression.fit(Feats, Targs)

# Number of test cases
T = int(raw_input())

# Read test data and run it with regression model built before
# Round each prediction result to 2 decimal places
for i in range(T):
    Feats_test = map(float, raw_input().strip().split(' '))
    print round(regression.predict(Feats_test)[0], 2)
