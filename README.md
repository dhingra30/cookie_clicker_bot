# Cookie Clicker Automation Script
This Python script uses Selenium to automate gameplay in the popular web-based game Cookie Clicker. The script performs the following tasks:

1. **Automated Cookie Clicking**: Continuously clicks the cookie to accumulate cookies.
2. **Item Purchasing**: Periodically checks the available in-game currency and purchases the most cost-effective items to optimize gameplay.

__Features__
- **Automated Item Buying**: Identifies and buys items based on the available amount of in-game currency.
- **Scheduled Execution**: Uses the schedule library to perform item purchasing tasks every 10 seconds.
- **Dynamic Price Handling**: Parses and processes item prices dynamically from the game's web interface.
- **Real-Time Feedback**: Prints the cookies per second (CPS) rate to track progress.

__How It Works__
> **Setup**: Configures and initializes the Chrome WebDriver for browser automation. 
> **Navigation**: Opens the Cookie Clicker game page. 
> **Element Interaction**: Locates and interacts with the game elements such as the cookie and item buttons. 
> **Price Parsing**: Extracts and converts item prices from the web page. 
> **Automated Tasks**: Clicks the cookie and buys items based on current game state in a loop running for 5 minutes.

__Requirements__
1. Python 3.x 
2. Selenium 
3. ChromeDriver (or appropriate WebDriver for your browser)

__Installation__
1. Clone the repository:
```git clone https://github.com/dhingra30/cookie_clicker_bot.git```
2. Install the required Python packages:
```pip install selenium schedule```
3. Download and set up ChromeDriver or your preferred WebDriver.

__Usage__
Run the script using:
```python script.py```

__Notes__
Make sure to update the path to the ChromeDriver executable in the script.
The script is designed for educational and experimental purposes.
Feel free to contribute or suggest improvements!


