({
    myAction : function(component, event, helper) {

    },
addToTable : function(component, event, helper) {
    var data = component.get("v.data");
    var dni = event.getParam("ownerDni");
    var name = event.getParam("ownerName");
    var objeto = {ownerDni: dni, ownerName: name}
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
       
        var appevent =$A.get("e.c:linkOwner");

        appevent.setParams(itemToLink);
        console.log("link owner event:"+itemToLink);
        appevent.fire();
    },
})
