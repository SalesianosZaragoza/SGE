({
    myAction : function(component, event, helper) {

    },
    addToTable : function(component, event, helper) {
        var data = component.get("v.data");
        var petChipId = event.getParam("petChipId");
        var petName = event.getParam("petName");
        var objeto = {petChipId: petChipId, petName: petName}
        data.push(objeto);
    //    data.push({
    //        ownerDni:event.getParam("ownerDni"),
    //        ownerName:event.getParam("ownerName")
    //    })
        component.set("v.data",data);
        },
})
