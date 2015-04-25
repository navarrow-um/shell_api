# shell_api
Flask micro service 

Install

git clone https://github.com/navarrow-um/shell_api.git

cd shell_api/

virtualenv venv/

source venv/bin/activate

venv/bin/pip install flask

./shell_api.py



#Simple TEST

Check if exists ls command

curl http://localhost:5000/v1.0/shell/ls


{
  "output": "/bin/ls"
}


List / directory

curl -s -u admin:admin http://localhost:5000/v1.0/shell -X POST -H "Accept: application/json" -H "Content-type: application/json" -d '{"command":"ls","args":"/"}'  

{
  "output": "bin\nboot\nboot-sav\ncdrom\ndev\netc\nhome\ninitrd.img\ninitrd.img.old\nlib\nlib64\nlost+found\nmedia\nmnt\nopt\nproc\nroot\nrun\nsbin\nsrv\nsys\ntmp\nusr\nvar\nvmlinuz\nvmlinuz.old"
}


