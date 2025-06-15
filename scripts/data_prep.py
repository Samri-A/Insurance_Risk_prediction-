import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore
import numpy as np
class data_prep:
    
    def load_data(path):
        try:
           df = pd.read_csv(path, sep="|")
           return df
        except FileNotFoundError:
            print("File Not found")
        else:
            print("Error occurred")
        finally:
            print("Execution completed")
    
    
    def handel_missing_value(df):
        missed_value = df.isnull().sum().sort_values(ascending=False)
        
        columns_to_drop = []
        print("List of columns to drop that has more than 50% null values") 
        for key in missed_value.index:
            i = missed_value[key]
            if(i > df.shape[0] * 0.5 ):
                print(i)
                print(key)
                columns_to_drop.append(key)
            else:
                break
        
        df.drop(columns=columns_to_drop , inplace= True)
        
        
    def loss_ratio(df):
        df["LossRatio"] = df.apply(
            lambda row: row["TotalClaims"] / row["TotalPremium"] if row["TotalPremium"] != 0 else np.nan ,
            axis = 1 )
        df["LossRatio"].head() 
        
    def check_outlier(df , column):
        sns.boxplot(df[column])
        plt.show()
        
    def compare_bivariant(df ,Y , X ):
        plt.figure(figsize=(12,5))
        sns.scatterplot(y = df[Y] ,  x= df[X]  )
        
    
        