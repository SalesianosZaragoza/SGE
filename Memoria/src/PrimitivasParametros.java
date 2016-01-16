
public class PrimitivasParametros {

	public static void main(String[] args) {
        int a = 10, b = 20;  // Declaro y asigno valores
        System.out.println("Valores antes de cambiar");
        System.out.format("a=%d, b=%d\n", a, b); // Imprime a=10, b=20
        
        cambiandoValores(a, b); // Cambia de valores
 
        System.out.println("Valores después de cambiar");
        System.out.format("a=%d, b=%d\n", a, b); // Imprime a=10, b=20
    }
 
    private static void cambiandoValores(int a, int b) { // Se declaran nuevas variables locales ( a, b ) y como valor reciben los valores enviados
    	System.out.println("Valores metodo antes del cambio");
        System.out.format("a=%d, b=%d\n", a, b); // Imprime a=10, b=20
        a = 100;
        b = 200;
        System.out.println("Valores cambiados en el método");
        System.out.format("a=%d, b=%d\n", a, b); // Imprime a=100, b=200
    }
}

/*
 *
 * Valores antes de cambiar
 * a=10, b=20
 * Valores metodo antes del cambio
 * a=10, b=20
 * Valores cambiados en el método
 * a=100, b=200
 * Valores después de cambiar
 * a=10, b=20
 * 
 */