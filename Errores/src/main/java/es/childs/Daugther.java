package es.childs;

import es.exceptions.WalkException;

public class Daugther implements Children {

	@Override
	public void walk() {
		try {
			throw new WalkException();
		} catch (WalkException e) {
			throw new RuntimeException(e);
		}
	}

}
