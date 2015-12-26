import java.util.HashMap;
import java.util.Set;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

public class Digilog{
	public static void main(String[] args) {
		HashMap map = new HashMap();
		map = separate("123.456");
		Set set = map.entrySet();
		Iterator i = set.iterator();
		while(i.hasNext()){
			Map.Entry me = (Map.Entry)i.next();
			System.out.println(me.getValue());
		}
	}

	static HashMap separate(String expr){
		HashMap map = new HashMap();
		String val = ""; String dec = "";
		for (int x = 0; x < expr.length(); x++) {
			if (expr.charAt(x) == '.') break;
			else { 
				val += expr.charAt(x);
				dec = expr.substring(expr.indexOf(expr.charAt(x)) + 1, expr.length());
				dec = dec.substring(dec.indexOf(".") + 1, dec.length());
			}
		}
		map.put("whole", val);
		map.put("decimal", dec);
		return map;
	}

	static float decimal(String input, int base){
		float val = 0;
		return val;
	}

	static int whole(String input, int base){
		int val = 0;
		return val;
	}
}