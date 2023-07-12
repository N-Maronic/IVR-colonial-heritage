from flask import Flask, request, url_for
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    response = VoiceResponse()

    message = """Hello, thank you for participating at identifying and describing objects from Ghana that are now displayed in Dutch Museums. 
                 For each of the four objects we will ask you three questions. Please answer the questions to the best of your abilities. 
                 We will evaluate your recordings and forward our results to the museum, hence they can add new information about the objects to their database. """


    response.say(message)
    response.say("Let's get started! Please record your answer after the beep and then hit the pound sign. ")

    # Start with first question for first object
    response.redirect('/question/1/1')

    return str(response)


@app.route("/question/<question_id>/<obj_id>", methods=['POST'])
def question(question_id, obj_id):
    questions = ["What do you see? Please describe the object. ",
                 "According to you, what is the purpose of this object? What could it be used for? ",
                 "Do you know about any rules in terms of how the object needs to be treated? What should, or should not be done with it? "]

    response = VoiceResponse()
    # if not English (but Dagbani), instead of text-to-speech, play wav files stored in twilio assets
        # response.play('https://avocado-ant-4965.twil.io/assets/question%201.mp3')

    i = int(question_id)
    
    output = "Question " + question_id + ": " + questions[i-1]
    response.say(output)
    action_url = url_for('next', question_id=question_id, obj_id=obj_id)
    response.record(action=action_url, finishOnKey='#')

    return str(response)

@app.route("/next/<question_id>/<obj_id>", methods=['POST'])
def next(question_id, obj_id):
    response = VoiceResponse()
    i = int(question_id) + 1
    next_q = str(i)

    if question_id == '3' and obj_id == '4':
        response.say("""Thank you for completing this survey and helping us to get a better understanding
                    for how people perceive colonial heritage objects. The call will now automatically end.""")
        response.hangup()
    elif question_id == '3':
        temp = int(obj_id) + 1
        next_o = str(temp)
        output = "We will now continue with the object number " + next_o + " . Please record your answer after the beep and then hit the pound sign."
        response.say(output)
        response.redirect(url=url_for('question', question_id=1, obj_id=next_o), method='POST')
    else:
        response.redirect(url=url_for('question', question_id=next_q, obj_id=obj_id), method='POST')
    return str(response)


if __name__ == "__main__":
    app.run(debug=True)

# in quickstart:
#   dir *env*
#   . env/bin/activate
#   python3 answer_phone.py
# in new terminal: ngrok http 5000
# copy-paste ngrok link to twilio
