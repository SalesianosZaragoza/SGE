public class ListContactController {
 

    public ApexPages.StandardSetController setConTacts {
        get {
            if(setConTacts == null) {
                setConTacts = new ApexPages.StandardSetController(
                    Database.getQueryLocator(
                        [SELECT FirstName, LastName FROM Contact]
                    )
                );
            }
            return setConTacts;
        }
        set;
    }

    // Initialize setCon and return a list of records
    public List<Contact> getcontacts() {
        return (List<Contact>) setConTacts.getRecords();
    }

    public Pagereference goToContact(){
        PageReference pr=Page.AddContact;
        return pr;
    }

      public Pagereference goToAccount(){
        PageReference pr=Page.AddAccount;
        return pr;
    }

}