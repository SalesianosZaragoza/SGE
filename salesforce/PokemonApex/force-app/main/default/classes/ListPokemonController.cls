public class ListPokemonController{
 
    public List<POKEMON__c> pokemons {get;set;}

    public ListPokemonController() {
        pokemons = [
            SELECT ID__c, Name__c,Life__c, Attack__c, TrainerID__c 
            FROM POKEMON__c 
            ORDER BY Pokemon_ID__c];
    }


    public Pagereference goToPokemon(){
        PageReference pr=Page.AddPokemon;
        return pr;
    }
}