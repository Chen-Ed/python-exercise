# """
# 题目：The n-queens puzzle is the problem of placing n queens on an n×n
# chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
# url:https://leetcode.com/problems/n-queens-ii/
# """


class Solution:
    def totalNQueens(self, n: int) -> int:

        self.n = n
        self.res = 0
        self.help_me(0, [])

        return self.res

    def help_me(self, level, result_list):
        """
        帮我放第i行
        :return:
        """

        # 假如已经成功到最后一行
        if not (self.n - level):
            self.res += 1
            return

        # 这一层不能放的列表
        no_set = set()
        for i, value in enumerate(result_list):
            no_set.add(value)  # 在此之前不能出现有同一列
            no_set.add(value + level - i)  # 不能有同一斜线
            no_set.add(value - level + i)

        # 将这一层可能的放法都放一遍
        for i in range(self.n):
            if i in no_set:
                continue

            # 不能有同一条斜线 当前是第 level 层
            tmp = result_list[:]
            tmp.append(i)
            self.help_me(level + 1, tmp)


if __name__ == '__main__':
    a = 4

    solution = Solution()
    result = solution.totalNQueens(a)
    print(result)

# """
# 分析:哦哦，他们会用那个清空现场
#
# """
