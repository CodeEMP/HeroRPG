import characters
import items
import locations


hero = characters.Hero(12)
hero.add_item(items.Longsword(), 1)
hero.add_item(items.Chainmail(), 1)
hero.add_item(items.Leather(), 0)
hero.show_inventory()
hero.hp -= 5
print(hero.hp)
town = locations.Town()
town.rest_at_inn(hero, 2)
print(hero.hp)
