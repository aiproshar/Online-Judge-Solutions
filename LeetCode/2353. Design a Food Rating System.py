'''
In place value update of heap, lazy deletion logic
We want maximum but whatif the elements inside heap changing value dynamically
+ A bit of OOP concepts, heavily using python Data Structures
'''
class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):

        self.food_to_cuisine = {foods[i]: cuisines[i] for i in range(len(foods))}
        self.cuisines = {}
        for cuisine in cuisines:
            # first object: a heap, each entry (-rating, food)
            # second object: a dict, dict[food] = rating, we keep track of
            # latest rating for specific food type, so we can invalidate older rating
            self.cuisines[cuisine] = ([], {})

        for i in range(len(foods)):
            cuisine = self.food_to_cuisine[foods[i]]
            heapq.heappush(self.cuisines[cuisine][0], (-ratings[i], foods[i]))
            # save the latest rating
            self.cuisines[cuisine][1][foods[i]] = -ratings[i]


    def changeRating(self, food: str, newRating: int) -> None:

        cuisine = self.food_to_cuisine[food]
        heap = self.cuisines[cuisine][0]
        lookup = self.cuisines[cuisine][1]
        lookup[food] = -newRating
        heapq.heappush(heap, (-newRating, food))


    def highestRated(self, cuisine: str) -> str:

        heap = self.cuisines[cuisine][0]
        lookup = self.cuisines[cuisine][1]

        while heap:
            rating, food = heap[0]
            if lookup[food] != rating:
                heapq.heappop(heap)
                continue
            else:
                return food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)