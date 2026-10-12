class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:

        notes = defaultdict(int)

        for bill in bills:
            notes[bill] += 1
            # nothing to return
            if bill == 5:
                continue
            else:
                # We have to return
                back = bill - 5
                # start from largest note to smallest
                current_note = back
                while back:
                    if current_note == 0:
                        # not possible
                        return False
                    if notes[current_note] > 0 and current_note <= back:
                        notes[current_note] -= 1
                        back -= current_note
                    else:
                        current_note -= 5
        return True
# Greedy Linear
# Time Complexity: O(n)
# Space: O(1) // Only 3 kind of notes