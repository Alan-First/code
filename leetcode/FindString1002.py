"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-common-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return [ char for char in set(A[0]) for i in range( min(s.count(char) for s in A )) ]
            
"""
1. 巧妙应用min的方法，用循环生成数据量
2. 通过s.count获取字符串个数
3. set转换成集合
"""
