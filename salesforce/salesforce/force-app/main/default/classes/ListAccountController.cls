public class ListAccountController {
 

    public ApexPages.StandardSetController setAccount {
        get {
            if(setAccount == null) {
                setAccount = new ApexPages.StandardSetController(
                    Database.getQueryLocator(
                        [SELECT AccountNumber, Site FROM Account]
                    )
                );
            }
            return setAccount;
        }
        set;
    }

    // Initialize setCon and return a list of records
    public List<Account> getAccounts() {
        return (List<Account>) setAccount.getRecords();
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