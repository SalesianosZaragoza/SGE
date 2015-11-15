package es.salesianos.people;

import es.salesianos.animals.Pet;

public class Kid implements Person{

	public void dardeComer(Pet pet) {
		System.out.println("nino da de comer a su mascota");
		pet.comer();
	}

}
