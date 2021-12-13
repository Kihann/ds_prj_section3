from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            return render_template('index.html')
        if request.method == 'POST':
            import pandas as pd
            from sklearn.linear_model import LinearRegression

            df_X = pd.read_csv('./X_train.csv')
            df_y = pd.read_csv('./y_train.csv')
            X_train = df_X.drop(['fuelType', 'transmission', 'carID', 'brand', 'model'], axis = 1)
            y_train = df_y.drop(['carID'], axis = 1)

            model = LinearRegression()
            model.fit(X_train, y_train)

            X_year = request.form['x1']
            X_mileage = request.form['x2']
            X_tax = request.form['x3']
            X_mpg = request.form['x4']
            X_engineSize = request.form['x5']
        
            X_test = pd.DataFrame([{'year':int(X_year), 'mileage':int(X_mileage), 'tax':int(X_tax), 'mpg':int(X_mpg), 'engineSize':int(X_engineSize)}])
            y_pred = round(model.predict(X_test)[0][0])

            return render_template('index.html', y_pred=y_pred)
 
    return app

if __name__ == "__main__":
  app = create_app()
  app.debug = True
  app.run()