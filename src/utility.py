import pandas as pd
import streamlit as st

@st.cache
def load_dataframe(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

    columns = list(df.columns)
    columns.append(None)
    biomarkers=["ALT","ALP","AST","TBIL","TP","ALB","GLOB","LDH","CK","CK MB","ALDO","TAS","CREA","P","AMY","LIP","Fe","TIBC","CU","LACTA","CO2","AMM","MG","CA","K","NA","CL","NA/K","ZN","TC","TG","HDL","LDL"]
    df_average=pd.DataFrame(data=        [[5.33,600.68,139.12,12.54,43.26,15.92,27.36,961.47,2287.89,3623.79,28.49,1.77,49.24,6.62,901.26,85.60,32.90,46.65,12.69,4.13,8.21,905.78,1.62,2.89,2.47,176.15,133.68,107.89,336.55,7.70,2.37,7.51,1.47]],columns =biomarkers)
    df_std=pd.DataFrame(data=        [[8.44,203.44,117.00,7.85,9.20,3.14,6.82,849.74,4333.03,7525.28,42.25,0.17,38.03,1.95,299.10,37.68,16.18,7.66,3.48,3.05,2.84,345.43,0.53,0.52,1.05,20.46,42.37,48.63,153.42,2.30,1.04,2.15,0.48]],columns =biomarkers)
    

    return df, columns,df_average,df_std