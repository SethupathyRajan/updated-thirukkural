from flask import Flask, sessions, render_template
from user.audioProcessing import AudioProceesing
from user.kural import kural
from app import app, login_required,session
from user.models import User


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login()


@app.route('/practice_thirukkural',  methods=["POST"])
def practice():
    return AudioProceesing().practice()


@app.route('/filter_adhigaram',  methods=["POST"])
def fetchKural():
    return kural().fetchKural()

@app.route('/selected_game', methods=['POST'])
def selected_game():
    return kural().selected_game()

from app import login_required
@app.route('/learn_thirukkural', methods=["GET"])
@login_required
def learn_thirukkural():
    return kural().learn_thirukkural()



@app.route('/drag_drop_game', methods=["GET"])
def drag_drop_game():
    return kural().drag_drop_game()


@app.route('/evaluate_drag_game',  methods=["POST"])
def evaluate_drag_game():
    return kural().evaluate_drag_game()



@app.route('/fillups_game', methods=["GET"])
def fillups_game():
    return kural().fillups_game()

@app.route('/evaluate_fillups_game',  methods=["POST"])
def evaluate_fillups_game():
    return kural().evaluate_fillups_game()


@app.route("/transaltee", methods=['POST', 'GET'])
def transaltee():
    return AudioProceesing().compareKural()


# N-gram Prediction Game Routes
@app.route('/ngram/game', methods=['GET'])
@login_required
def ngram_game():
    return kural().ngram_game()


@app.route('/ngram/get_kural', methods=['GET'])
@login_required
def get_ngram_kural():
    return kural().get_ngram_kural()


@app.route('/ngram/predict', methods=['POST'])
@login_required
def ngram_predict():
    return kural().ngram_predict()


@app.route('/ngram/submit_score', methods=['POST'])
@login_required
def submit_ngram_score():
    return kural().submit_ngram_score()


@app.route('/ngram/leaderboard', methods=['GET'])
@login_required
def ngram_leaderboard():
    return kural().ngram_leaderboard()