({
    myAction : function(component, event, helper) {

    },
    registerScore : function(component, event, helper) {
    var scores = component.get("v.scores");
    var tries = event.getParam("tries");
    var today = new Date();
    var date = today.getDate()+'/'+(today.getMonth()+1)+'/'+today.getFullYear();
    var objeto = {tries: tries, date: date}
    scores.push(objeto);
    component.set("v.scores",scores);
    }
})
