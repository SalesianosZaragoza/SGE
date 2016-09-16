package es.salesianos.filter;

import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.io.IOException;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.Spy;
import org.mockito.runners.MockitoJUnitRunner;


@RunWith(MockitoJUnitRunner.class)
public class IpRangeFilterTest {

	@Spy
	private IpRangeFilter filter = new IpRangeFilter();

	@Mock
	private HttpServletResponse response;

	@Mock
	private HttpServletRequest request;

	@Mock
	private FilterChain chain;

	@Test
	public void testInvalidIpRangeDoFilter() throws IOException, ServletException {
		when(request.getRemoteAddr()).thenReturn("123.123.123.123");
		when(filter.getValidIpRange()).thenReturn("192.168");
		filter.doFilter(request, response, chain);
		verify(chain, times(0)).doFilter(request, response);
	}

	@Test
	public void testValidIpRangeDoFilter() throws IOException, ServletException {
		when(request.getRemoteAddr()).thenReturn("192.168.0.0");
		when(filter.getValidIpRange()).thenReturn("192.168");
		filter.doFilter(request, response, chain);
		verify(chain, times(1)).doFilter(request, response);
	}

	@Test
	public void testEmptyIpRangeDoFilter() throws IOException, ServletException {
		when(request.getRemoteAddr()).thenReturn("192.168.0.0");
		when(filter.getValidIpRange()).thenReturn("");
		filter.doFilter(request, response, chain);
		verify(chain, times(1)).doFilter(request, response);
	}


}
