from flask import Blueprint

import os
from flask import render_template, request, flash, redirect, url_for, request

main = Blueprint('main', __name__, static_folder='static', static_url_path='/main/static')


@main.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', title="UpMock")