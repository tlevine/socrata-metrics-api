#!/usr/bin/env node

var metrics  = require('./site-metrics')
  , fs       = require('fs')
  , argv     = require('optimist').argv

var mode = argv._.length > 0 ? argv._[0] : ''
if (mode === 'download') {
  download()
}

function download() {
  var portals = [
    'data.austintexas.gov',
    'data.cityofnewyork.us',
    'data.hawaii.gov',
    'explore.data.gov',
    'bronx.lehman.cuny.edu',
    'data.sfgov.org',
    'data.baltimorecity.gov',
    'data.oregon.gov',
    'data.raleighnc.gov',
    'finances.worldbank.org',
    'data.ok.gov',
    'data.seattle.gov',
    'data.montgomerycountymd.gov'
  ]
  if (!fs.existsSync('data')){
    fs.mkdirSync('data')
  }
  portals.map(downloadPortal)
  
  function downloadPortal(portal) {
    getDays().map(downloadPortalDay)

    function getDays() {
      var days = []
      var day = new Date('2013-01-01')
      while (day <= new Date()) {
        days.push(new Date(day.setDate(day.getDate() + 1)))
      }
      return days
    }

    function downloadPortalDay(day) {
      
      var datestamp = [
        day.getFullYear(),
        (day.getMonth() + 1 <= 9 ? '0' : '') + (day.getMonth() + 1),
        (day.getDate() <= 9 ? '0' : '') + (day.getDate())
      ].join('-')
      if (!fs.existsSync('data/' + datestamp)){
        fs.mkdirSync('data/' + datestamp)
      }
      ['site','top-datasets','top-referrers','top-embeds','top-searches'].map(function(subdir){
        if (!fs.existsSync('data/' + datestamp + '/' + subdir)){
          fs.mkdirSync('data/' + datestamp + '/' + subdir)
        }
      })

      fs.exists(datestamp + '/site/' + portal, function(yes){
        if (!yes) metrics.daily.site(portal, day, write(datestamp + '/site/' + portal))
      })
      fs.exists(datestamp + 'top-datasets' + portal, function(yes){
        if (!yes) metrics.daily.top('DATASETS', portal, day, write(datestamp + '/top-datasets/' + portal))
      })
      fs.exists(datestamp + '/top-referrers/' + portal, function(yes){
        if (!yes) metrics.daily.top('REFERRERS', portal, day, write('/top-referrers/' + portal))
      })
      fs.exists(datestamp + '/top-embeds/' + portal, function(yes){
        if (!yes) metrics.daily.top('EMBEDS', portal, day, write('/top-embeds/' + portal))
      })
      fs.exists(datestamp + '/top-searches/' + portal, function(yes){
        if (!yes) metrics.daily.top('SEARCHES', portal, day, write('/top-searches/' + portal))
      })
    }
  }

  function write (filename) {
    return function(body) {
      fs.writeFile('data/' + filename + '.json', JSON.stringify(body), function(){})
    }
  }
}
