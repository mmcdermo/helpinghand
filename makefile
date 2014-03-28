####################################
### Kaleidoscope Powered HelpingHandServer makefile
####################################
SHELL := /bin/bash

#launches the test server address 127.0.0.1:8000
test:
	source /home/kleene/code/helpinghand/venv/bin/activate;\
	python /home/kleene/code/helpinghand/venv/HelpingHandServer/manage.py runserver

#destroys whole project. Probably don't want to use this unless starting over.
nuke:
	rm -rf dictionary.py dictionary.pyc /home/kleene/code/helpinghand/venv req.pip makefile *~
