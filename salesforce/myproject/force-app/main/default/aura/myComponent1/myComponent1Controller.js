({
    callControllerJs : function(component, event, helper) {
        helper.changeMyVariable(component, event);
    },

    callAura : function(component, event, helper) {
        console.log("estoy pintqndo la pared");
        helper.callAuraMethod(component, event);
    },

    handleEvent1 : function(component, event){
        var message = event.getParam("message");
        console.log("observer component 1:"+message)
        component.set("v.myvariable",message)
    },

    handleSubmit : function(component, event, helper){

    },

    callExternalUrl : function(component, event, helper){
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = $A.getCallback(function(){
            if(this.readyState===4){
                if(xhttp.status === 200){
                    console.log(xhttp.responseText);
                    var response = JSON.parse(xhttp.responseText);
                    console.log(response);
                    var mapa = new Map();
                    mapa.set("bitcoin_dominance_percentage",response.bitcoin_dominance_percentage);
                    component.set("v.mapa",mapa)
                    console.log("vmapa"+mapa);
                }
            }
        });
        //csp trusted definition
        xhttp.open("GET","https://api.coinpaprika.com/v1/global");
        //debe ir despues del open
        xhttp.setRequestHeader('Access-Control-Allow-Headers','Accept');
        xhttp.setRequestHeader('Access-Control-Allow-Origin','*');
        xhttp.send(null);

    },
    
    showAlert : function (cmp, event, helper) {
        alert("You clicked: " + event.getSource().get("v.label"));
        alert("zona horaria:"+$A.get("$Locale.timezone"));
        alert("moneda:"+$A.get("$Locale.currency"));
    }
})
