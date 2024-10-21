from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total
    
class PercentageDiscount(DiscountStrategy):

    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percentage/100)
    
class FixedAmountDiscount(DiscountStrategy):

    def __init__(self, fixed_amount: float):
        self.fixed_amount = fixed_amount

    def apply_discount(self, total: float) -> float:
        return total - self.fixed_amount
    
class ShoppingCart:

    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
        self.items = {}

    def add_item(self, item: str, price: float):
        self.items[item] = self.items.get(item, [])
        self.items[item].append(price)

    def remove_item(self, item: str):
        if item in self.items:
            self.items[item].pop()
            if not self.items[item]:
                del self.items[item]

    def get_total(self) -> float:
        total = 0
        for key in self.items:
            total += sum(self.items[key])
        return total
    
    def get_total_after_discount(self) -> float:
        return self.discount_strategy.apply_discount(self.get_total())
    
if __name__ == "__main__":
    cart = ShoppingCart(PercentageDiscount(10))

    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)
    cart.remove_item("Item 2")

    print("Total before discount:", cart.get_total())
    print("Total after discount:", cart.get_total_after_discount())
