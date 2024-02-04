exports.handler = function(context, event, callback) {
    let twiml = new Twilio.twiml.VoiceResponse();
    const question = 'Question 2: According to you, what is the purpose of this object? What could it be used for?  ';
  
    twiml.say(question);
    twiml.record({
        action: 'https://colonial-heritage-4866.twil.io/object1/question/3',
        finishOnKey: '#',
        transcribe: true
    });
  
    return callback(null, twiml);
  };