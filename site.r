#!/usr/bin/env Rscript
library(sets)

if (!('site' %in% ls())) {
  site <- read.csv('csv/site.csv')
}
col.names <- list(total = cset(colnames(site)[grepl('.total$', colnames(site))]))
col.names$change <- cset_intersection(cset(sub('.total$','',col.names$total)), colnames(site))
col.names$total.but.no.change <- cset_difference(cset(sub('.total$','',col.names$total)), col.names$change)
col.names$other <- cset_difference(cset_union(col.names$total, col.names$change, col.names$total.but.no.change), colnames(site))
# ratings.count might be the change for ratings.total
