package es.childs;

import es.exceptions.CrawlException;

public class Nephew implements Children {

	@Override
	public void walk() {
		throw new CrawlException();

	}

}
