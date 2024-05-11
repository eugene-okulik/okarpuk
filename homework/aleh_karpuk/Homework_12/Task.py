class Flower:
    def __init__(self, name, color, freshness, stem_length, price):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price


class Rose(Flower):
    def __init__(self, name, color, freshness, stem_length, price, kind):
        super().__init__(name, color, freshness, stem_length, price)
        self.kind = kind


class Lily(Flower):
    def __init__(self, name, color, freshness, stem_length, price, fragrance):
        super().__init__(name, color, freshness, stem_length, price)
        self.fragrance = fragrance


class Bouquet:
    def __init__(self):
        (self.flowers) = []

    def add_flower(self, flower_name):
        self.flowers.append(flower_name)

    def calculate_average_wilting_time(self):
        total_wilting_time = 0
        for i in self.flowers:
            total_wilting_time += i.freshness
        wilting_time_calculation = round((total_wilting_time / len(self.flowers)), 2)
        return wilting_time_calculation

    def sort_flowers_by_parameter(self, parameter):
        self.flowers.sort(key=lambda x: getattr(x, parameter))

    def search_flowers_by_parameter(self, parameter, value):
        return [i for i in self.flowers if getattr(i, parameter) == value]


rose1 = Rose("rose 1", "red", 4, 25, 4, "tea rose")
rose2 = Rose("rose 2", "pink", 5, 30, 5, "garden rose")
lily1 = Lily("lily", "white", 5, 22, 7, "sweet")


bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(lily1)


average_wilting_time = bouquet.calculate_average_wilting_time()
print("Average wilting time of flowers in the bouquet:", average_wilting_time)


bouquet.sort_flowers_by_parameter("color")
print("Flowers in the bouquet sorted by color:")
for flower in bouquet.flowers:
    print(f"{flower.name} - {flower.color}")


search_result = bouquet.search_flowers_by_parameter("price", 4)
print("Flowers in the bouquet with chosen price:")
for flower in search_result:
    print(f"{flower.name} - price: {flower.price}")
