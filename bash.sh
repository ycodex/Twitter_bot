#clone
git clone https://github.com/ycodex/Twitter_bot.git
cd Twitter_bot
#install requirements
pip install -r requirements.txt

#run main
python main.py

#commit changes
git config --global user.email "karthiknaik120@gmail.com"
git config --global user.name "ycodex"
git add .

msg="push changes"

git commit -m "$msg"

git remote rm origin
git remote add origin https://ycodex:${GH_TOKEN}@github.com/ycodex/Twitter_bot
git push origin master

