# -*- coding: utf-8 -*-
import scrapy
import json


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['www.airbnb.com']

    def start_requests(self):
        yield scrapy.Request(url='https://www.airbnb.co.in/api/v2/explore_tabs?version=1.3.9&satori_version=1.0.7&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=false&fetch_filters=true&has_zero_guest_treatment=true&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=true&show_groupings=true&supports_for_you_v3=true&timezone_offset=330&client_session_id=99c29d30-9048-48ae-b5e3-2caa2cb6c45e&metadata_only=false&is_standard_search=true&refinement_paths%5B%5D=%2Frestaurants&selected_tab_id=restaurant_tab&place_id=ChIJCSF8lBZEwokRhngABHRcdoI&screen_size=medium&query=Brooklyn%2C%20NY%2C%20United%20States&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=INR&locale=en-IN', callback=self.parse_id)

    def parse_id(self, response):
        data = json.loads(response.body)
        restaurants = data.get('explore_tabs')[0].get('sections')[0].get('recommendation_items')
        for restaurant in restaurants:
            yield scrapy.Request(url='https://www.airbnb.co.in/api/v2/similar_restaurants/{0}?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=INR&locale=en-IN&number_of_guests=2&_format=default'.format(restaurant.get('id')), callback=self.parse)

    def parse(self, response):
        restaurant = json.loads(response.body).get('place_activity')
        yield  {
            'id': restaurant.get('id'),
            'title': restaurant.get('title'),
            'type': restaurant.get('action_kicker'),
            'description': restaurant.get('description'),
            'place:' (
                'address': restaurant.get('place').get('address'),
                'city': restaurant.get('place').get('city'),
                'country': restaurant.get('place').get('country'),
                'lattitude': restaurant.get('place').get('lat'),
                'longitude': restaurant.get('place').get('lng'),
            ),
            'phone_number': restaurant.get('place').get('phone'),
            'website': restaurant.get('place').get('website') 
        }

