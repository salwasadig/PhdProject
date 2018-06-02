from MLModels import MLmodel
import pickle
import pandas as pd

x = MLmodel()
X_train, X_test, Y_train, Y_test = x.get_data()


RF = pickle.load(open('finalized_RF_model.sav', 'rb'))
RFscore = RF.score(X_test, Y_test)
print('RF:{}'.format(RFscore))

DT = pickle.load(open('finalized_DT_model.sav', 'rb'))
DTscore = DT.score(X_test, Y_test)
print('DT:{}'.format(DTscore))
