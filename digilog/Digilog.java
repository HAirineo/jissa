public class Digilog{
	public static void main(String[] args) {
		
	}

	static int separate(String expr){
		String val = ""; String dec = "";
		for (int x = 0; x < expr.length(); x++) {
			if (expr.charAt(x) == '.') break;
			else { 
				val += expr.charAt(x);
				dec = expr.substring(expr.indexOf(expr.charAt(x)) + 1, expr.length());
				dec = dec.substring(dec.indexOf(".") + 1, dec.length());
			}
		}
		return Integer.parseInt(val);
	}

	static double decimal(String expr, int base){
		double dec = 0;
		for (int x = 0, y = -1; x < expr.length() && (Math.abs(y) - 1) < expr.length(); x++, y--) {
			dec += (int)(Character.digit(expr.charAt(x), 10)) * Math.pow(base, y);
		}
		return dec;
	}

	static int whole(String expr, int base){
		int whole = 0;
		for (int x = expr.length() - 1, y = 0; x >= 0 && y < expr.length(); x--, y++) {
			whole += (int)(Character.digit(expr.charAt(x), 10) * Math.pow(base, y));
		}
		return whole;
	}
}