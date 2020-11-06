public class TrainerController {

    public Trainer__c trainer {get;set;}


    public TrainerController() {
        trainer = new Trainer__c();
    }

    public Pagereference save(){
        try {
            insert trainer;
        } catch(System.DMLException e) {
            ApexPages.addMessages(e);
            System.debug('An unexpected error has occurred: ' + e.getMessage());
            return null;
        }
        return null;    
    }

    public Pagereference goToTrainerList(){
        PageReference pr=Page.ListTrainer;
        return pr;
    }
}
