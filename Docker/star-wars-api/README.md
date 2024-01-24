Project Overview

This Node.js application is a simple server built with Express.js. It's designed to manage a list of favorite movies or characters, leveraging a MongoDB database for storage. The application also integrates external API calls to fetch movie and character data.

Features

List Favorites: Retrieve a list of favorite items stored in the database.
Add Favorites: Add new favorite items, with validations for item types.
Fetch Movie Data: External API integration to fetch movie data.
Fetch Character Data: External API integration to fetch character data.
Prerequisites
Before you begin, ensure you have met the following requirements:

Node.js installed on your system.
MongoDB running locally or accessible via a MongoDB URI.

Installation

Clone the repository to your local machine:

git clone https://github.com/Imperfectwow/star-wars-api.git

cd [Project-Folder-Name]

npm install

Configuration

Set up your MongoDB URI in the connection string in the application, or set it as an environment variable.


Running the Application

To start the server, run: node app.js

The server will start running on http://localhost:3000.


Endpoints

GET /favorites: Returns all favorites from the database.
POST /favorites: Add a new favorite item. Requires name, type, and url in the request body.
GET /movies: Fetches movie data from an external API.
GET /people: Fetches character data from an external API.
