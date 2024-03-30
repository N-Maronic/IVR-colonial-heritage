exports.handler = function(context, event, callback) {
    // setting up some TWiML to respond to with this function
    let twiml = new Twilio.twiml.VoiceResponse();
  
    const welcome_message = 'Hello, thank you for participating in describing objects from Ghana ' 
          + 'that are now displayed in Dutch Museums. Your responses will be kept anonymous and confidential. '
          + 'Only general findings will be shared. If you agree to the previously described terms, ' 
          + 'please say yes and then hit the hash sign.';
  
    // output the message
    twiml.say(welcome_message);
    
    // record the participants response
    twiml.record({
        // redirect to the first question after the participant pressed '#'
        action: 'https://colonial-heritage-4866.twil.io/object1/question/1',
        finishOnKey: '#'
      });
  
    // we return the Twiml voice response after the function was invoked
    return callback(null, twiml);
  };