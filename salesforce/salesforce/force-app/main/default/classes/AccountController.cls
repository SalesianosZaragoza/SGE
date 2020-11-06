public with sharing class AccountController {

    /**
     * Set the contact for the page using the email parameter, if there is one
     */
    public AccountController(ApexPages.StandardController controller) {
        // Get the last name from the url
        //String accountNumber = ApexPages.currentPage().getParameters().get('accountNumber');

        //if (accountNumber != null) {
            // Query the object
            //Account account = [SELECT ID FROM Account WHERE AccountNumber = :accountNumber LIMIT 1];

            // this will set the Id, so now you can use the standard controller and just reference fields on the page
            //ApexPages.currentPage().getParameters().put('id', account.Id);
        //}
    }

    public Pagereference goToList(){
        PageReference pr=Page.ListAccounts;
        return pr;
    }

    public Pagereference goToContact(){
        PageReference pr=Page.AddContact;
        return pr;
    }
}
