import pandas as pd
import re

data = pd.read_csv("../data/NYPL-menus.csv")

# print(data.head())

'''Select a subset of the data for cleaning with Python'''
subset = data[['event', 'venue', 'place', 'date']]

# print(subset.head())

'''Destructure DataFrame to return individual column Series to pass to functions'''
(event, venue, place, date) = subset['event'], subset['venue'], subset['place'], subset['date']

'''Functions to operate on each column and return cleaned data'''

def clean_event(event):
    event = event.str.replace('[', '', regex=True)
    event = event.str.replace(']', '', regex=True)

    # TODO: Change this to replace with space if at end of word, : if in the middle
    event = event.str.replace(';', '', regex=True)
    return print(event.head(50))

def clean_venue(venue):
    return print(venue.head())

def clean_place(place):
    return print(place.head())

def clean_date(date):
    return print(date.head())


def main():
    clean_event(event)

    # clean_venue(venue)

    # clean_place(place)

    # clean_date(date)


if __name__ == "__main__":
    main()