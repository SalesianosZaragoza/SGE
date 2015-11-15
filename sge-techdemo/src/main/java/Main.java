import es.salesianos.animals.CatImpl;
import es.salesianos.animals.DogImpl;
import es.salesianos.animals.Pet;
import es.salesianos.people.Kid;
import es.salesianos.people.Person;

public class Main {

	public static void main(String[] args) {
		Person kid = new Kid();
		Pet pet = new CatImpl();
		Pet pet2 = new DogImpl();
	
		kid.dardeComer(pet);
		kid.dardeComer(pet2);
		
		//Creamos una clase anonima usando una interfaz
		Pet pet3 = new Pet() {
			
			public void pedir() {
				// TODO Auto-generated method stub
				
			}
			
			public void dormir() {
				// TODO Auto-generated method stub
				
			}
			
			public void comer() {
				// TODO Auto-generated method stub
				
			}
			
			public void cagar() {
				// TODO Auto-generated method stub
				
			}
			
			public void aranar() {
				// TODO Auto-generated method stub
				
			}
		};
	}

}
