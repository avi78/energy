import streamlit as st
from pages import sector, unit, station, station_type, region,state, consumer

# Sidebar for selecting pages
selected_page = st.sidebar.radio("Select Dataset", ["Sector","Unit","Region","Station", "Station_type","State", "Consumer"])

# Display content based on selected page
if selected_page == "Sector":
    sector.display_content()
elif selected_page == "State":
    state.display_content()
elif selected_page == "Unit":
    unit.display_content()
elif selected_page == "Region":
    region.display_content()
elif selected_page == "Station":
    station.display_content()
elif selected_page == "Station_type":
    station_type.display_content()
elif selected_page == "Consumer":
    consumer.display_content()