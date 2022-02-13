# Integer Palindrome check. 
## Reverse second half and Compare with first half. O(d/2)

<pre>
public static boolean palindromeInt2(int x) { 
		if(x<0 || (x%10==0 && x != 0)) {
			return false;
		}
		
		int rev = 0;
		while(x > rev) { //2332..233...23	| 23432..2343..234
			int rem = x%10; //2...3  		| 2..3..4
			x = x/10;	//233...23 			| 2343..234..23
			rev = rev * 10 + rem;//2..23 	| 2..23..234
		}
		if(x == rev || x == rev/10) {
			return true;
		}
		return false;
	}
  </pre>
  
  # Integer Palindrome
  ## Reverse complete number and compare O(d)
  <pre>
  public static boolean palindromeInt(int x) { 
		if(x<0) {
			return false;
		}
		int y = x;
		int rev = 0;
		while(x != 0) {
			int rem = x%10;
			x = x/10;
			rev = rev * 10 + rem;
		}
		if(y == rev) {
			return true;
		}
		return false;
	}
  </pre>
  
  # String palindrome.
  ## Reverse second half and compare with first half.
  <pre>
  public static boolean palindrome1(int x) { 
		StringBuilder builder = new StringBuilder(x+"");
		int n = builder.length();
		if(n%2==0) {
			StringBuilder sHalf = new StringBuilder(builder.substring(n/2, n));
			if(builder.substring(0, n/2).toString().equals(sHalf.reverse().toString())) {
				return true; 
			}
		} else {
			StringBuilder sHalf = new StringBuilder(builder.substring(n/2, n));
			if(builder.substring(0, (n/2)+1).equals(sHalf.reverse().toString())) {
				return true;
			}
		}
		return false;
	}
  </pre>
  
  # String Palindrome
  ## Reverse complete String and compare
  <pre>
  public static boolean palindrome(int x) { 
		StringBuilder builder = new StringBuilder(x+"");
		builder.reverse();
		if((x+"").equals(builder.toString())) {
			return true;
		}
		System.out.println(x + ", " + builder.toString());
		return false;
	}
  </pre>
