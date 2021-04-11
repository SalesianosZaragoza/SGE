({
    myAction : function(component, event, helper) {

    },
    setWord : function(component, event, helper) {
        //Set tries to 0 everytime we reset the game
        component.set("v.tries",0);

        var wordToGuess = event.getParam("word");
        component.set("v.wordToGuess",wordToGuess);
    },
    checkWord : function(component, event, helper) {
        //Increment tries
        var tries = component.get("v.tries");
        tries++;
        component.set("v.tries",tries);

        //Checking word
        var wordToGuess = component.get("v.wordToGuess");
        var wordToCheck = component.find("wordInput").getElement().value;

        if(wordToCheck === wordToGuess){
            console.log('Ole tu hueva sosio');
        }else{
            var hint = component.get("v.hint");
            hint = wordToGuess.charAt(Math.floor(Math.random() * wordToGuess.length));
            component.set("v.hint",hint);
        }

    },

})
