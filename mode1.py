from island import Island
from data_structures.bst import BinarySearchTree

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        Best case -> 
        Worst case -> O(nlog(n)) or less
        """
        self.island_bst = BinarySearchTree()
        for island in islands:
            self.island_bst[island.money / island.marines] = island
        
        self.crew = crew


    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        Best case -> O(log(n)) or less
        Worst case -> O(n) or less
        """
        selected_islands = []
        remaining_crew = self.crew

        while remaining_crew > 0 and not self.island_bst.is_empty():
            island = self.island_bst.root.item
            if island > 0:
                pirates_sent = min(remaining_crew, island.marines)
                selected_islands.append(island, pirates_sent)
                remaining_crew -= pirates_sent
                del self.island_bst[island]
                
        return selected_islands

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        Best case ->
        Worst case -> O(C * N) where C is the length crew numbers
        """
        res = []
        for count in crew_numbers:
            remaining_crew = count
            total_money = 0

            while remaining_crew > 0 and not self.island_bst.is_empty():
                island = self.island_bst.root.item
                if island.money > 0:
                    pirates_sent = min(remaining_crew, island.marines)
                    total_money += min(((pirates_sent * island.money)/island.marines), island.money)
                    remaining_crew -= pirates_sent
            res.append(total_money)

        return res
        

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        Best case ->
        Worst case -> O(log(n)) or less
        """
        if new_money > 0:
            del self.island_bst[island.money / island.marines]
            island.money = new_money
            island.marines = new_marines
            self.island_bst[new_money / new_marines] = island
