<div align="center">
<img src="images/logo.webp" alt="screenshot 1" width= "250">
</div>
<h1 align="center">Sunrise-Sunset app</h1>

# Overview
This is a simple command line application which creates a table saved in a text file (`sunrise_sunset.txt`) showing the time of sunset and sunrise on a specific date in a city/country.

# How to install and run
1. Clone the CFG-Assignments repository by typing:<br>
`git clone https://github.com/em-baggie/CFG-Assignments.git`.
2. Ensure all required modules are installed. This can be done by navigating to the project root directory `/assignment-2` and typing:</br>`pip install -r requirements.txt`<br>Alternatively you can install the two required modules using:</br>`pip install tabulate`<br>`pip install requests`.
3. To run the program, navigate to the project root directory `/assignment-2` and type:</br>`python main.py`.
4. Follow the instructions in the program - to enter the program, enter `e`.
5. You will then be prompted to enter a country, a city within that country and a date.
6. The program will return a `sunrise_sunset.txt` file containing a table showing the sunrise/sunset times in UTC for the inputted country/city/time.
7. You then have an option to enter the program again to make another entry to the table by entering `e`, or you can quit the program by entering `q`.

### **Note**:
- The APIs used are free of charge and require no API keys.
- This project could be improved by incorporating error handling and ensuring valid user input.

# APIs used
- <a href= "https://photon.komoot.io/">Photon</a> for obtaining longitude and latitude.
- <a href="https://sunrise-sunset.org/api">Sunrise Sunset API</a> for obtaining sunrise/sunset times.