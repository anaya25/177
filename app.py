from flask import Flask, jsonify
import random

app = Flask(__name__)

templates = [
   
    {
        "inputs":5,
        "category":"Sports",
        "word":"Chess"
        
    },
    {
        "inputs":6,
        "category":"European Country Name",
        "word":"France"
        
    },
    {
        "inputs":8,
        "category":"Indian Dish",
        "word":"Chokha Batee"
        
    },
    {
        "inputs":2,
        "category":"Luxury Car",
        "word":"Jaguar"
        
    },
]

@app.route("/")
def index():
    return jsonify({
        "status" : "success",
        "word" : random.choice(templates)
    })