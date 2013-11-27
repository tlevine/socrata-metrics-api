#!/usr/bin/env python3
import csv
import os
import json

field_names = {
    'site': [
        "datasets-created-total",
        "datasets-deleted-total",
        "datasets-deleted-href",
        "datasets-deleted-blobby",
        "datasets-created-snapshot-total",
        "datasets-deleted-snapshot-total",
        "datasets-created-blobby-total",
        "datasets-created-blobby",
        "datasets-deleted-blobby-total",
        "datasets-created-href",
        "datasets-created-href-total",
        "datasets-deleted-href-total",
        "charts-created-total",
        "charts-deleted-total",
        "maps-created-total",
        "maps-deleted-total",
        "filters-created-total",
        "filters-deleted-total",
        "rows-created-total",
        "rows-deleted-total",
        "users-created",
        "page-views-total",
        "embeds-total",
        "embeds",
        "maps-created",
        "page-views",
        "bytes-out",
        "rows-loaded-api",
        "rows-loaded-print",
        "datasets-deleted-snapshot",
        "rows-accessed-website",
        "rows-loaded-download",
        "rows-accessed-api",
        "rows-loaded-website",
        "datasets-created-snapshot",
        "rows-deleted",
        "rows-accessed-rss",
        "maps-deleted",
        "filters-created",
        "rows-accessed-widget",
        "rows-loaded-widget",
        "datasets-created",
        "js-page-view",
        "rows-accessed-download",
        "datasets-deleted",
        "view-loaded",
        "rows-accessed-print",
        "charts-deleted",
        "rows-loaded-rss",
        "bytes-in",
        "filters-deleted",
        "charts-created",
        "rows-created",
        "disk-usage",
        "geocoding-requests",
        "shares",
        "app-token-created",
        "comments",
        "ratings-total",
        "ratings-count",
        "date",
        "portal",
    ],
    'top-datasets':[
        "view-id",
        "count",
        "date",
        "portal",
    ],
    'top-embeds':[
        "date",
        "portal",
        'url',
        'count',
    ],
    'top-referrers':[
        "date",
        "portal",
        'url',
        'count',
    ],
    'top-searches':[
        "date",
        "portal",
        'search-term',
        'count',
    ],
}

def main():
    if not os.path.isdir('csv'):
        os.mkdir('csv')
    write_table('site')
    write_table('top-searches', transform_search)
    write_table('top-embeds', transform_url)
    write_table('top-referrers', transform_url)

def write_table(table_name, transform_func = lambda x: [x]):
    f = open(os.path.join('csv', table_name + '.csv'), 'w')
    c = csv.DictWriter(f, field_names[table_name])
    c.writeheader()
    for date in os.listdir('data'):
        x = os.path.join('data', date, table_name)
        for portal in os.listdir(x):
            y = os.path.join(x, portal)
            try:
                g = open(y)
                c.writerows(transform_func(json.load(g)))
                g.close()
            except:
                print(y)
                raise
    f.close()

def transform_search(widerows: list):
    if len(widerows) == 0:
        pass
    elif len(widerows) > 1:
        print(widerows)
        raise ValueError("I don't know what to do with multiple elements.")
    else:
        widerow = widerows[0]
        counts = widerow['count']
        del(widerow['count'])
        del(widerow['view-id'])

        for search, count in counts.items():
            longrow = {
                'portal': widerow['portal'],
                'date': widerow['date'],
                'search-term': search,
                'count': count,
            }
            yield longrow

def transform_url(widerow):
    counts = widerow['count']
    host = widerow['view-id']
    del(widerow['view-id'])

    for route, count in counts.items():
        longrow = {
            'portal': widerow['portal'],
            'date': widerow['date'],
            'url': host + route,
            'count': count,
        }
        yield longrow

if __name__ == '__main__':
    main()
