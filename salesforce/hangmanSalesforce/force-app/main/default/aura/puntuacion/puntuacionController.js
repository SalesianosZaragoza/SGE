({
    myAction : function(component, event, helper) {

    },
    registerScore : function(component, event, helper) {
    //var scores = component.get("v.scores");
    var tries = event.getParam("arguments").tries;
    var today = new Date();
    var date = today.getDate() + '/' + (today.getMonth()+1) + '/' + today.getFullYear();

    var newScore = tries+' - '+date;

    var action = component.get("c.getScoreList");
    action.setParams({"newScore":newScore,"scores":scoreList});
    var scoreList = component.get("v.scores");
    action.setCallback(this, function(response){
        var state = response.getState();
        if(state ==="SUCCESS"){
            console.log(response.getReturnValue());
            component.set("v.scores", response.getReturnValue());
        }
    });
    $A.enqueueAction(action);
}
})
