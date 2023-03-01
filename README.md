This repo holds a simple Python script that has been instrumented as a background job with the New Relic Python APM agent. 

To run:

1. Install the requirements: `pip3 install -r requirements.txt` 
2. Input your license key in the newrelic.ini file, line 30
3. Run the agent with the program: `NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-python main.py`
