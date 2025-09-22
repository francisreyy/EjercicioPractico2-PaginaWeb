#!/bin/bash

if python3 --version; then
	echo "Python ya está instalado"
else
	echo "Python necesita ser instalado"
	sudo apt install python3
fi

if pip3 --version; then
	echo "Pip ya está instalado"
else
	echo "Pip necesita ser instalado"
	sudo apt install python3-pip
fi

sudo apt install python3-venv


mkdir TP2-IDS
cd TP2-IDS

mkdir .venv

mkdir static
cd static
mkdir css
mkdir images
cd ..
mkdir templates
touch app.py

python3 -m venv .venv

. .venv/bin/activate

pip3 install flask
