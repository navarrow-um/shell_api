# shell_api
#Flask micro service 

#Install

git clone https://github.com/navarrow-um/shell_api.git
cd shell_api/
virtualenv ./
source bin/activate
bin/pip install flask
./shell_api.py



#Simple TEST

curl http://localhost:5000/v1.0/shell/ls


{
  "output": "/bin/ls"
}
