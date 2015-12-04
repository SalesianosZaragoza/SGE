import org.junit.Test;

import es.childs.Children;
import es.childs.Daugther;
import es.childs.Son;
import es.parents.Mother;
import es.parents.Parent;
import junit.framework.Assert;

public class MotherTest {

	@Test
	public void testMomWithSon() {
		Parent mother = new Mother();
		Children son = new Son();
		MiddleClass clas = new MiddleClass();
		try {
			clas.callFunction(mother, son);
		} catch (Exception e) {
			Assert.fail("Nunca debereia llegar aqui");
		}
	}
	
	@Test
	public void testMomWithDaugther() {
		Parent mother = new Mother();
		Children son = new Daugther();
		MiddleClass clas = new MiddleClass();
		try {
			clas.callFunction(mother, son);
			Assert.fail("Nunca debereia llegar aqui");
		} catch (Exception e) {
		}
	}

}
