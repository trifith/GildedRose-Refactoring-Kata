# Refactor

Step one is to add testing for all cases. We're assuming that the existing code
works correctly. 

Tests
- all items have a SellIn value
- all items have a Quality value
- No item has a Quality higher than 50
- No item has a Quality lower than 0
- "Sulfuras" does not lose Quality or SellIn
- "Aged Brie" has higher Quality, but never more than 50
- "Backstage passes" have higher quality if SellIn is greater than 0
- "Backstage passes" quality increase by 2 if Sellin is <= 10
- "Backstage passes" quality increases by 3 if SellIn is <= 5
- "Conjured" items have 2 less quality
- All other items have 1 less quality and 1 less SellIn
- "Backstage passes" have a quality of zero if SellIn is 0 or less.
- "Conjured" itmes have 4 less quality if SellIn is 0 or less
- Items with a SellIn of 0 or less have 2 less quality

Step two, extract handling of special items into a seperate function. 


