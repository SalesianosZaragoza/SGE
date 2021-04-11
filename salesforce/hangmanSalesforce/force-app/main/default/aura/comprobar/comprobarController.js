({
    myAction : function(component, event, helper) {

    },
    setWord : function(component, event, helper) {
        //Set tries to 0 everytime we reset the game
        component.set("v.tries",0);

        var wordToGuess = event.getParam("word");
        component.set("v.wordToGuess",wordToGuess);
    },
    sendWord : function(component, event, helper) {
        var wordInput = component.find("wordInput").getElement().value;

        var appevent =$A.get("e.c:sendWord");
        appevent.setParams({
            "word":wordInput
        });
        console.log("disparando sendWord event:"+wordInput);
        appevent.fire();
    },

})
