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
    ]
}

def main():
    if not os.path.isdir('csv'):
        os.mkdir('csv')
    write_table('site')

def write_table(table_name):
    f = open(os.path.join('csv', table_name + '.csv'), 'w')
    c = csv.DictWriter(f, field_names[table_name])
    c.writeheader()
    for date in os.listdir('data'):
        x = os.path.join('data', date, table_name)
        for portal in os.listdir(x):
            y = os.path.join(x, portal)
            try:
                g = open(y)
                c.writerow(json.load(g))
                g.close()
            except:
                print(y)
                raise
    f.close()

if __name__ == '__main__':
    main()
