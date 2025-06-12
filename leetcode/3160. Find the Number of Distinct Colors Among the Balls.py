from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = []
        ball_to_color = {}  # ball -> color
        # color_to_ball = {}  # color -> ball

        color_counter = {}
        for ball, color in queries:
            if ball in ball_to_color:
                old_color = ball_to_color.get(ball)
                if old_color != color:
                    color_counter[old_color] -= 1
                ball_to_color[ball] = color
                color_counter[color] = color_counter.get(color, 0) + 1
            else:
                ball_to_color[ball] = color
                color_counter[color] = 1

            count = sum([1 for e in color_counter if color_counter[e] > 0])
            result.append(count)

        return result


# class Solution:
#     def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
#         result = []
#         colors = set()
#         for i in range(limit):
#             color = queries[i][0]
#             colors.add(color)
#             result.append(len(colors))
#         return result
#


# res = Solution().queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]])
# print(f'res {res}')
res = Solution().queryResults( 4,
                   [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]])
print(f'res {res}')

limit = 1
queries = [[0, 1], [1, 4], [1, 1], [1, 4], [1, 1]]
solution = Solution()
result = solution.queryResults(limit, queries)
print(result)  # Output: [1, 2, 1, 2, 1]
