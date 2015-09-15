from flask import Flask, render_template, request, redirect, url_for,jsonify
import feedparser
import unicodedata
app=Flask(__name__)

@app.route('/')
def rss():
	return render_template('index.html')

@app.route('/html',methods=['GET','POST'])
def html():
	posts=[]
	url = request.form['RSSURL'].decode("utf-8")
	url =unicodedata.normalize('NFKD', url).encode('ascii','ignore')
	feed=feedparser.parse(url)
	print url
	print type(url)
	for i in range(0,len(feed['entries'])):
		title=feed['entries'][i].title
		description=feed['entries'][i].summary
		url=feed['entries'][i].link
		posts.append({
        'title': unicodedata.normalize('NFKD', title).encode('ascii','ignore'),
        'description': unicodedata.normalize('NFKD', description).encode('ascii','ignore'),
        'url': unicodedata.normalize('NFKD', url).encode('ascii','ignore'),
   		 })


	return render_template('result.html',feeds=posts)



if __name__=="__main__":
	app.debug = True
	app.run(host='0.0.0.0', port = 5000)