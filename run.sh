echo $http_proxy
echo $https_proxy
if [ -f google_appengine/dev_appserver.py ]
then
	python2.5 google_appengine/dev_appserver.py --debug code
else
	echo "ERROR"
	echo "you need to place the google app engine under the google_appengine subdirectory"
	echo "get it here:"
	echo "http://code.google.com/appengine/downloads.html"
fi
