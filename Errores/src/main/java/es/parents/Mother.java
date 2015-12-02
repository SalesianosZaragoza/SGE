package es.parents;

import es.childs.Children;

public class Mother implements Parent {

	public void feed(Children children) {
		children.walk();
		System.out.println("dando de comer a mi hijo");
	}

}
