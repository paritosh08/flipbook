if ! command -v pip
then
	if ! command -v pip3
	then
		echo Please check if pip is installed
	else
		pip3 install fpdf
		pip3 install Pillow
	fi
else
	pip install fpdf
	pip install Pillow
fi

