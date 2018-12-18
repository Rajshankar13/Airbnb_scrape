import json

with open('restaurants.json', 'r') as file:
    data = json.load(file)

tab_id = data.get('explore_tabs')[0].get('tab_id')
print(tab_id)

restaurants = data.get('explore_tabs')[0].get('sections')[1].get('recommendation_items')

for restaurant in restaurants:
    print(restaurant.get('id'), restaurant.get('title'))
