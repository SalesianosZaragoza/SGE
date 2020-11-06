public class PokemonController {

    public Pokemon__c pokemon {get;set;}


    public PokemonController() {
        pokemon = new Pokemon__c();
    }

    public Pagereference save(){
        try {
            insert pokemon;
        } catch(System.DMLException e) {
            ApexPages.addMessages(e);
            System.debug('An unexpected error has occurred: ' + e.getMessage());
            return null;
        }
        return null;    
    }

    public Pagereference goToPokemonList(){
        PageReference pr=Page.ListPokemon;
        return pr;
    }
}
