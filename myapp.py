import pickle  # Added import statement
#import yfinance as yf
import streamlit as st
import numpy as np
from datetime import date, datetime

# Load the pre-trained model
with open("sales_forecasting_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def main():
    st.title("Sales Forecasting Application")
    st.write("""
    This app predicts future sales based on the input data provided.
    Please enter the necessary details below to get the forecasted sales.
    """)

    # User input fieldsdate = st.date_input("Enter Date:", value=datetime.today())
    #Holiday_Flag= st.text_input("Holiday_Flag:", value="")
    Tempertuture= st.text_input("Tempertuture:", value="")
    CPI= st.text_input("CPI:", value="")
    Fuel_Price= st.text_input("Fuel_Price:", value="")
    Unemployment= st.text_input("Unemployment:", value="")
    Date= st.date_input("Enter Date:", value=datetime.today())

    

    if st.button("Get Forecast"):
        # Validate inputs
        if   Tempertuture.strip() and CPI.strip() and Fuel_Price.strip() and Unemployment.strip() and Date.strip():
            try:
                # Convert ID
                #Holiday_Flag=bool(Holiday_Flag)
                Tempertuture=float(Tempertuture)
                CPI = float(CPI)
                Fuel_Price= float(Fuel_Price)
                Unemployment=float(Unemployment)

                
                # Extract date components
                year = date.year
                month = date.month
                day = date.day
                
                # Prepare feature array (adjust based on model requirements)
                features = np.array([[Tempertuture,CPI,Fuel_Price,Unemployment]])
                
                # Make prediction
                forecast = model.predict(features)
                st.success(f"Forecasted Sales: ${forecast[0]:.2f}")
            
            except ValueError:
                st.error("Store ID and Product ID must be numeric values.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please fill in all the inputs.")

if __name__ == "__main__":
    main()
