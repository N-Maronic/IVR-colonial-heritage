exports.handler = function(context, event, callback) {
    let twiml = new Twilio.twiml.VoiceResponse();
    const question = 'Question 3: Do you know about any rules in terms of how the object needs to be treated? What should, or should not be done with it? ';
  
    twiml.say(question);
    twiml.record({
        action: 'https://colonial-heritage-4866.twil.io/goodbye',
        finishOnKey: '#',
        transcribe: true
    });
  
    return callback(null, twiml);
};