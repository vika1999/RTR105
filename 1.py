
#!/bin/bash
if [ # == 1 ]
then
git config --global user.email viktorija.99@mail.ru
git add . 
#git commit -m "20171012_09_55"
git commit -m $1
git push origin master
fi
