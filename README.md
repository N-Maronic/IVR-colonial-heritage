# IVR colonial heritage
This is a project conducted in fulfillment of the requirements for the Honours Programme at the Vrije Universiteit Amsterdam, which is an excellence annotation to the VU Bachelor of Science degree in Computer Science.

## About the project
The aim of this project is to use crowdsourcing techniques to tag objects from the colonial period exhibited in Dutch museums.
We created a IVR (interactive voice response) system to gather information about colonial heritage objects that are originally from Ghana, and that are now exhibited in the Wereldculturen Collectie. We are using the [Twilio platform](https://www.twilio.com/en-us), which offers a Voice API to create a personalized voice interface.

## Installation Guide

Note: We are assuming you have a valid Twilio account.

The next two sections show step-by-step how to set up the IVR. The first option is using Python and running on a webhook connected to your local machine. The second option, is using the Twilio Service, including functions and assets, which runs on the Node.js engine.

### Python
Run the app locally following these steps:

  1. Clone this repository and `cd` into it.
  2. Install a virtualenv with
     ``` bash
     pip install virtualenv
     ```
  4. Create the virtual environment with
     ```bash
     virtualenv env
     ```
  6. Activate the virtual environement with
     ```bash
     source env/bin/activate
     ```
  8. Install the dependencies with
     ```bash
     pip install -r reqs.txt
     ```
  9. Execute answer_phone.py with
     ```bash
     python3 answer_phone.py
     ```
  10. In a new terminal run
      ```bash
      ngrok http 5000
      ```
      to create a Webhook to your locally running application. You can find more information about ngrok [here](https://ngrok.com/)
  11. Copy-paste the ngrok link to your Twilio console

Now your server, and consequently your IVR, is up and running. 

### Node.js
   1. Create a new Service in your Twilio Functions and Assets ([documentation](https://www.twilio.com/docs/serverless/functions-assets/functions/create-service))
   2. Copy-paste the JavaScript files from the Node.js folder in function files in your Twilio Functions and Assets ([documentation](https://www.twilio.com/docs/serverless/functions-assets/functions))
   3. Deploy your Service
   4. Copy-paste the URL to your Twilio Console ![Screenshot Twilio Voice Configuration](/Screenshots/Voice_Configuration.png)

## Testing
### Python
To check whether the Webhook correctly routes to your localhost, simply paste the ngrok URL in your browser of choice.

### Both implementations
To test the voice application, simply call your Twilio number. The recordings of the call can then be found under 'Call Logs' on your Twilio console.
![Screenshot Twilio Call Details](/Screenshots/Call_Details.png)

## Retrieving recordings and transcripts
In order to store links to the recorded calls and the respective transcripts in a local spreadsheet, simply execute the 'retrieveCalls.py' file after the following steps:
   1. Save your Twilio SID and authentication token in the twilio.env file to set the environment parameters
   2. execute ```source ./twilio.env``` in the terminal 
