#### Clone project repo
```
 $ git clone https://github.com/Bkumar28/django_survey_app.git
```
 
#### Use Python Version
 - Python 3.8

#### Create virtual environment
```
$ virtualenv venv -p python3
```

#### Activate virtual environment

```
$ source venv/bin/activate
```
#### Go to the project directory

```
$ cd django_survey_app/
```

#### Install dependency

```
$ pip3 install -r requirements.txt
```

#### Migration command

```
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Create super admin user

```
$  python manage.py createsuperuser
>>>  username : super_admin
>>>  email_address : kumar.bhart28@gmail.com
>>>  password : admin@1234
>>>  password (again): admin@1234
```

#### Run django server
```
$ python3 manage.py runserver
```

#### Open swagger in browser
```
http://127.0.0.1:8000/swagger/
```

#### Survey List API
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys
- Request Method - GET

#### Survey Post API
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys
- Request Method - POST
- Request Payload
```
{
  "title": "Survey Questions",
  "description": "Survey Questions",
  "start_date": "2021-10-25T15:17:02.453Z",
  "expired_date": "2021-11-26T15:17:02.453Z",
  "status": "D",
  "questions": [
    {
      "title": "How many employees work at your company?",
      "field_type": "N",
      "is_required": false
    },
    {
      "title": "How would you classify your role?",
      "field_type": "T",
      "is_required": true
    },
    {
      "title": "How would you classify your industry?",
      "field_type": "T",
      "is_required": true
    },
    {
      "title": "What is your favorite product?",
      "field_type": "T",
      "is_required": true
    },
    {
      "title": "What additional features would you like to see in this product?",
      "field_type": "T",
      "is_required": false
    },
    {
      "title": "Are we meeting your expectations?",
      "field_type": "T",
      "is_required": true
    },
    {
      "title": "How satisfied are you with our customer support?",
      "field_type": "T",
      "is_required": true
    },
    {
      "title": "How can we be more helpful?",
      "field_type": "T",
      "is_required": false
    },
    {
      "title": "How many hours a day do you spend on a computer?",
      "field_type": "N",
      "is_required": true
    },
    {
      "title": "How would you rate us on a scale of 1 to 10?",
      "field_type": "N",
      "is_required": true
    }
  ]
}
```

#### Single Survey Get API
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys/1
- Request Method - GET

#### Single Survey Update API
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys/1
- Request Method - PUT
- Request Payload
```
{
  "status": "S",
  "questions": [
    {
       "id": 1,
      "is_required": false,
      "action_type" : "PUT"
    },
    {
      "title": "Was this article useful?",
      "field_type": "N",
      "is_required": true,
      "action_type" : "POST"
    },
    {
       "id": 2,
      "action_type" : "DELETE"
    }
  ]
}
```

#### Single Survey Delete API
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys/1
- Request Method - DELETE


#### Send survey to other user
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys/1/send
- Request Method - POST
- Request Payload

```
{
  "email": "user@example.com" 
}
```

#### Survey answer list
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys/1/answers
- Request Method - GET

#### Post survey answer 
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys/1/answers
- Request Method - POST
- Request Payload
```
{
  "answers": [
    {
      "question_id": 1,
      "ans": 100
    },
    {
      "question_id": 2,
      "ans": "Individual Contributor"
    },
    {
      "question_id": 3,
      "ans": "Technology/software"
    },
    {
      "question_id": 4,
      "ans": "My favorite product is Amazon Kindle Paperwhite because it gives the ultimate reading experience. It’s an e-reader designed and marketed by Amazon. I love this product because it has solved a lot of user  problems for me."
    },
    {
      "question_id": 5,
      "ans": "More filtered sub-category of the product. For example in diapers, Diapers with pants style or normal diapers. I always need to look at image to confirm, is it pant style or not ?"
    },
    {
      "question_id": 6,
      "ans": "Weather can effect me harshly. The lightly stormy day is wracking me in spasms. Thank you Quora for distracting me between the painful episodes. I’m stuck in my very slow, very painful mode today - AND IT WAS NOT MY PLAN!"
    },
    {
      "question_id": 7,
      "ans": "Amazon, one of the most popular eCommerce websites in the globe, seems to be exceeding user expectations  by collecting all kinds of information. What we like: Amazon makes information easily accessible in a knowledge base so users can find answers and troubleshoot on their own. This reduces the chances of incorrect purchases, which can make all the difference in a customer's buying decisions."
    },
    {
      "question_id": 8,
      "ans": "The Community is intended to provide helpful, relevant content to customers. Content you submit should be relevant and based on your own honest opinions and experience. "
    },
    {
      "question_id": 9,
      "ans": "5"
    },
    {
      "question_id": 10,
      "ans": "8"
    }
  ]
}
```

#### Survey reports
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys/1/report
- Request Method - GET
- sample response
```buildoutcfg
{
  "data": {
    "id": 5,
    "title": "Survey 1",
    "description": "Survey Description",
    "start_date": "2021-10-23T15:17:02Z",
    "expired_date": "2021-11-24T15:17:02Z",
    "status": "S",
    "reports": {
      "total_submission": 4,
      "anonymous_user": 3,
      "invited_user": 1,
      "total_answer": 39,
      "total_unanswer": 1,
      "popular_answer": {
        "total": 4,
        "question": "Are we meeting your expectations?"
      },
      "unpopular_answer": {
        "total": 1,
        "question": "How can we be more helpful?"
      }
    }
  },
  "status": "success",
  "code": 200
}
```


#### Get my submitted survey answers
- API Endpoint - http://127.0.0.1:8000/api/v1/surveys/1/answers/asop2323zdds34sdsd
- Request Method - GET
