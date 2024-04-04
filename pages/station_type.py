import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to display content of page 1
def display_content():
    # Load the data
    averaged_result = pd.read_csv('/content/drive/MyDrive/YESIST/averaged_results.csv')

    # Combine Year and Month to form a single date column
    averaged_result['Date'] = pd.to_datetime(averaged_result[['Year', 'Month']].astype(int).assign(DAY=1))

    # Sort the DataFrame by Date
    averaged_result.sort_values(by='Date', inplace=True)

    # Plotting
    st.write("### Actual vs Predicted Values over Time")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(averaged_result['Date'], averaged_result['Actual'], label='Actual', color='blue')
    ax.plot(averaged_result['Date'], averaged_result['Predicted'], label='Predicted', color='green')
    ax.set_title('Actual vs Predicted Values over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot
    st.pyplot(fig)
