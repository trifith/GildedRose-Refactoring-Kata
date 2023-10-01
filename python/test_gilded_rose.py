# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_quality_under_50(self):
        items = [Item('standard', 10, 52)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)
    def test_quality_not_lower_than_zero(self):
        items = [Item('standard', 10, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
    def test_sufuras_does_not_lose_quality_or_sellIn(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        items_orig = items
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items, items_orig)
    def test_aged_bree_has_higher_quality(self):
        items = [Item("Aged Brie", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)

if __name__ == '__main__':
    unittest.main()
# Refactor

# Step one is to add testing for all cases. We're assuming that the existing code
# works correctly. 
# 
# Tests
# - "Sulfuras" does not lose Quality or SellIn
# - "Aged Brie" has higher Quality, but never more than 50
# - "Backstage passes" have higher quality if SellIn is greater than 0
# - "Backstage passes" quality increase by 2 if Sellin is <= 10
# - "Backstage passes" quality increases by 3 if SellIn is <= 5
# - "Conjured" items have 2 less quality
# - All other items have 1 less quality and 1 less SellIn
# - "Backstage passes" have a quality of zero if SellIn is 0 or less.
# - "Conjured" itmes have 4 less quality if SellIn is 0 or less
# - Items with a SellIn of 0 or less have 2 less quality
# 
# Step two, extract handling of special items into a seperate function. 
# 
# 
