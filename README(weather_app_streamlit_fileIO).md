Weather Application with Streamlit, OpenWeatherMap API and FILE I/O

Overview
This Python application fetches real-time weather data using the OpenWeatherMap API and displays it via a Streamlit web interface. 
Users can select a city from a predefined list, view current weather conditions such as temperature, humidity, wind speed, and direction.
City descriptions are sourced from a text file for additional context.

Features
Displays current weather information for selected cities.
Dynamic updates based on user input.
Error handling for file operations and API requests.
Responsive UI built using Streamlit.

Setup
Clone the repository
cd weather-application
Install dependencies: Use pip install for installing dependencies

Obtain API key:
Sign up for a free API key at OpenWeatherMap.
Replace 'Your API Key' in get_weather() function with your API key.

Run the application:
streamlit run weather_app.py

File Structure
weather_app.py: Main application script using Streamlit.
cities.txt: Text file containing city names and descriptions.

Usage
Select a city from the dropdown menu.
Weather details and city description will be displayed.
Handle errors gracefully if city not found or API request fails.

Contributor
Anmol Kumar Srivastava (dArKmOLeS)

License
This project is licensed under the MIT License - see the LICENSE file for details.
