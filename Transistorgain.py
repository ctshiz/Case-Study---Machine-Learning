import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
from scipy.stats import *
import scipy.stats as stats


#Linear regression library
from sklearn.linear_model import *
from sklearn.preprocessing import *
from sklearn.model_selection import *
from sklearn.metrics import *



#Create the data
observacao = [i for i in range(1, 15)]
drive_in_time = [195,255,195,255,255,255,255,195,255,255,255,255,255,340]
dose_ion = [4,4,4.6,4.6,4.2,4.1,4.6,4.3,4.3,4,4.7,4.3,4.72,4.3]
gain = [1004,1636,852,1506,1272,1270,1269,903,1555,1260,1146,1276,1225,1321]
transistor_gain = pd.DataFrame({"Observações": observacao, "Drive-in Time": drive_in_time, "Dose Ion": dose_ion, "gain": gain})


#checking the data
st.title("Detect Lack of Fit in Simple Linear Regression: Influence of emitter drive-in time and emitter dose in the transistor gain between emitter and collector in an integrated circuit")
st.write("Transistor gain between emitter and collector in an integrated circuit device (hFE) is related to two variables (Myers, Montgomery and Anderson-Cook,2009) that can be controlled at the deposition process, emitter drive-in time (x1, in minutes) and emitter dose (x2, in ions × 10^14). Fourteen samples were observed following deposition, and the resulting data are shown in the table below. We will consider linear regression models using gain as the response and emitter drive-in time or emitter dose as the regressor variable")
check_data = st.checkbox("Select to see the simple data")
if check_data:
	st.write(transistor_gain.head())
	st.write(transistor_gain.describe())
st.write("Let's find out how gain is affected by one parameter")

#Define the problem
st.write("Two questions arise from the data:")
st.write("a) Does the emitter drive-in time influence gain in a linear relationship ?")
st.write("b) Does the emitter dose influence gain in a linear relationship ?")


#Define Hypothesis testing
st.write("In order to asnwer both questions above, the hypothesis test will be done on the slope m of the regressor variable x. Let's remember the linear regression equation: y = mx + b where m is the slope of regressor variable; b is the intercep")
st.write("** 1. Hypothesis Testing **")
st.write("The null Ho e alternative Ha for both questions above are:")
st.write("Ho: The emitter parameter does not influence gain in a linear relationship, i.e, m = 0")
st.write("Ha: The emitter parameter influences gain in a linear relationship, i.e, m != 0 (read m is not null)")
st.write("The stats.lineregress library of Numpy will be used to perfom the hypothesis testing on the slope")


#First, let's start with Emitter Drive-in Time as the first parameter
st.write("** 1.1. Influence of emitter drive-in time in transistor gain**")

#Calling the stats.lineregress library
x_1 = np.array(transistor_gain['Drive-in Time'])
y_1 = np.array(transistor_gain['gain'])
slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = stats.linregress(x_1,y_1)
df = pd.DataFrame(np.array([[slope_1,intercept_1,r_value_1,p_value_1,std_err_1]]), columns = ["slope_1", "intercept_1", "r-value_1", "p-value_1", "std_err_1"])
st.table(df)

if p_value_1 < 0.05:
    st.write("** Conclusion: ** *Reject the Null Hypothesis,.i.e , the emitter drive-in time influences gain in a linear relationship*")
else:
    st.write("** Conclusion: ** *Fail to reject the null hypothesis, i.e, the emitter drive-in time does not influence gain in a linear realtionship*")


#Second, let's proceed with Emitter Dose ion as the second parameter
st.write("** 1.2. Influence of emitter dose ion in transistor gain**")

#Calling the stats.lineregress library
x_2 = np.array(transistor_gain['Dose Ion'])
slope_2, intercept_2, r_value_2, p_value_2, std_err_2 = stats.linregress(x_2,y_1)
df_2 = pd.DataFrame(np.array([[slope_2,intercept_2,r_value_2,p_value_2,std_err_2]]), columns = ["slope_2", "intercept_2", "r-value_2", "p-value_2", "std_err_2"])
st.table(df_2)

if p_value_2 < 0.05:
    st.write("** Conclusion: ** *Reject the Null Hypothesis,.i.e , the emitter drive-in time influences gain in a linear relationship*")
else:
    st.write("** Conclusion: ** *Fail to reject the null hypothesis, i.e, the emitter drive-in time does not influence gain in a linear realtionship*")


#Linear Modeling Step
st.write("**2. Linear Regression Modeling**")
st.write("The selected model is the Simple Linear Regression")
st.write("**2.1. Emitter Driver-in Time as the regressor variable** ")
#Splitting the data
X = transistor_gain[['Drive-in Time']]
y = transistor_gain[['gain']]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, test_size = 0.2, random_state = 6)

#Modelling Step

#Import the selected model

transistor_model = LinearRegression()
#fitting and predict the model
transistor_model.fit(X_train, y_train)
gain_predict = transistor_model.predict(X)


fig, ax = plt.subplots()
ax.scatter(X, y)
ax.plot(X, gain_predict)
plt.xlabel("Drive-in Time, min")
plt.ylabel("Gain")
#plt.show()
st.pyplot(fig)

#Coefficient of determination R^2
st.write('**The coefficent of determinaton of the model is**', r2_score(y, gain_predict))


st.write("**2.2. Emitter Driver-in Time as the regressor variable** ")
#Splitting the data
X_2 = transistor_gain[['Dose Ion']]
X_train_2, X_test_2, y_train, y_test = train_test_split(X_2, y, train_size = 0.8, test_size = 0.2, random_state = 6)
#import the model
transistor_model.fit(X_train_2, y_train)
gain_predict_2 = transistor_model.predict(X_2)
#plot the model
fig_2, ax = plt.subplots()
ax.scatter(X_2, y)
ax.plot(X_2, gain_predict_2)
plt.xlabel("Dose Ion, x10^14")
plt.ylabel("Gain")
st.pyplot(fig_2)

#coefficent of determination R^2
st.write('**The coefficent of determination of the model is**', r2_score(y, gain_predict_2))

#Conclusion
st.write("**Conclusion**: Looking at both determination coefficent R^2 it is clear that the emitter drive-in time model is worse. However the hypothesis testing showed that this parameter affects linearly the transistor gain.  ")
