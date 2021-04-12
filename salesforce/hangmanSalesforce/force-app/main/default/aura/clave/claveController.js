({
    myAction : function(component, event, helper) {
        
    },
    generateWord: function(component, event, helper){
        let wordList =["patata","tomate", "mesa", "aprobado"];
        const randomWord = wordList[Math.floor(Math.random() * wordList.length)];
        component.set("v.wordToGuess",randomWord);
    },

    checkWord : function(component, event, helper) {
        
        //Increment tries
        var tries = component.get("v.tries");
        tries++;
        component.set("v.tries",tries);

        //Checking word
        var wordToGuess = component.get("v.wordToGuess");
        var wordToCheck = event.getParam("word");

        if(wordToCheck === wordToGuess){            
            var child = component.find('child');
            child.insertScore(tries);
            component.set("v.message", "HAS ACERTADOOO!");
        }else{
            var hint = component.get("v.hint");
            hint = wordToGuess.charAt(Math.floor(Math.random() * wordToGuess.length));
            component.set("v.hint",hint);
            component.set("v.message", "Prueba otra vez");
        }   
    }
})
