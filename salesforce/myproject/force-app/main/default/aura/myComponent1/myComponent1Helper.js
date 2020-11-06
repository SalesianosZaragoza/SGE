({
    changeMyVariable : function(component,event){
        console.log(event);
        console.log(component);
        component.set("v.myvariable","componente1");
    },

    callAuraMethod : function(component, event) {
        var userInput = component.find('userInput').getElement().value;
              
        var action =component.get("c.callWithParam");
        action.setParams(
            
            {msg:" buenos dias"}
            
            );

        action.setCallback(this, function(response){
            var state = response.getState();
            if(state==="SUCCESS"){
                component.set("v.myvariable",userInput+response.getReturnValue());                
            }
            if(state==="INCOMPLETE"){
            }
            if(state==="ERROR"){
                var errors = response.getError();
                if(errors){
                    if(errors[0] && errors[0].message ){
                        console.log(errors[0].message);
                    }
                    component.set("v.myvariable","error");
                }
            }

        });
        $A.enqueueAction(action);

        console.log("antes");
    }
})
