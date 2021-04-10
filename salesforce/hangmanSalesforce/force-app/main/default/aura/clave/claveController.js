({
    myAction : function(component, event, helper) {
        
    },
    generateWord: function(component, event, helper){
        let wordList =["patata","tomate", "mesa", "aprobado"];
        const randomWord = wordList[Math.floor(Math.random() * wordList.length)];
        
        var appevent =$A.get("e.c:sendWord");
        appevent.setParams({
            "word":randomWord
        });
        console.log("disparando sendWord event:"+randomWord);
        appevent.fire();
    }

})
