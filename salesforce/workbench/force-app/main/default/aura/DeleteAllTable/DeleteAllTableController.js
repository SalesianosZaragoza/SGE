({
     deleteAll: function(component, event, helper) {
        //var list = component.get("v.list");
        //list=[];
        //console.log(list);
        //component.set("v.list", list);

        component.set("v.list", []);
    },
    deleteItem: function(component, event, helper){
        var id = event.getParam("id")
        var list = component.get("v.list");
        list.remove(id);
        component.set("v.list", list);
    },
    changeName: function(component, event, helper){
        var id = event.target.itemid;      
        var list =component.get("v.list");
        var itemToUpdate = list.get(id);
        var action =component.get("c.giveMeUnknownName");
        action.setCallback(this, function(response){
            var state = response.getState();
            if(state==="SUCCESS"){
                itemToUpdate.nombre= response.getReturnValue();
                list.push(itemToUpdate);
                component.set("v.list",list);                
            }

        });
        $A.enqueueAction(action);

        }
    
})
