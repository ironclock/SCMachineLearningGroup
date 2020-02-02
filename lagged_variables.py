import numpy as np
import pandas as pd



def make_lags(df, name, lags):
    for i in range (1, lags+1):
        label=name+"_"+str(i)
        df[label]=df[name].shift(i,fill_value=np.nan)