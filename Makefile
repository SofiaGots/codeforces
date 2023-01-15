
all:
	ssh-add
	git add ./*
	git commit -m "autoupdated at ${date}"
	git push
