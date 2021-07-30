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
    # Work on this to remove all quotes
    event = event.str.replace('"', '', regex=True)
    event = event.str.replace('""', '', regex=True)
    event = event.str.lstrip('"')
    event = event.str.rstrip('"')


    event = event.str.replace('[', '', regex=True)
    event = event.str.replace(']', '', regex=True)

    # Match this: (?)
    pattern1 = '\(\?\)'
    event = event.str.replace(pattern1, '', regex=True)

    # Match semicolons at the end of the string
    pattern2 = '\;$'
    event = event.str.replace(pattern2, '', regex=True)

    # Match semicolons in the middle of a string and replace with :
    pattern3 = '\\b;'
    event = event.str.replace(pattern3, ':', regex=True)
    return event.to_csv("../data/test_event.csv")

def clean_venue(venue):
    venue = venue.str.replace(';', '')

    venue = venue.str.replace('?', '')

    venue = venue.str.replace('[', '', regex=True)
    venue = venue.str.replace(']', '', regex=True)

    venue = venue.str.replace('\(\)', '', regex=True)

    return venue.to_csv("../data/test_venue.csv")

def clean_place(place):
    place = place.str.replace('"', '', regex=True)
    place = place.str.replace('""', '', regex=True)
    place = place.str.lstrip('"')
    place = place.str.rstrip('"')

    place = place.str.replace(';', '')

    place = place.str.replace('?', '')

    place = place.str.replace('[', '', regex=True)
    place = place.str.replace(']', '', regex=True)

    place = place.str.replace('\(', '', regex=True)
    place = place.str.replace('\)', '', regex=True)

    return place.to_csv("../data/test_place.csv")

def clean_date(date):
    
    date = pd.Series([d for d in date if d != '190-03-06' or d != '1091-01-27' or d != '2928-03-26'])
    
    return date.to_csv("../data/test_date.csv")

def merge_series_to_df(event, venue, place, date):

    all_series = {"event": event, "venue": venue, "place": place, "date": date}
    
    df = pd.concat(all_series, axis=1)

    return df.to_csv("../data/cleaned-NYPL-menus.csv")

def main():
    # clean_event(event)

    # clean_venue(venue)

    # clean_place(place)

    clean_date(date)

    # merge_series_to_df(event, venue, place, date)


if __name__ == "__main__":
    main()