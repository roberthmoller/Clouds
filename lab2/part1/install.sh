#/bin/env bash

echo "Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip nginx

# Flask setup 
echo "Setting up Flask"
mkdir -p www/flaskapp
cd www/flaskapp
pip3 install virtualenv	
python3 -m virtualenv flaskenv 	
chmod 755 flaskenv/
# From here is not working from the script
source flaskenv/bin/activate
export FLASK_APP=$(pwd)/app.py
echo "Starting flask application on port 5000"
flask run --host 0.0.0.0 --port 5000 &

# Nginx setup
echo "Setting up nginx"
sudo echo "server{
	listen 80;
	location / {
		proxy_pass http://localhost:5000;
	}
}" > /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
echo "Done"