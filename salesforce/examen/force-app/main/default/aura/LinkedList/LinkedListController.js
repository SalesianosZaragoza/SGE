({
    myAction : function(component, event, helper) {

    },

    addOwner : function(component, event, helper) {
        var data = component.get("v.data");
        var owner = event.getParam("owner");
        console.log("handler owner:"+owner);

        data.push(owner);
    },

    addPet : function(component, event, helper) {
        var data = component.get("v.data");
        var pet = event.getParam("pet");
        console.log("handler pet:"+pet);
        data.push(pet);
    },


})
