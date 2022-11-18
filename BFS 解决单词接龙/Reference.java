import java.util.Set;
import java.util.List;
import java.util.HashSet;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;

class Reference {
	public static void main(String[] args){
		Imp imp = new Imp();
		// String[] ctt = {"hot", "dot", "dog", "lot", "log", "cog"};
		List<String> list = new ArrayList<String>();
		list.add("hot");
		list.add("dot");
		list.add("dog");
		list.add("lot");
		list.add("log");
		list.add("cog");
		System.out.println(imp.ladderLength("hit", "cog", list));
	}
}

class Imp {
	public int ladderLength(String beginWord, String endWord, List<String> wordList) {
		// 把字典中的单词放入到set中，主要是为了方便查询
		Set<String> dictSet = new HashSet<String>(wordList);
		Set<String> visited = new HashSet<String>();
		Queue<String> queue = new LinkedList<String>();
		queue.add(beginWord);// 把起始点添加到队列中
		int level = 0;
		while (!queue.isEmpty()) {
			int levelCount = queue.size();// 当前层的节点个数
			level++;// 第几层
			// 遍历当前层的所有字符串
			while (levelCount-- > 0) {
				String word = queue.poll();
				// 下面是修改字符串的字符，然后生成一个新的字符串
				for (int j = 0; j < word.length(); j++) {
					char[] ch = word.toCharArray();
					for (char c = 'a'; c <= 'z'; c++) {
						if (c == word.charAt(j))
							continue;
						ch[j] = c;
						// 修改其中的一个字符，然后重新构建一个新的单词
						String newWord = String.valueOf(ch);
						// 如果字典中包含newWord，并且newWord没有被访问过，就把他加入到队列中
						if (dictSet.contains(newWord) && visited.add(newWord)) {
							// 加入队列之前判断newWord是不是我们要找的，如果是就直接返回
							if (newWord.equals(endWord))
								return level + 1;
							queue.add(newWord);
						}
					}
				}
			}
		}
		return 0;
	}
}


