#Dockerfile, Image, Container

FROM python:3.12

##ADD [source file] [file directory]
ADD top250letterboxd.py . 

RUN pip install requests bs4

CMD [ "python", "./top250letterboxd.py" ]

#TO RUN IN TERMINAL:    
# docker build -t top250letterboxd-docker-practice . 
# docker run top250letterboxd-docker-practice

# Run docker build everytime you make changes to source files