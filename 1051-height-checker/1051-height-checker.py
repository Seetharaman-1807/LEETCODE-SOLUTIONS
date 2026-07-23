class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        return sum(h1 != h2 for h1, h2 in zip(heights, expected))
