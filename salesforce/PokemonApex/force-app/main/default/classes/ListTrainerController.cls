public class ListTrainerController{
 
    public List<TRAINER__c> trainers {get;set;}

    public ListTrainerController() {
        trainers = [SELECT ID__c, Name__c FROM TRAINER__c ORDER BY ID__c];
    }


    public Pagereference goToTrainer(){
        PageReference pr=Page.AddTrainer;
        return pr;
    }
}