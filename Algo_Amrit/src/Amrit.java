
public class Amrit {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String txt = "Google";
		String[]txtarray = txt.split("");
		String pat = "ogle";
		String[]patarray = pat.split("");
		int j = 0;
		int i = 0;
		for (i = 0; i < txt.length(); ++i)
			for (j = 0; j< pat.length(); ++j)
				if (txtarray[i+j] != patarray[j])
					break;
			if (j == patarray.length-1)
				System.out.println(i);
		

	}

}
