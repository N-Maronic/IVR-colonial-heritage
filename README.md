# HP-Project
This is a project conducted in fulfillment of the requirements for the Honours Programme at the Vrije Universiteit Amsterdam, which is an excellence annotation to the VU Bachelor of Science degree in Computer Science.

## About the project
The aim of this project is to use crowdsourcing techniques to tag objects from the colonial period exhibited in Dutch museums.
We created a IVR (interactive voice response) system to gather information about colonial heritage objects that are originally from Ghana, and that are no exhibited in the Wereldculturen Collectie. We are using the [Twilio platform](https://www.twilio.com/en-us), which offers a Voice API to create a personalized voice interface.

## Build status
This project is still under development. More specifically, we are still working on including Dagbani as a language option for the survey. 

## Installation Guide (for python3)
Note: We are assuming you have a valid Twilio account.

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

Now your server, and consequently your IVR, is up an running. 

## Testing
To check whether the Webhook correctly routes to your localhost, simply paste the ngrok URL in your browser of choice.

To test the voice application, simply call your Twilio number. The recordings of the call can then be found under 'Call Logs' on your Twilio console.
