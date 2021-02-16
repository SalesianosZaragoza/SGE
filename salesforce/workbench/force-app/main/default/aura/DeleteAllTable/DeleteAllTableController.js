({
     deleteAll: function(component, event, helper) {
        //var list = component.get("v.list");
        //list=[];
        //console.log(list);
        //component.set("v.list", list);

        component.set("v.list", []);
    },
    deleteItem: function(component, event, helper){

        var list = component.get("v.list");
        list.remove();
        component.set("v.list", list);
    }
})
