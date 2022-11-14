class Reference {
	public static void main(String[] args){
		System.out.println(new Imp().minWindow("AAAAAAAAAABBB", "AB"));
	}
}

class Imp {
	public String minWindow(String s, String t) {
		int[] map = new int[128];
		// 记录字符串t中每个字符的数量
		for (char ch : t.toCharArray())
			map[ch]++;
		int count = t.length();// 字符串t中字符的数量
		int left = 0;// 窗口的左边界
		int right = 0;// 窗口的右边界
		// 记录满足条件的最小窗口长度
		int minWindow = Integer.MAX_VALUE;
		// 记录满足条件的最小窗口开始位置，以便于后面截取
		int strStart = 0;
		while (right < s.length()) {
			// 如果窗口覆盖t中的一个字符，count就减1
			if (map[s.charAt(right)]-- > 0)
				count--;
			// 如果count等于0，说明全部覆盖了，要移动窗口的左边界
			// 找到最小的能全部覆盖的窗口
			while (count == 0) {
				// 如果现在窗口比之前保存的还要小，就更新窗口的长度以及窗口的起始位置
				if (right - left < minWindow) {
					minWindow = right - left + 1;
					strStart = left;
				}
				// 移除窗口最左边的元素，也就是缩小窗口，这里是关键，如果窗口最左边
				// 那个元素的个数是0，那么这个元素肯定也存在于字符串t中，因为如果不
				// 存在的话，右指针第一遍扫描的时候就把他变成负的了
				if (map[s.charAt(left)]++ == 0)
					count++;
				// 左指针往右移
				left++;
			}
			right++;// 窗口右边往右移一步
		}
		//如果找到合适的窗口就截取，否则就返回空
		if (minWindow == Integer.MAX_VALUE)
			return "";
		return s.substring(strStart, strStart + minWindow);
	}
		
}


