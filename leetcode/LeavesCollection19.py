"""
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

示例 1：

输入：leaves = "rrryyyrryyyrr"

输出：2

解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

示例 2：

输入：leaves = "ryr"

输出：0

解释：已符合要求，不需要额外操作

提示：

3 <= leaves.length <= 10^5
leaves 中只包含字符 'r' 和字符 'y'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/UlBDOe
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        r, ry, ryr = 1 if leaves[0] == 'y' else 0, float('inf'), float('inf')
        for i in range(1, len(leaves)):
            if leaves[i] == 'r':
                r, ry, ryr = r, min(r, ry) + 1, min(ry, ryr)
            else:
                r, ry, ryr = r + 1, min(r, ry), min(ry, ryr)+1
        return ryr

"""
思路
一共n片树叶，第i片可能为r，也可能为y，前i片最终要和后面的树叶连起来，组合ryr模式，因此需要总结出前i片什么样的模式才能与后面的树叶结合起来共同组成ryr模式。

r模式，即全为r，后面跟yr即可组成ryr模式。
ry模式，后面跟r即可组成ryr模式。
ryr模式，后面跟r即可组成ryr模式。
以y开头的模式，全不符合。
所以前i片树叶组成的模式一共3种：r模式，ry模式，ryr模式
那么前i-1片也是这3种模式，每个模式修改树叶数量用变量r，ry，ryr记录

第i片树叶为r的情况下：

r模式，r模式可以由前i-1片的r模式跟第i片直接组成，无需修改，修改数量跟之前相同为r
ry模式，将本片树叶修改为y，与前i-1片树叶的r模式或者ry模式组合均可，取两者中比较小的：min(r, ry) + 1
ryr模式，与前i-1片树叶的ry模式或者ryr模式直接组合即可，无需修改，取两者中比较小的：min(ry, ryr)
第i片树叶为y的情况下：

r模式，r + 1
ry模式，min(r, ry)
ryr模式，min(ry, ryr) + 1
因此状态转移如下：
如果第i片为r：

f(i).r = f(i-1).r
f(i).ry = min(f(i-1).r, f(i-1).ry) + 1
f(i).ryr = min(f(i-1).ry, f(i-1).ryr)
如果第i片为y：

f(i).r = f(i-1).r + 1
f(i).ry = min(f(i-1).r, f(i-1).ry)
f(i).ryr = min(f(i-1).ry, f(i-1).ryr) + 1
第0片为边界，如果第0片为r，则r=0，否则为1，ry、ryr不可能由1片组成，因此全设置为float('inf')

作者：vzp
链接：https://leetcode-cn.com/problems/UlBDOe/solution/dong-tai-gui-hua-python3-by-vzp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
