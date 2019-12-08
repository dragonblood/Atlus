import numpy as np
import warnings
import pickle

mentalhealth_df = list(mydata.values())


male = set(["male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man", "msle", "mail", "malr", "cis man"])

female = set(["cis female", "f", "female", "woman", "femake", "female ", "cis-female/femme", "female (cis)", "femail"])

numbersdf = [None] * 21
numbersdf[0] = int(mentalhealth_df[0])

if mentalhealth_df[1].lower() in male:
    numbersdf[1] = 2
elif mentalhealth_df[1].lower() in female:
    numbersdf[1] = 0
else:
    numbersdf[1] = 1


def yn(x,i):
    if x == "Yes":
        numbersdf[i] = 1
    else:
        numbersdf[i] = 0


def ydkn(x,i):
    if x == "Yes":
        numbersdf[i] = 2
    elif x == "Don't know":
        numbersdf[i] = 1
    else:
        numbersdf[i] = 0


def ymn(x,i):
    if x == "Yes":
        numbersdf[i] = 2
    elif x == "Maybe":
        numbersdf[i] = 1
    else:
        numbersdf[i] = 0


def ysotn(x,i):
    if x == "Yes":
        numbersdf[i] = 2
    elif x == "Some of them":
        numbersdf[i] = 1
    else:
        numbersdf[i] = 0


yn(mentalhealth_df[5],2)

if mentalhealth_df[7] == "Often":
    numbersdf[3] = 3
elif mentalhealth_df[7] == "Sometimes":
    numbersdf[3] = 2
elif mentalhealth_df[7] == "Rarely":
    numbersdf[3] = 1
else:
    numbersdf[3] = 0

if mentalhealth_df[8] == "1-5":
    numbersdf[4] = 1
elif mentalhealth_df[8] == "6-25":
    numbersdf[4] = 2
elif mentalhealth_df[8] == "26-100":
    numbersdf[4] = 3
elif mentalhealth_df[8] == "100-500":
    numbersdf[4] = 4
elif mentalhealth_df[8] == "500-1000":
    numbersdf[4] = 5
elif mentalhealth_df[8] == "More than 1000":
    numbersdf[4] = 6
else:
    numbersdf[4] = 0

yn(mentalhealth_df[9],5)
yn(mentalhealth_df[10],6)
ydkn(mentalhealth_df[11],7)

if mentalhealth_df[12] == "Yes":
    numbersdf[8] = 2
elif mentalhealth_df[12] == "Not sure":
    numbersdf[8] = 1
else:
    numbersdf[8] = 0

ydkn(mentalhealth_df[13],9)
ydkn(mentalhealth_df[14],10)
ydkn(mentalhealth_df[15],11)

if mentalhealth_df[16] == "Very Easy":
    numbersdf[12] = 4
elif mentalhealth_df[16] == "Somewhat easy":
    numbersdf[12] = 3
elif mentalhealth_df[16] == "Somewhat difficult":
    numbersdf[12] = 2
elif mentalhealth_df[16] == "Very difficult":
    numbersdf[12] = 1
else:
    numbersdf[12] = 0

ymn(mentalhealth_df[17], 13)
ymn(mentalhealth_df[18], 14)
ysotn(mentalhealth_df[19], 15)
ysotn(mentalhealth_df[20], 16)
ymn(mentalhealth_df[21], 17)
ymn(mentalhealth_df[22], 18)
ydkn(mentalhealth_df[23], 19)
yn(mentalhealth_df[24], 20)

numbersdf = (np.asarray(numbersdf)).reshape(1, -1)

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(numbersdf)
prediction = np.where(result > 0, 'Yes', 'No')
print(prediction)

