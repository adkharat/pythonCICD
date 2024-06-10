# base python image for custom image
FROM python:3.10.12

# create working directory and install pip dependencies
WORKDIR /aviatnetbuild
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy python project files from local to /aviatnetbuild image working directory
COPY . .

# run the lambdaFunction.py file
CMD [ "python3" "lambdaFunction.py"]