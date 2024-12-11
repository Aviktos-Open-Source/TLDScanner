NAME=TLDScanner

$(NAME): clear
	python3 -m TLDScanner.main google src/TLDScanner/data --format json

clear:
	@clear