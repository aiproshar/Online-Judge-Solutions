'''
Greedy Problem, my messy greedy solution
Corner Case: If any number is larget than target, we cannot append them
My solution not only works three triplets, it works for n -lets. More general purpose
'''

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        valid_triplets = []
        for triplet in triplets:
            for i in range(len(target)):
                if triplet[i] > target[i]:
                    break
            else:
                valid_triplets.append(triplet)
        if valid_triplets == []:
            return False
        cols = zip(*valid_triplets)
        col_list = []
        for col in cols:
            col_list.append(set(col))
        for i in range(len(target)):
            if target[i] not in col_list[i]:
                return False
        return True
# Time Complexity: O(n)
# Space: O(n)


'''
More greedy solution, only for three element triplets
Just keep track of finding exact match on each, and discard invalid one before updating max
'''


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            else:
                if triplet[0] == target[0]:
                    found[0] = True
                if triplet[1] == target[1]:
                    found[1] = True
                if triplet[2] == target[2]:
                    found[2] = True
        return all(found)


# Time Complexity: O(n)
# Space: O(1)