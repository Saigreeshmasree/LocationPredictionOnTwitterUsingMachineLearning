from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, mean_absolute_error,mean_squared_error,r2_score
import math
import numpy as np
class UserNaiveBayesClass:
    def getNaiveResults(self,df):
        df = df[['latitude','longitude', 'userloc']]
        print("df=",df.head())
        X = df[['latitude', 'longitude']]
        y = df[['userloc']]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)
        model = GaussianNB()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test,y_pred)
        mae = mean_absolute_error(y_pred,y_test)
        mse = mean_squared_error(y_pred,y_test)
        rmse = math.sqrt(mse)
        r_squared =r2_score(y_pred,y_test)
        print("Naivebayes","Accuracy = ",accuracy,"\t MAE=",mae,"\t MSE=",mse,"\t RMSE=",rmse,"\t r_squared = ",r_squared)
        #return round(accuracy,2),round(mae,2),round(mse,2),round(rmse,2),round(r_squared,2)
        return accuracy,mae,mse,rmse,r_squared
