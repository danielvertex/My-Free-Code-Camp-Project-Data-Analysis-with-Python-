import pandas as pd 
import numpy as np

def calculate(list):
    #condition
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        #transform the list to a 3x3 matrix
        arr = np.array(list).reshape(3,3)
        
        #create de df
        df = {
            
            
            'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr.flatten()).item()],
            'variance': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr.flatten()).item()],
            'standard deviation': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr.flatten()).item()],
            'max': [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr.flatten()).item()],
            'min': [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr.flatten()).item()],
            'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr.flatten()).item()]
        }


        #df = pd.DataFrame(df)


        return df
