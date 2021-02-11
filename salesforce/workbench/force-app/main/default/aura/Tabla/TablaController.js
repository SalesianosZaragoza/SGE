({
    addToTable : function(component, event, helper) {
         var params = event.getParam("arguments");
         console.log("recibiendo evento");
         console.log(params);
        if(params){
            var list = component.get("v.output");
            list.push(params.input);
            component.set("v.output",list);
        }
        console.log(component.get("v.output"));
    }

})
