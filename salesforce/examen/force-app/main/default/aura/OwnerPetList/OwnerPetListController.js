({
    myAction : function(component, event, helper) {

    },
    addToTable : function(component, event, helper) {
        var data = component.get("v.data");
        var pet = event.getParam("petName");
        var owner = event.getParam("ownerName");
        var objeto = {petName: pet, ownerName: owner}
        data.push(objeto);
    //    data.push({
    //        ownerDni:event.getParam("ownerDni"),
    //        ownerName:event.getParam("ownerName")
    //    })
        component.set("v.data",data);
        },
})
