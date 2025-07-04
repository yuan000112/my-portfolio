# -*- coding: utf-8 -*-
from flask import Flask, render_template, abort

app = Flask(__name__)

SECTIONS = [
    {"slug": "experiences", "title": "經歷"},
    {"slug": "projects",    "title": "作品"},
    {"slug": "skills",      "title": "技能"},
    {"slug": "contact",     "title": "聯絡我"},
]

@app.route('/')
def home():
    return render_template('index.html', sections=SECTIONS)

@app.route('/<section>')
def show_section(section):
    slugs = [s['slug'] for s in SECTIONS]
    if section not in slugs:
        abort(404)
    title = next(s['title'] for s in SECTIONS if s['slug'] == section)
    return render_template(f'{section}.html', title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

