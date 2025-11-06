from ccna_questions import questions_dict
# from linux_questions import questions_dict
from random import shuffle
import json
import os
qs_dict = {} # 'category':{ {'answer','partofanswer'}:['question','questionwithsameanswer'], ... }, ... 
state = {
    'asked':0, #how many questions have been asked
    'save':True, #quizing using wrong.json sets this to false
    # 'total':0 #total number of questions in current + previous categories
}

#json.dump doesnt take sets.
def convert_to(wrong,type):
    for category in wrong:
        if type == 'list':
            wrong[category] = list(wrong[category])
        elif type == 'set':
            wrong[category] = set(wrong[category])

    return wrong 

def save(wrong):
    if not state['save']:
        return 
    
    wrong_copy = convert_to(wrong.copy(),'list')
    with open("wrong.json", "w") as f:
        json.dump(wrong_copy, f)

def load():
    if "wrong.json" not in os.listdir():
        return {}

    with open("wrong.json", "r") as f:
        return convert_to(json.load(f), 'set')

#abstracts part of fix_dicts
#helps ensure case sensitivity, spaces, hyphens don't result in rejecting right answers
def fix_answers(answers):
    new_answers = []
    for a in answers:
        new_answers.append(a.replace(' ','').replace('-','').lower())

    return frozenset(new_answers)

def fix_dicts(questions_dict=questions_dict): #unfortunate consequence of bad planning
    #don't squint, it's offensive.
    for k in questions_dict.keys():
        qs_dict[k] = {}
        for answers, questions in questions_dict[k].items():
            qs_dict[k][fix_answers(answers)] = questions

        if k not in wrong:
            wrong[k] = set()

def parse_answer(answer):
    answer = answer.replace(' ','').replace('-','').lower().split(',')
    
    # bandaid fix for one of the answers
    if answer[0] == 'switchporttrunkallowed10':
        answer = {','.join(answer)}

    return frozenset(answer)

def check_answer(category_name,question,answer):
    answer = parse_answer(answer)
    if answer not in qs_dict[category_name] or question not in qs_dict[category_name][answer]:
        return 'wrong'

def get_questions(category_name):
    if not state['save']: 
        questions = list(wrong[category_name])
    else:
        questions = sum(list(qs_dict[category_name].values()),[]) #gets flat list of questions (no answers)

    # state['total'] += len(questions)
    shuffle(questions)
    return questions


def ask(category_name): 
    questions = get_questions(category_name)
    state['asked'] = 0

    for q in questions:
        state['asked'] += 1
        attempts = 3
        while(attempts>0):
            print(f'\nq({state['asked']}/{len(questions)}) {category_name}: {q}\n')
            answer = input(f'{attempts} attempts> ')
            result = check_answer(category_name,q,answer)
            if result == 'wrong':
                attempts -= 1
            else:
                break

        if attempts < 1: 
            print('attempts exhausted.')
            wrong[category_name].add(q)
            save(wrong)
         

def mixed_quiz(): #mixes all topics together
    pass 

def whole_quiz():
    for category in qs_dict:
        ask(category)
            
def quiz_wrong():
    state['save'] = False

    for category in wrong:
        if len(wrong[category]):
            ask(category)

wrong = load()

fix_dicts()
# print('\n###############################\n')

# quiz_wrong()
whole_quiz()
# print(wrong)
