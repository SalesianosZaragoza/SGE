package es.salesianos.filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;


public class IpRangeFilter implements Filter {

	private String validIpRange;

	public void init(FilterConfig filterConfig) throws ServletException {
		validIpRange = filterConfig.getInitParameter("validIpRange");
	}

	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		if (isValidIp(request))
			chain.doFilter(request, response);
	}

	public void destroy() {
	}

	private boolean isValidIp(ServletRequest request) {
		boolean valid = true;
		String validIpRange = getValidIpRange();
		if (!validIpRange.isEmpty()) {
			String[] ipRange = validIpRange.split("\\.");
			String[] ipReal = request.getRemoteAddr().split("\\.");
			for (int i = 0; i < ipRange.length; i++) {
				if (!ipRange[i].equals(ipReal[i])) {
					valid = false;
				}
			}
		}
		return valid;
	}

	public String getValidIpRange() {
		return validIpRange;
	}


}
