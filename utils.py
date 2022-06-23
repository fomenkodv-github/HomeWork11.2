import json

def load_candidates_from_json(file='candidates.json') -> list[dict]:
    with open('candidates.json', encoding='UTF-8') as f:
        json_file = json.loads(f.read())
    return json_file

def get_candidate_by_id(id: int) -> dict:
    for candidate in load_candidates_from_json():
        if candidate.get('id') == id:
            break
    return candidate

def get_candidates_by_name(name: str) -> list[dict]:
    candidates = []
    for candidate in load_candidates_from_json():
        if name.lower() in candidate.get('name').lower().strip().split(' '):
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill: str) -> list[dict]:
    candidates = []
    for candidate in load_candidates_from_json():
        if skill.lower() in candidate['skills'].replace(' ','').lower().split(','):
            candidates.append(candidate)
    return candidates

