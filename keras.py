import numpy as np
from keras.models import Sequential
from keras.models import dense
np.random.seed(99)

#def getData(filename='sample.csv'):
my_data = np.genfromtxt(sample.csv, delimiter=',')
#data that represents where the letters are
x=my_data[:,:27]
y=my_data[:27,:]
#rawData=rawData.astype(int)

#def createDense:
#set up model,numbers are arbitrary
model = model = Sequential()
model.add(Dense(37, input_dim=27, init='uniform', activation='relu'))
model.add(Dense(27, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

    

#if __name__=="__main__":

#configure its learning process
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#iterate traning datasets
model.fit(X_train, Y_train, nb_epoch=200, batch_size=500)
#evaluate performance
loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=32)



    
