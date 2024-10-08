class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0

        for j in range(n):
            left_smaller = 0
            left_greater = 0
            right_smaller = 0
            right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                if rating[i] > rating[j]:
                    left_greater += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                if rating[k] > rating[j]:
                    right_greater += 1

            count += left_smaller * right_greater + left_greater * right_smaller

        return count
