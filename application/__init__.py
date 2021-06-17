from flask import Flask, jsonify, request
from application.model.entity.medicoes import Medicoes

app = Flask(__name__)

from application.controller import app_controller