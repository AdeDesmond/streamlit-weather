
import streamlit  as st
import plotly.express as px
from backend import get_data


st.title("Weather forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value= 1, max_value= 5, help="Select number of forecasted days")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")

if place:
    data = get_data(place=place, forecast_days=days, kind=options) 


    # plotting the chart

    filtered_data = get_data(place=place, forecast_days=days)

    if options == "Temperature":
        temps = [dict_data["main"]["temp"] for dict_data in filtered_data]
        dates = [dict_data["dt_txt"] for dict_data in filtered_data]
        figure = px.line(x=dates, y=temps, labels={"x":"Date", "y":"temperature (C)"})
        st.plotly_chart(figure)

    if options == "Sky":
        images = {
            "Clear":"images/clear.png",
            "Clouds":"images/cloud.png",
            "Rain":"images/rain.png",
            "Snow":"images/snow.png"
        }
        
        sky_conditions = [dict_data["weather"][0]["main"] for dict_data in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)