({
     deleteAll: function(component, event, helper) {
        //var list = component.get("v.list");
        //list=[];
        //console.log(list);
        //component.set("v.list", list);

        component.set("v.list", []);
    },
    deleteItem: function(component, event, helper){
        var id = event.getParam("arguments").id;
        var list = component.get("v.list");
        list.splice(id,1);
        component.set("v.list", list);
    },
    changeName: function(component, event, helper){
        var ctarget  = event.currentTarget;
        var id = ctarget.dataset.value;   
        var list =component.get("v.list");
        var itemToUpdate = list[id];
        console.log("cambiando nombre a:"+itemToUpdate );
        var action =component.get("c.giveMeUnknownName");
        action.setCallback(this, function(response){
            var state = response.getState();
            if(state==="SUCCESS"){
                console.log(itemToUpdate);
                itemToUpdate.nombre= response.getReturnValue();
                itemToUpdate.edad=18;
                component.set("v.list",list);                
            }

        });
        $A.enqueueAction(action);

        }
    
})
