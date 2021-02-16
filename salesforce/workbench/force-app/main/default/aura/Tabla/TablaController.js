({
    addToTable : function(component, event, helper) {
         var input = event.getParam("input");
         console.log("recibiendo evento");
         console.log(input);
        if(input){
            var list = component.get("v.output");
            list.push(input);
            component.set("v.output",list);
        }
        console.log(component.get("v.output"));
    },
    deleteAll : function(component, event, helper){
        var child = component.find("child");
        child.deleteItemFromSon(id);

    },

})
