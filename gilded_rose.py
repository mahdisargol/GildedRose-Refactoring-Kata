import json
import unittest
from Item import Item
# Load items from a data source

f = open('rules.json')
rule = json.load(f)
f.close()


class GildedRose():




 def update_quality(name, sell_in, quality):

    ruleItem = next((case for case in rule if case["name"] == name), {})
    item = Item(ruleItem)
    if not item.allow_sale:
        print(name, ', ', sell_in, ', ', quality,' (Not allowed to sale)')

        return

    if sell_in == 0 and item.quality_date_passed is not None:
        new_quality = item.quality_date_passed

    elif sell_in == 0 and item.step_date_passed is not None:
        new_quality = quality + item.step_date_passed

    elif item.step_table is not None:
        stepItem = next(
            (d for d in item.step_table if d[0] <= sell_in and sell_in <= d[1]), None)
        new_quality = quality + \
            stepItem[2] if stepItem is not None else item.step

    else:
        new_quality = quality + item.step

    new_quality = min(new_quality, item.max_quality)
    new_quality = max(new_quality, item.min_quality)
    sell_in=sell_in-1

    print(name, ', ', sell_in, ', ', new_quality)



GildedRose.update_quality(name="+5 Dexterity Vest", sell_in=10, quality=20)
GildedRose.update_quality(name="Aged Brie", sell_in=2, quality=0)
GildedRose.update_quality(name="Elixir of the Mongoose", sell_in=5, quality=7)
GildedRose.update_quality(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
GildedRose.update_quality(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)
GildedRose.update_quality(
    name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
GildedRose.update_quality(
    name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49)
GildedRose.update_quality(
    name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49)
GildedRose.update_quality(name="Conjured Mana Cake", sell_in=3, quality=6)


