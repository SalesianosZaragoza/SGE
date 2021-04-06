({
    myAction : function(component, event, helper) {

    },
    sendPetData : function(component, event, helper) {
        var petName = component.find("petName").getElement().value;
        var petChipId = component.find("petChipId").getElement().value;

        var appevent =$A.get("e.c:insertPet");
        appevent.setParams({
            "petName":petName,
            "petChipId":petChipId
        });
        console.log("disparando insert pet event:"+petName+petChipId);
        appevent.fire();
    }
})
