import twitter
import urllib2
from urllib2 import urlopen
import cookielib
from cookielib import CookieJar
import json

#basic auth required to access the twitter API

ckey='tN3sOuulbKmiAQ3Zz5bpeRrkv'
csec='Uw380sVUL2U8oaJSc1k66FPDP6DtwV5eQlszgaJgRBvFTA0aCS'
token='2436704168-kEQxs02I6GIzLmWokKyhhjhOJ8Eb2SnWd7QlQhm'
token_secret='xQQZwIgOgp8hOplC0E4Pxe1HwUWhzdQYdMxFaeD6BcjVS'

auth=twitter.oauth.OAuth(token,token_secret,ckey,csec)

twitter_api=twitter.Twitter(auth=auth)

print twitter_api

#setting proxy authentication

#proxy=urllib2.ProxyHandler({})
#autho=urllib2.HTTPBasicAuthHandler()
#opener=urllib2.build_opener(proxy,autho,urllib2.HTTPHandler)
#opener.addheaders=[('User-agent','Mozilla/29.0')]
#urllib2.install_opener(opener)

#use WOE to find trending topics of a place

WORLD_WOE_ID=1
INDIA_WOE_ID=23424848

#calls GET HTTP request with url="http://api.twitter.com/1.1/trends/place.json?id=1" for world
#calls GET HTTP request with url="http://api.twitter.com/1.1/trends/place.json?id=23424848" for world

world_trends=twitter_api.trends.place(_id=WORLD_WOE_ID)
india_trends=twitter_api.trends.place(_id=INDIA_WOE_ID)

#print world_trends
#print
#print india_trends

#use json to make the previous result readable

print json.dumps(world_trends,indent=1)
print
print json.dumps(india_trends,indent=1)
""""
#use set data structure to find the common trending topics of india and world

world_trends_set=set([trend['name']
                      for trend in world_trends[0]['trends']])

india_trends_set=set([trend['name']
                      for trend in india_trends[0]['trends']])

common_trends = world_trends_set.intersection(india_trends_set)

print
print common_trends
#print json.dumps(common_trends,indent=1)

"""
