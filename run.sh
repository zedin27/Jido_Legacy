#!/bin/sh

if ! [ -e venv ]
then
	virtualenv venv
	. venv/bin/activate
	pip3 install -r requirements.txt
fi
	. venv/bin/activate