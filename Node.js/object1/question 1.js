exports.handler = function(context, event, callback) {
    let twiml = new Twilio.twiml.VoiceResponse();
    const obj1 = 'Let\'s begin with object number 1 in the red frame.';
    const question = 'Question 1: What do you see? Please describe the object. ';
  
    twiml.say(question);
    //or using asset: twiml.play('https://colonial-heritage-4866.twil.io/question%201.mp3')
    
    //record the participants answer and continue with question 2 (object 1)
    twiml.record({
        action: 'https://colonial-heritage-4866.twil.io/object1/question/2',
        finishOnKey: '#',
        transcribe: true
    });
  
    return callback(null, twiml);
  };