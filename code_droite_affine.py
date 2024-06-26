from sklearn.linear_model import LinearRegression
y = maxima[5:75]
x = (np.array(range(1954,2024,1))).reshape(-1,1)

regression_model = LinearRegression()
regression_model.fit(x, y)

y_prediction = regression_model.predict(x)
y_prediction
plt.plot(x,y)
plt.plot(x,y_prediction)
plt.show()
