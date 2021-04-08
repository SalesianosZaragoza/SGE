({
    guessWord : function(component, event, helper) {
        var word = component.find('word').getElement().value;

        var appevent =$A.get("e.c:guessEvent");
        appevent.setParams({"word":word});
        appevent.fire();
    },

    isGuessed : function(component, event, helper) {
        var coinciden = event.getParam("coinciden");
        var key = event.getParam("key");
        var pista = component.get("v.pista");

        var tries = component.get("v.tries");

        if (coinciden) {
            component.set("v.pista", key);
            component.set("v.status", "Has ganado");

            var appevent =$A.get("e.c:guessedEvent");
            appevent.setParams({"coinciden":coinciden, "tiempo": new Date().toString(), "intentos": tries.toString()});
            appevent.fire();

        } else {

            if (pista.length < key.length) {
                component.set("v.pista", pista.concat(key.charAt(pista.length)));
            }
            tries--;
            component.set("v.tries", tries);
            component.set("v.status", "Has fallado");

            if (tries <= 0) {
                component.set("v.pista", key);
                component.set("v.status", "Has perdido");
            }
        }
    }
})
