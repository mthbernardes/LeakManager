# LeakManager

# Install
<pre>
sudo apt-get install mongodb-org screen
pip3 install -r requeriments.txt
</pre>

# Usage
<pre>
screen -S leakManager
hug -f index.py -p 1337
OR
gunicorn index:__hug_wsgi__ -b 0.0.0.0:1337
OR
uwsgi --http 0.0.0.0:1337 --wsgi-file index.py --callable __hug_wsgi__
ctrl + a + d
</pre>

# Change user/passwd
<pre>
edit etc/LeakManager.conf file
</pre>

# MassInsert
<pre>
CSV Format
email,username,password,database

CSV Format example:
admin@admin.com,admin,admin1234,appXPTO
jose@admin.com,,zezin123,appXPTO
paula@admin.com,paula,123456,appXPTO
zika@admin.com,virus,nicole,appXPTO

</pre>
![LeakManager](leakManager.png)
