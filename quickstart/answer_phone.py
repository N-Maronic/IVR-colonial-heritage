from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    response = VoiceResponse()

    message = """Hello, thank you for participating at identifying and describing objects from Ghana that are now displayed in Dutch Museums. 
                 For each of the five objects we will ask you four questions. Please answer the questions to the best of your abilities. 
                 After every question, we will record your answer for at most 2 minutes. 
                 If you are done earlier, you can press zero to continue with the next question. 
                 We will evaluate your recordings and forward our results to the museum, hence they can add new information about the objects to their database. """


    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            # response.say("you chose one")
            survey(response)
            return str(response)
        else:
            response.say("Sorry, I don't understand that choice.")
    else:
        response.say(message)

    # Start our <Gather> verb
    gather = Gather(num_digits=1)
    gather.say('Press one, to start with the first object.')
    response.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    response.redirect('/welcome')
    
    return str(response)


# private methods

def survey(response):
    questions = ["What do you see? Please describe the object.",
                 "According to you, what is the purpose of this object? What could it be used for?",
                 "Do you know about any rules in terms of how the object needs to be treated? What should, or should not be done with it?"]

    response.say("Let's get started! Press zero when you finished.")

    for j in range(1,5):
        for i in range(1,4):
            output = "Question " + str(i) + ": " + questions[i-1]
            response.say(output)
            # response.record(max_length=2)

        if j != 4:
            next_object = "Thank you for answering all questions about the object " + str(j) +  ". We will now continue with the next object."
        response.say(next_object)

    response.say("""Thank you for completing this survey and helping us to get a better understanding
                    for how people perceive colonial heritage objects. The call will now automatically end.""")

    response.hangup()
    return response



@app.route("/test", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Test for hp project", voice='alice')

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/test')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# in quickstart env:
#   dir *env*
#   . env/bin/activate
#   python3 answer_phone.py
# in new terminal: ngrok http 5000
# copy-paste ngrok link to twilio