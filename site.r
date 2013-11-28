#!/usr/bin/env Rscript
library(sets)

if (!('site' %in% ls())) {
  site <- read.csv('csv/site.csv')
}
col.names <- list(total = cset(colnames(site)[grepl('.total$', colnames(site))]))
col.names$change <- cset_intersection(cset(sub('.total$','',col.names$total)), colnames(site))
col.names$total.but.no.change <- cset_difference(cset(sub('.total$','',col.names$total)), col.names$change)
col.names$change.but.no.total <- cset_difference(col.names$change, cset(sub('.total$','',col.names$total)))
col.names$other <- cset_difference(colnames(site), cset_union(col.names$total, col.names$change, col.names$total.but.no.change))
# ratings.count might be the change for ratings.total
