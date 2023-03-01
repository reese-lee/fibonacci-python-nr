# Sample Python fibonacci app that's been instrumented with the New Relic APM agent. 

To run:

1. Install the requirements: `pip3 install -r requirements.txt` 
2. Input your license key in the newrelic.ini file, line 30
3. Run the agent with the program: `NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-python main.py` 
4. To exercise traffic to the program, simply run this command in your terminal a few times. 
5. Head to your NR account to view the data.
