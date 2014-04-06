####################################
### Kaleidoscope Powered HelpingHandServer makefile
####################################
SHELL := /bin/bash

#launches the test server address 127.0.0.1:8000
test:
	source /Users/jc/code/helpinghand/server/venv/bin/activate;\
	python /Users/jc/code/helpinghand/server/venv/HelpingHandServer/manage.py runserver

#destroys whole project. Probably don't want to use this unless starting over.
nuke:
	rm -rf dictionary.py dictionary.pyc /Users/jc/code/helpinghand/server/venv req.pip makefile .git *~
