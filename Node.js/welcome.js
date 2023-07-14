exports.handler = function(context, event, callback) {
    //create voice response
    let twiml = new Twilio.twiml.VoiceResponse();

    const welcome_message = 'Hello, thank you for participating at identifying and describing objects from Ghana ' 
        + 'that are now displayed in Dutch Museums. For each of the four objects we will ask you three questions. '
        + 'Please answer the questions to the best of your abilities. We will evaluate your recordings and forward '
        + 'our results to the museum, hence they can add new information about the objects to their database. '
        + 'Let\'s get started! Please record your answer after the beep and then hit the pound sign. ';
  
    twiml.say(welcome_message);
  
    //redirect to URL that outputs the first question and records the participants answer
    twiml.redirect('/object1/question/1');
  
    return callback(null, twiml);
  };