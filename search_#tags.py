import twitter
import urllib2
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

#proxy=urllib2.ProxyHandler({'http':'http://ipg_2012011:akg4850@192.168.1.103:3128'})
#autho=urllib2.HTTPBasicAuthHandler()
#opener=urllib2.build_opener(proxy,autho,urllib2.HTTPHandler)
#urllib2.install_opener(opener)

q='@spam'

count=10000

#calls GET on http://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results=twitter_api.search.tweets(q=q,count=count)

statuses=search_results['statuses']

#iterate through 5 more batches of results by following the cursor instead of pagination given the dynamic nature of tweets

for _ in range(50):
    print "Length of statuses",len(statuses)
    try:
        next_results=search_results['search_metadata']['next_results']
    except KeyError, e:
        break
    #create dictionary from next_results, which has form: ?max_id=1546468238467&q=NCAAA&include_entities=1
    kwargs=dict([kv.split('=') for kv in next_results[1:].split("&") ])

    search_results=twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

    #calls the function as twitter_api.search.tweets(q='%23MentionSomeoneImportantForYou',include_entities=1,max_id=316626749367) it appears as key/value pair in dictionary

#show one sample results by slicing the list

print json.dumps(statuses[0],indent=1)
"""
status_texts=[status['text']
              for status in statuses]

screen_names=[user_mention['screen_name']
              for status in statuses
                  for user_mention in status['entities']['user_mentions']]

hashtags=[hashtag['text']
          for status in statuses
              for hashtag in status['entities']['hashtags']]

words=[w
       for t in status_texts
           for w in t.split()]

print json.dumps(status_texts[0:5],indent=1)
print json.dumps(screen_names[0:5],indent=1)
print json.dumps(hashtags[0:5],indent=1)
print json.dumps(words[0:5],indent=1)
"""
