import os
import datetime

from flask import Flask, jsonify, redirect, render_template, request, url_for
import psycopg2

import db

app = Flask(__name__)

@app.before_first_request
def initialize():
  db.setup()


@app.route('/')
def home():
	return render_template("home.html")


@app.route('/consent')
def consent():
	return render_template("survey.html")


@app.route('/decline')
def decline():
  return render_template("decline.html")


@app.route('/thanks', methods=['POST'])
def thanks():
	new_name = request.form['new_name']
	rudest_animal = request.form['rudest_animal']
	hotdog_sandwich = request.form['hotdog_sandwich']
	one_more = request.form.get('one_more')
	time_submit = datetime.datetime.now()
	if(one_more):
		extra = request.form['extra']
	with db.get_db_cursor(commit=True) as cur:
		if(one_more):
			cur.execute("insert into dummy(new_name, rudest_animal, hotdog_sandwich, one_more, extra, time_submit) values (%s, %s, %s, %s, %s, %s)",(new_name, rudest_animal, hotdog_sandwich, one_more, extra, time_submit))
		else:
			cur.execute("insert into dummy(new_name, rudest_animal, hotdog_sandwich, one_more, extra, time_submit) values (%s, %s, %s, 'no', ' ', %s)",(new_name, rudest_animal, hotdog_sandwich, time_submit))
	return render_template("thanks.html")


@app.route('/api/results')
def api_results():
	reverse = request.args.get('reverse')
	with db.get_db_cursor() as cur:
		cur.execute("SELECT * FROM dummy;")
		results = [record for record in cur]
		data_list = []
		for i in range(len(results)):
			entry = results[i];
			data = {
				"dummy_id": entry[0],
				"new_name": entry[1],
				"rudest_animal": entry[2],
				"hotdog_sandwich": entry[3],
				"one_more": entry[4],
				"extra": entry[5],
				"time_submit": entry[6]
			}
			data_list.append(data)
		if reverse == "true":
			return jsonify(list(reversed(data_list)))
		else:
			return jsonify(data_list)


@app.route('/admin/summary')
def admin_summary():
	link_api = url_for("api_results")
	return render_template("summary.html", link_api=link_api)

if __name__ == '__main__':
  pass

