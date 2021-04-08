({
    myAction : function(component, event, helper) {

    },
    addToPets : function(component, event, helper) {
        var pets = component.get("v.pets");
        var chip = event.getParam("petChipId");
        var name = event.getParam("petName");
        var objeto = {petName: name, petChipId: chip}
        pets.push(objeto);
        component.set("v.pets",pets);
        },
        addToOwners : function(component, event, helper) {
            var owners = component.get("v.owners");
            var dni = event.getParam("OwnerDni");
            var name = event.getParam("ownerName");
            var objeto = {ownerName: name, ownerDni: dni}
            owners.push(objeto);
            component.set("v.owners",owners);
            },
            sendLinkData : function(component, event, helper) {
                var owner = component.find("selectOwner").get("v.value");
                var pet = component.find("selectPet").get("v.value");
        
                var appevent =$A.get("e.c:doLink");
                appevent.setParams({
                    "ownerName":owner,
                    "petName":pet
                });
                console.log("disparando link event:"+owner+pet);
                appevent.fire();
            }
})
