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
    link : function(component, event, helper) {

        var ctarget  = event.currentTarget;
        var id = ctarget.dataset.value;   
        var list =component.get("v.data");
        var itemToLink = list[id];
        console.log("cambiando nombre a:"+itemToLink );
       
        var appevent =$A.get("e.c:linkPet");

        appevent.setParams(itemToLink);
        console.log("link pet event:"+itemToLink);
        appevent.fire();
    },
})
