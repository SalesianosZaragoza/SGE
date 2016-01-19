public class ObjetosParametros {

	public static void main(String[] args) {

		Persona p; // Definimos Declaramos una variable de tipo puntero que va a
					// recibir una direccion de memoria de un objeto de la clase
					// Persona

		p = new Persona(); // Creeamos o instanciamos el objeto

		p.setNombre("Diego"); // le asignamos un nombre
		System.out.println("El nombre antes del método es:" + p.getNombre());

		cambiarNombre1(p);
		// pasamos al metodo el objeto p, es decir, enviamos el valor que
		// almacena la variable p, una direccion de memoria de un objeto de la
		// clase Persona
		System.out.println("El nombre después del método es:" + p.getNombre());

		/*********************************************************************/
		System.out.println("************************************************");
		System.out.println("************************************************");
		/*********************************************************************/

		Persona q; // Definimos Declaramos una variable de tipo puntero que va a
		// recibir una direccion de memoria de un objeto de la clase
		// Persona

		q = new Persona(); // Creeamos o instanciamos el objeto

		q.setNombre("Carlos"); // le asignamos un nombre
		System.out.println("El nombre antes del método es:" + q.getNombre());

		cambiarNombre2(q);
		// pasamos al metodo el objeto q, es decir, enviamos el valor que
		// almacena la variable q, una direccion de memoria de un objeto de la
		// clase Persona
		System.out.println("El nombre después del método es:" + q.getNombre());
	}

	private static void cambiarNombre1(Persona p) {
		// Aqui se define una variable de tipo puntero llamada "p" y es local
		// que va a recibir una direccion de memoria de un objeto de la clase
		// persona.
		// Como valor va a recibir la direccion de memoria del objeto p de
		// arriba (linea 9).
		// Es decir esta variable p local va a apuntar al mismo objeto que
		// apunta la variable p global de arriba

		p = new Persona();
		// p, que es local, ahora recibe una nueva direccion de un objeto de la
		// clase persona, por lo tanto ahora p apunta a un nuevo objeto de la
		// clase persona

		p.setNombre("Santiago"); // le asignamos un nombre
		System.out.println("El nombre en el método es:" + p.getNombre());
	}

	private static void cambiarNombre2(Persona q) {
		// Aqui se define una variable de tipo puntero llamada "q" y es local
		// que va a recibir una direccion de memoria de un objeto de la clase
		// persona.
		// Como valor va a recibir la direccion de memoria del objeto q de
		// arriba (linea 9).
		// Es decir esta variable q local va a apuntar al mismo objeto que
		// apunta la variable q global de arriba

		q.setNombre("Pepito"); // Le asignamos un nombre
		System.out.println("El nombre en el método es:" + q.getNombre());

		// Como la variable q local apunta al mismo objeto que la variable
		// global q, un cambio en q local tambien afecta a la variable q global
		// porque ambas tienen la direccion de memoria del mismo objeto
	}

}
