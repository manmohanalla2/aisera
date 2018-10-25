
#### Scripts for deploying Aisera Fun Project

main.py: the rest api by flask-restful. Plese run this file for the module.



Compatibility
=============

Flask-RestPlus requires Python 3.6+, Docker.


Docker Image Setup
==================

Build:

	```
    $ docker build -t aisera:0.1 .
    ```

Run:


	```
    $ docker run -d -v /home/ubuntu/mount:/tmp/ -p 5050:5050 aisera:0.1
    ```


1. GET all 

	```http://{host-ip}/api/v1.0/parallel?url=<url>```

	CURL Command:

	```curl -X GET 'http://18.224.24.183/api/v1.0/parallel?url=http%3A%2F%2Fwww.gutenberg.org%2Ffiles%2F15%2Ftext%2F' \
		  -H 'cache-control: no-cache'```

	Return Value:

	```
	{
	  	"data": "data",
	  	"status": "success"
	}
	```

	Reponse Status:

	```
	success : 200
	Fail : 200
	```

2. GET all branch from any project

	```http://{host-ip}/api/v1.0/sequential?url=<url>```

	CURL Command:

	```curl -X GET 'http://18.224.24.183/api/v1.0/sequential?url=http%3A%2F%2Fwww.gutenberg.org%2Ffiles%2F15%2Ftext%2Fmoby-000.txt' \
  		-H 'cache-control: no-cache'```

	Return Value:

	```
	{
	  	"data": 
		    {
		      "preliminary": 1,
		      "this": 6,
		      ......
		    }
	}
	```

	Reponse Status:

	```
	success : 200
	Fail : 200
	```

	Required Parameters:
	- reponame: required
	- groupname: required
	- project_name: optional
