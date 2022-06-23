from flask import Flask,request,render_template
from utils import get_candidates_by_skill,get_candidate_by_id,get_candidates_by_name,load_candidates_from_json

app = Flask(__name__)


@app.route('/')
def load_full():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:x>')
def load_candidate_by_id(x: int):
    candidate = get_candidate_by_id(x)
    return render_template('single.html', candidate=candidate)

@app.route('/search/<name>')
def load_candidate_by_name(name):
    candidates = get_candidates_by_name(name)
    QTY = len(candidates)
    return render_template('search.html', candidates=candidates, QTY=QTY)

@app.route('/skill/<skill>')
def load_candidate_by_skill(skill):
    candidates = get_candidates_by_skill(skill)
    QTY = len(candidates)
    return render_template('skills.html', candidates=candidates, QTY=QTY, skill=skill)




if __name__ == '__main__':
    app.run()
