({
    myAction : function(component, event, helper) {

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
