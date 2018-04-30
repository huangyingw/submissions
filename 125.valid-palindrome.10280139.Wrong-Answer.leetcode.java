	public class Solution {
		public boolean isPalindrome(String s) {
			assert s != null;
			int start = 0;
			int end = s.length() - 1;

			while (start < end) {
				if (!Character.isLetterOrDigit(s.charAt(start))) {
					start++;
				}
				if (!Character.isLetterOrDigit(s.charAt(end))) {
					end--;
				}
				if (Character.toLowerCase(s.charAt(start)) != Character
						.toLowerCase(s.charAt(end))) {
					return false;
				}
				else {
					start++;
					end--;
				}
			}

			return true;
		}
	}

