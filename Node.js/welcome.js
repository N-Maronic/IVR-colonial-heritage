exports.handler = function(context, event, callback) {
    let twiml = new Twilio.twiml.VoiceResponse();

    const welcome_message = 'Hello, thank you for participating at identifying and describing objects from Ghana ' 
        + 'that are now displayed in Dutch Museums. For each of the three objects we will ask you three questions. '
        + 'Please answer the questions to the best of your abilities. We will evaluate your recordings and forward '
        + 'our results to the museum, hence they can add new information about the objects to their database. '
        + 'Please note that we will only forward general findings; your responses will be kept anonymous and confidential.'
        + 'If you agree to the previously described terms and you would like to continue with the survey, please press 1.';

    twiml.say(welcome_message);
        
    twiml.gather({
        action: 'https://colonial-heritage-4866.twil.io/object1/question/1',
        finishOnKey: '1'
        });
  
    return callback(null, twiml);
  };