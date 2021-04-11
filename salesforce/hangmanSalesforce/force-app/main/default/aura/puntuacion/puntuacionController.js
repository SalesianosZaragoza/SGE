({
    myAction : function(component, event, helper) {

    },
    registerScore : function(component, event, helper) {
    var scores = component.get("v.scores");
    var tries = event.getParam("arguments").tries;
    var today = new Date();
    var date = today.getDate()+'/'+(today.getMonth()+1)+'/'+today.getFullYear();
    var newScore = {tries: tries, date: date}
    scores.push(newScore);
    component.set("v.scores",scores);
    }
})
