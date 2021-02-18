public inherited sharing class Manager {
    public Manager() {

    }
    @AuraEnabled
    public static string giveMeUnknownName(){
        return 'John';
    }
}
