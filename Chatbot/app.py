from flask import Flask, render_template, request
from googlesearch import search
import requests
import bs4
import os
from bs4 import BeautifulSoup
from chatbot import *
import pickle
from listoperations import *
from mapping import *
from image import location

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if os.path.exists(userText):
    	temp = temp1 = ""
    	try:
    		temp = location(userText)
    	except Exception as e:
    		return "Not an image file path"
    	try:
    		temp1 = str(mapping(temp))
    		return (temp + ",    " + temp1)
    	except Exception as e:
    		if temp != "":
    			return temp
    		else:
	    		return "Can't find the Place"
    userText =userText.lower()
    try:
        return str(mapping(userText))
    except Exception as e:
        return "I am having trouble understanding.<br>Please check your network or refine your query ! <br> "
if __name__ == "__main__":
    app.run()
