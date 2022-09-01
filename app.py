from flask import  Flask, render_template, request, jsonify, url_for, session, redirect
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.9cihgwo.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta



@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/')
def home2():
    return render_template('movie.html')
# movie.html 추가 -> python 테마로 변경할예정 movie 명칭 -> python으로 변경해야함

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title': title,
        'image': image,
        'desc': desc,
        'star': star_receive,
        'comment': comment_receive
    }
    db.movies.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    movie_list = list(db.movies.find({}, {'_id': False}))
    return jsonify({'movies':movie_list})



@app.route("/ds", methods=["POST"])
def web_ds_post():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']

    passwordCheck_receive = request.form['passwordCheck_give']
    phone_receive = request.form['phone_give']
    address_receive = request.form['address_give']
    gender_receive = request.form['gender_give']

    doc = {
        'id': id_receive,
        'password': password_receive,
        'passwordCheck': passwordCheck_receive,
        'phone': phone_receive,
        'address': address_receive,
        'gender': gender_receive
    }

    db.ds.insert_one(doc)

    return jsonify({'msg': '회원가입 완료!'})


@app.route("/ds", methods=["GET"])
def web_mars_get():
    order_list = list(db.ds.find({}, {'_id': False}))
    return jsonify({'orders': order_list})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
