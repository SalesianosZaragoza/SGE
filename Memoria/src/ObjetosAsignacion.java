public class ObjetosAsignacion {

	public static void main(String[] args) {
		Persona p; // Definimos Declaramos una variable de tipo puntero que va a
					// recibir una direccion de memoria de un objeto de la clase
					// persona
		Persona q; // Definimos Declaramos una variable de tipo puntero que va a
					// recibir una direccion de memoria de un objeto de la clase
					// persona
		Persona r; // Definimos Declaramos una variable de tipo puntero que va a
					// recibir una direccion de memoria de un objeto de la clase
					// persona

		p = new Persona("Diego"); // Creeamos o instanciamos el objeto, con el
									// nombre
		q = new Persona("Pepe"); // Creeamos o instanciamos el objeto, con el
									// nombre
		r = p; // Asignamos a r el valor de q, es decir, el valor de q es una
				// direccion de memoria de un objeto de la clase Persona

		System.out.println("p: El nombre es:" + p.getNombre());
		System.out.println("q: El nombre es:" + q.getNombre());
		System.out.println("r: El nombre es:" + r.getNombre());
		System.out.println("********************************");

		p = q; // Es como decir que p ahora apunta al objeto al que apunta q

		System.out.println("p: El nombre es:" + p.getNombre());
		System.out.println("q: El nombre es:" + q.getNombre());
		System.out.println("r: El nombre es:" + r.getNombre());
		System.out.println("********************************");

		p.setNombre("Carlos");

		System.out.println("p: El nombre es:" + p.getNombre());
		System.out.println("q: El nombre es:" + q.getNombre());
		System.out.println("r: El nombre es:" + r.getNombre());
		System.out.println("********************************");

		q.setNombre("Lucas");

		System.out.println("p: El nombre es:" + p.getNombre());
		System.out.println("q: El nombre es:" + q.getNombre());
		System.out.println("r: El nombre es:" + r.getNombre());
	}
}