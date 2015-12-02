import org.junit.Test;

import es.childs.Children;
import es.childs.Son;
import es.parents.Mother;
import es.parents.Parent;

public class MotherTest {

	@Test
	public void testMom() {
		Parent mother = new Mother();
		Children son = new Son();
		MiddleClass clas = new MiddleClass();
		clas.callFunction(mother, son);
	}

}
