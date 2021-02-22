({
    addToTable : function(component, event, helper) {
         var input = event.getParam("input");
         console.log("recibiendo evento");
         console.log(input);
        if(input){
            var list = Array(component.get("v.output"));
            var objeto = {nombre: input, apellido: "Doe" }
            list.push(objeto);
            component.set("v.output",list);
        }
        console.log(component.get("v.output"));
    },
    deleteAll : function(component, event, helper){
        var ctarget  = event.currentTarget;
        var id = ctarget.dataset.value;
        var child = component.find("child");
        child.deleteItemIdFromSon(id);

    },

})
