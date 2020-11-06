public class TestController {

    public TEST__c test {get;set;}

    public TestController() {
        test = new TEST__c();
    }

    public Pagereference save(){
        try {
            insert test;
        } catch(System.DMLException e) {
            ApexPages.addMessages(e);
            System.debug('An unexpected error has occurred: ' + e.getMessage());
            return null;
        }
        return null;    
    }

   



}
