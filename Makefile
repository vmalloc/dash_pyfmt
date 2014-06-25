default: python_format_strings.docset

python_format_strings.rb: cheats.yml generate.py
	python generate.py cheats.yml $@

python_format_strings.docset: python_format_strings.rb
	cheatset generate $<
	open $@
