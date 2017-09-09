<h1>Movies Trailer</h1>

## Project Title

Server-side code to store a list of your favorite movies and
generate a web page allowing visitors to browse the title and the
trailers of these movies

## Table of Contents
<ul>
	<li><a href="#Getting Started">Getting Started</a>
	<ul>
		<li><a href="Prerequisites">Prerequisites</a></li>
	</ul>
	</li>
	<li><a href="#Downloading repository to local">Downloading repository to local</a>
	</li>
	<li><a href="#Running the program with IDLE">Running the program with IDLE</a>
	</li>
	<li><a href="#Built With">Built With</a>
	<ul>
		<li><a href="Modules">Modules</a></li>
		<li><a href="Authors">Prerequisites</a></li>
	</ul>
	<li><a href="#Acknowledgments">Acknowledgments</a></li>
</ul>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure Python 2.7(or later version) is installed<br />
Make sure an application called Idle is installed and ready to run

## Downloading repository to local


* Fork the current repository to create your own copy in Github. 
* Clone the repository and donwnload the zip folder containing 
the following files:
```
.DS_Store, .gitignore, README.md, entertainment_center.py, 
fresh_tomatoes.pymeadia.py, fresh_tomatoes.pymeadia.pyc,
media.py, media.pyc
```
## Running the program with IDLE

* Opening the python file
* Run IDLE. A "Python Shell" window will be opened.
* Click File, Open 
* Choose the "entertainment_center.py" document in your local directory. A new window of "entertainment_center.py" will be opened.


* Create new instances of class Movie just like the existing instances <br />
"terminator", "god", "metal", "iron" in the following format: 
```
new_instance = media.Movie("movie_title", "movie_storyline", 
"poster_image_url_link", "trailer_youtube_url_link")
```

* Add these new instances to the array called movies 
in the following format:
```
movies = [new_inst_1, new_inst_2, new_inst_3, new_inst_4]
```
* Select Run
* Run Module(by pressing F5)

Upon running, an html file will be generated in the same 
directory where the python files are downloaded and a webpage 
will be opened with your default web browser, showing names as 
well as images of your favourite movies. By clicking on one of 
the displayed images, trailer for the movie will be played.

## Built With

### Modules:

* [Module: webbrowser, os, re]- Stdlib from python library

### Authors

* **Xiaofan Liu** - *Initial work* - [adarsh0806](https://github.com/adarsh0806)


## Acknowledgments

* Audacity.com
* Full Stack Web Developer Nanodegree Program
* Project Movie Trailer Website

