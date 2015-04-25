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


curl http://localhost:5000/v1.0/shell/ls


{
  "output": "/bin/ls"
}
