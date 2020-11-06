public with sharing class ContactController {

    /**
     * Set the contact for the page using the lastName parameter, if there is one
     */
    public ContactController(ApexPages.StandardController controller) {
        // Get the last name from the url
        //String lastName = ApexPages.currentPage().getParameters().get('lastName');

        //if (lastName != null) {
            // Query the object
            //Contact theContact = [SELECT ID FROM Contact WHERE LastName = :lastName LIMIT 1];

            // this will set the Id, so now you can use the standard controller and just reference fields on the page
            //ApexPages.currentPage().getParameters().put('id', theContact.Id);
        //}
    }

    public Pagereference goToList(){
        PageReference pr=Page.ListContacts;
        return pr;
    }

      public Pagereference goToAccount(){
        PageReference pr=Page.AddAccount;
        return pr;
    }

}
