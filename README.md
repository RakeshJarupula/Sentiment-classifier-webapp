# Sentiment-classification-webapp
This is beginner project on sentiment classification. The machine learning model is trained on IMDB dataset. This web application is deployed to Heroku platform. 

The skills and tools used are:

* Python's `requests` package.
* Python's `flask` web framework.
* working with JSON.
* modular programming.

When a client visits the application, it:

1. gets the client's IP address.
2. uses the IP address to look up their location.
3. uses their location data to greet them with temperature of the city they are located in.

## Prerequisites

All required Python packages can be found in the `requirements.txt` file. Additionally, the provided `Makefile` can be used to create a virtual environment by running `make venv`. You will also need a Heroku account, and to have installed the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

## Running the app locally using Flask

You may want to run the app using Flask locally before deploying it to Heroku, especially if you have made any changes to the code. To run locally (with a Unix-like OS):

1. clone the repository.
2. in the repository, run `make deploy`.
3. open the link provided in the command line.

If you are using Windows, you can:

1. create and activate the virtual environment.

        py -3 -m venv venv
        venv\Scripts\activate.bat

2. `set FLASK_APP=app` in the command line.
3. run `python -m flask run`.
4. open the link in the command line.

## Deploying to Heroku

Make sure your app is ready to be deployed to Heroku by running Flask locally. To deploy to Heroku:

1. clone the repository (if you haven't yet).
1. `heroku login` and enter your credentials.
1. `heroku create` or `heroku create app-name` where app-name is a custom app name.
1. `git push heroku master`.
1. `heroku config:set DEPLOY=heroku`.
1. `heroku open` or open the app online through your Heroku profile.

## Future work

Since this is a short demonstration of what you can do using Python to create web applications, consider extensions to the project. Some ideas include:

1. showing a plot of the forecast.
2. using their location to display other location specific data.

## Contributing to this project

Please see the contributing guidelines found in [`CONTRIBUTING.md`](CONTRIBUTING.md).
