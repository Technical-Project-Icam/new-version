# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:45:35 2024

@author: kslw
"""

from flask import Flask, jsonify
from scraper.scraper import scrape_quotes

app = Flask(__name__)

@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    try:
        data = scrape_quotes()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
