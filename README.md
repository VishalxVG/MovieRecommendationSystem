# Movie Recommendation System

This project implements a movie recommendation system using machine learning techniques, integrated with a web interface using Streamlit. It utilizes NLTK for stemming text data, Scikit-learn for building the recommendation model, and the TMDB API for fetching movie posters related to the recommended movies.

## Tech Stack

- **Python**: Core programming language.
- **Scikit-learn**: Machine learning library for building the recommendation model.
- **NLTK**: Natural Language Toolkit for text processing and stemming.
- **Streamlit**: Open-source app framework for creating web interfaces.
- **TMDB API**: The Movie Database API for fetching movie information and posters.
- **Pickle**: For saving and loading the recommendation model as a `.pkl` file.

## ## Database

- You can download the database file [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).


## How It Works

1. **Data Collection**: Movie data is fetched from a dataset.
2. **Preprocessing**: Text data is preprocessed using NLTK for stemming and other text processing tasks.
3. **Model Training**: A recommendation model is trained using Scikit-learn, possibly collaborative filtering or content-based filtering.
4. **Web Interface**: The recommendation system is deployed using Streamlit to provide an interactive web interface.
5. **Fetching Posters**: TMDB API is used to fetch movie posters based on the recommended movies.

## Database

[Describe your database here if using SQLite/MySQL/PostgreSQL]

## Pickle File

The trained recommendation model is saved as a `.pkl` file using Python's `pickle` module for easy loading and usage in other Python scripts.

## Installation

Follow these steps to set up and run the project:

### Prerequisites

- Python 3.x
- Git

### Steps

1. **Clone the Repository**

    ```sh
    git clone https://github.com/your_username/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Create a Virtual Environment and Activate It**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**

    Create a `.env` file in the root directory and add necessary API keys or other configurations.

5. **Run the Streamlit App**

    ```sh
    streamlit run app.py
    ```

6. **Open the Web Interface**

    Open your web browser and go to `http://localhost:8501` to use the movie recommendation system.

## Screenshots

![](https://github.com/VishalxVG/MovieRecommendationSystem/blob/main/Screenshot%20(101).png)


## Usage

1. Select a user or input preferences to get personalized movie recommendations.
2. Explore recommended movies and view their posters fetched from TMDB.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Scikit-learn](https://scikit-learn.org/)
- [NLTK](https://www.nltk.org/)
- [Streamlit](https://www.streamlit.io/)
- [TMDB API](https://www.themoviedb.org/documentation/api)

---

