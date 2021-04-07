({
    myAction : function(component, event, helper) {

    },
    sendOwnerData : function(component, event, helper) {
        var name = component.find("ownerName").getElement().value;
        var dni = component.find("ownerDni").getElement().value;

        var appevent =$A.get("e.c:insertOwner");
        appevent.setParams({
            "ownerName":name,
            "ownerDni":dni
        });
        console.log("disparando insert owner event:"+name+dni);
        appevent.fire();
    }
})
