# Chinese-BBB-Web

Currently we support python3 only.
### Steps to run this app:
0. Create Environment variables like QICHACHA_APPKEY or TENCENT_APPKEY
(or define them in .env file)
1. virtualenv -p python3 env

2. source env/bin/activate

3. pip install -r requirements.txt

4. python application.py(use -p to specify binding port)

### Steps to Verify API:
1. Login:

curl -b cookies.txt -c cookies.txt -H "Content-Type: application/json" -X POST 'http://localhost:5000/api/login' -d '{"phone_num":"az", "password":"az"}'

2. Whether a phone number exists:

curl -H "Content-Type: application/json" -X GET 'http://localhost:5000/api/phone_exist/17782583329'

3. Register:
curl -H "Content-Type: application/json" -X POST 'http://localhost:5000/api/register' -d '{"phone_num": "133", "password":"133", "sex":"female"}'

4. fuzzy Qichacha query:
curl -b cookies.txt -c cookies.txt -H "Content-Type: application/json" -X POST 'http://localhost:5000/api/fuzzy_query' -d '{"keyword": "baidu"}'


### To do List:

- [x] build the fundamental backends based on flask rest plus and test out its functionality
- [x] Adding [flask documentation generation](https://flask-restplus.readthedocs.io/en/0.2/documenting.html) support
- [x] Initialize the work of sqlAlchemy framework using flask migration
- [ ] Adding all API routing rules required from [API doc](https://github.com/chinese-bbb/documents/blob/master/api-summary.md)
- [ ] Adding [flask unit test module](http://flask.pocoo.org/docs/1.0/testing/)
- [ ] Encrypt the app.db. Today the DB is plain and doesn't require credentials.
- [ ] After MVP stage, move the db to production S3 storage.


### Steps to evolve database schema:

1. Change Models which manages the source of truth schema. E.g, app/models.py

2. flask db migrate -m "posts table"

3. flask db upgrade

Done! The database should have evolved schema.


### Steps to launch the flask app on AWS at the first time:

1. pip install awsebcli (Inside the python virtual environment)

2. eb init. Select us-east-2

3. eb create

### Steps to update the flask app on AWS:

1. Change code.

2. eb deploy

3. Whenevery you need to ssh into the EC2 machine. Do 
	eb ssh <EB environment name>


### Steps to add Environment Variables:

1. Log in Aws Console and access Application page

2. Modify Configuration and Add Environment Variables

3. Call os.environ[KEY] to fetch the Value of Environment Variable.

