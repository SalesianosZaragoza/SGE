({
    guessWord : function(component, event, helper) {
        var key = component.get("v.key");
        var word = event.getParam("word");

        var coinciden = key == word;

        var appevent =$A.get("e.c:isGuessedEvent");
        appevent.setParams({"coinciden":coinciden, "key":key});
        appevent.fire();
    },

    setKey : function(component, event, helper) {
        var key = component.find('key').getElement().value;

        component.set("v.key", key);
    },

    guessed : function(component, event, helper) {
        var coinciden = event.getParam("coinciden");
        var tiempo = event.getParam("tiempo");
        var intentos = event.getParam("intentos");

        var child = component.find("child");
        if (coinciden) {
            child.addScoreFromSon(tiempo, intentos);
        }
    }
})
