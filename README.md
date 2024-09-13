# NovelNudge

**NovelNudge** is an AI-powered book recommendation system that suggests personalized reads based on your favorite titles. This project is built using Python, Flask, and Scikit-learn.

## Features

- **Personalized Recommendations**: Get book suggestions tailored to your preferences.
- **RESTful API**: A simple API to return recommendations.
- **Scalable**: Easy to deploy on platforms like Heroku or run locally.

## Project Structure

- `src/` : Contains the main application code.
  - `app.py` : The Flask API that serves the recommendations.
  - `recommendation.py` : The recommendation engine logic.
- `data/` : Directory to store datasets like the Book-Crossing dataset.
- `requirements.txt` : Lists the dependencies required to run the project.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ignisko/NovelNudge.git
   cd NovelNudge
