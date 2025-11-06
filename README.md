# Networking-Practice-Tools
This repository contains 3 tools for revising and practicing networking concepts.

- **binary parctice.html** - interactive/graphical tool for practicing binary-decimal conversion 
- **subnet analysis practice.html** - web page for practicing subnetting 
- **quiz.py** - a CLI-based quiz with ~550 questions that cover topics from the CCNA exam outline

Scroll down for more details.

## Binary Practice Tool
<img src="https://github.com/NickMakeThing/Networking-Practice-Tools/blob/main/demo/binary.gif?raw=true" alt="binary.gif" width="800">
Built with JavaScript, CSS, and HTML.<br />
Runs in a typical web browser.<br />
Click bits in a byte to flip them.<br /> 
Successfully creating a byte that matches with the presented decimal number will clear the screen and present a new challenge.

## Subnetting Practice Tool
<img src="https://github.com/NickMakeThing/Networking-Practice-Tools/blob/main/demo/subnet.gif?raw=true" alt="subnet.gif" width="800">
Built with JavaScript, CSS, and HTML.<br />
Runs in a typical web browser.<br />
Calculate and enter the correct IP addresses, address count, and subnet count.<br /> 
Successfully entering the correct information will clear the screen and present a new challenge.<br />
Switching between the CIDR and Classful options requires a refresh.

## CCNA Quiz
<img src="https://github.com/NickMakeThing/Networking-Practice-Tools/blob/main/demo/quiz.png?raw=true" alt="quiz.png" width="800">
Built with Python (3.13.1)<br />
On running, the user will be asked questions from a specific topic.<br />
Questions will be randomly selected until all questions from that topic have been asked, and then the user will be asked questions from another topic.<br />
Numbers on the left of the question tell us how many questions have been asked (x), and how many questions are left in the current topic (y) in q(x/y).<br />
Questions that have been answered incorrectly 3 times in a row will be saved to wrong.json. 

#### Useful Functions
- `ask(category_name)` asks questions from a specific topic, and takes a str arg
- `quiz_wrong()` asks questions from wrong.json
- `whole_quiz()` asks every question from every topic

#### Quiz Files
- quiz.py - contains the main logic.
- ccna_questions.py - contains a dict of ~550 questions and their answers.
- wrong.json - this file will be created on running the script. 

#### Older Versions of Python
The `ask(category_name)` function may fail in older versions of python3. \
In this case, insert ```asked = state['asked']``` between lines 88 and 89. \
Then replace ```print(f'\nq({state['asked']}/{len(questions)}) {category_name}: {q}\n')``` with ```print(f'\nq({asked}/{len(questions)}) {category_name}: {q}\n')```
