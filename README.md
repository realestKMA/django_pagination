# Django Up

A template to quickly get up and coding your [Django](https://www.djangoproject.com/) apps.


## The Why, What & How
#

## Why Djangoup ?

As a Django developer, while starting a new project, i find myself doing the same thing over and over again. That is, setting up a docker environment for development, installing django, running the ```startproject``` command and more.

## What will Djangoup accomplish ?

The goal of this ```repo``` is to instantly spin up a django environment for development, with the following as key factors :-

* Consistency.
* Simplicity.
* Easy of use.


## How to use Djangoup ?
At this point, it is safe to say you are familiar with [Python](https://www.python.org/) & [Django](https://www.djangoproject.com/).

> Make sure to have docker and docker compose installed on your system, this will be needed as this project is designed to run in a docker environment. Please refer to [Docker](https://docs.docker.com/) to get started with docker if you need to.


### To get started

* Clone this repo
    ```cmd
    $ git clone https://github.com/realestKMA/djangoup.git
    ```
* move into repo directory: 
    ```cmd 
    $ cd djangoup
    ```

* create an ```.env``` file with data from the ```.env.sample``` and fill the required details:
    ```cmd
    $ cp .env.sample .env
    ```
* Build the docker compose file using the dev yaml file:
    ```cmd
    $ docker compose -f docker-compose.dev.yml build
    ```
* Bring up the docker compose file and start coding:
    ```cmd
    $ docker compose -f docker-compose.dev.yml up
    ```

Your project is now up and ready for development, you can now access it by visiting [http://127.0.0.1:8000](). Changes made while you code will automatically reflect on the docker instance.
