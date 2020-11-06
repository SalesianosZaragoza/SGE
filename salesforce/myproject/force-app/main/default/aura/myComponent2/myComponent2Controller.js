({
    selectNumber:function(component,event,helper){
        var selectedNumber = component.find('select').get('v.value');
        component.set("v.output",selectedNumber);
    
        var appevent =$A.get("e.c:myevent1");
        appevent.setParams({"message":"hey you!"});
        appevent.fire();
    
    },

    callChildMethod : function(component, event, helper){
        var child = component.find("child");
        child.childMethod("i`m dad");
    },

    onInit : function(component, event, helper){
        var attributes={
            "label":"campo de texto",
            "name":"TextField",
            "aura:id":"dynamicInput"
        };
        $A.createComponent("Lightning:input",attributes,function(lightninginput,status,errorMessage){
            if(status==="SUCCESS"){
                var formBody=component.get("v.dynamicForm");
                formBody.push(lightninginput);
                component.set("v.dynamicForm",formBody);
                console.log("SUCCESS");
                console.log(lightninginput);
            }else if(status === "INCOMPLETE"){
                console.log("Error creating component");
            }else if(status === "ERROR"){
                console.log("error "+errorMessage);
            }
        });
    }
    ,

    handleEvent2 : function(component, event){
        var message = event.getParam("message");
        console.log("observer component 2:"+message);
        component.set("v.output2",message);
    },

    myAction : function(component, event, helper) {
        
    }
})
