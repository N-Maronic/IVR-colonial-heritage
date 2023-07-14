exports.handler = function(context, event, callback) {
    let twiml = new Twilio.twiml.VoiceResponse();
    const question = 'Question 2: According to you, what is the purpose of this object? What could it be used for?  ';
  
    twiml.say(question);
    twiml.record({
        action: 'https://colonial-heritage-4866.twil.io/object2/question/3',
        finishOnKey: '#'
    });
  
    return callback(null, twiml);
  };