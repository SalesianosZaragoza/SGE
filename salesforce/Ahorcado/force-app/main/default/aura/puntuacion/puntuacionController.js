({
    addScore : function(component, event, helper) {
        var tiempo = event.getParam("arguments").tiempo;
        var intentos = event.getParam("arguments").intentos;

        var action = component.get("c.addScoreboard");
        action.setParams({"tiempo": tiempo, "intentos": intentos});
        action.setCallback(this, function(response){
            var state = response.getState();
            if(state==="SUCCESS"){
                var scoreboard = response.getReturnValue();
                component.set("v.scoreboard", scoreboard);                
            }

        });
        $A.enqueueAction(action);
    }
})
