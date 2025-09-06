import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { 
  getMovies, 
  deleteMovie, 
  searchMovies, 
  getMoviesPaginated,
  getMoviesByCategory 
} from "../api/moviesApi";
import { useUser } from "../contexts/UserContext";

export default function Movies() {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [lastDoc, setLastDoc] = useState(null);
  const [selectedCategory, setSelectedCategory] = useState("all");
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const { user } = useUser();

  const pageSize = 10;

  useEffect(() => {
    if (!user) {
      navigate("/login", { replace: true });
      return;
    }
    loadMovies();
  }, [user, navigate]);

  const loadMovies = async () => {
    try {
      setLoading(true);
      const result = await getMoviesPaginated(pageSize, null);
      setMovies(result.movies);
      setLastDoc(result.lastDoc);
      setHasMore(result.hasMore);
      setCurrentPage(1);
    } catch (err) {
      console.error("Error loading movies:", err);
      setError("Failed to load movies");
    } finally {
      setLoading(false);
    }
  };

  const loadMoreMovies = async () => {
    if (!hasMore || !lastDoc) return;
    
    try {
      const result = await getMoviesPaginated(pageSize, lastDoc);
      setMovies(prev => [...prev, ...result.movies]);
      setLastDoc(result.lastDoc);
      setHasMore(result.hasMore);
      setCurrentPage(prev => prev + 1);
    } catch (err) {
      console.error("Error loading more movies:", err);
      setError("Failed to load more movies");
    }
  };

  const handleSearch = async () => {
    if (!searchTerm.trim()) {
      loadMovies();
      return;
    }

    try {
      setLoading(true);
      const searchResults = await searchMovies(searchTerm.trim());
      setMovies(searchResults);
      setHasMore(false);
      setCurrentPage(1);
    } catch (err) {
      console.error("Error searching movies:", err);
      setError("Failed to search movies");
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryFilter = async (category) => {
    setSelectedCategory(category);
    
    if (category === "all") {
      loadMovies();
      return;
    }

    try {
      setLoading(true);
      const categoryResults = await getMoviesByCategory(category);
      setMovies(categoryResults);
      setHasMore(false);
      setCurrentPage(1);
    } catch (err) {
      console.error("Error filtering by category:", err);
      setError("Failed to filter movies");
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteMovie = async (movieId) => {
    if (!window.confirm("Are you sure you want to delete this movie?")) {
      return;
    }

    try {
      await deleteMovie(movieId);
      setMovies(prev => prev.filter(movie => movie.id !== movieId));
    } catch (err) {
      console.error("Error deleting movie:", err);
      setError("Failed to delete movie");
    }
  };

  const handleEditMovie = (movieId) => {
    navigate(`/edit-movie/${movieId}`);
  };

  if (!user) {
    return null;
  }

  return (
    <div className="movies-container">
      <div className="movies-header">
        <h1>Movies Collection</h1>
        <button 
          onClick={() => navigate("/add-movie")}
          className="add-movie-btn"
        >
          + Add New Movie
        </button>
      </div>

      <div className="movies-controls">
        <div className="search-section">
          <input
            type="text"
            placeholder="Search movies by title..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            onKeyPress={(e) => e.key === "Enter" && handleSearch()}
            className="search-input"
          />
          <button onClick={handleSearch} className="search-btn">
            Search
          </button>
          <button onClick={loadMovies} className="clear-btn">
            Clear
          </button>
        </div>

        <div className="category-filters">
          <button
            onClick={() => handleCategoryFilter("all")}
            className={selectedCategory === "all" ? "active" : ""}
          >
            All
          </button>
          <button
            onClick={() => handleCategoryFilter("action")}
            className={selectedCategory === "action" ? "active" : ""}
          >
            Action
          </button>
          <button
            onClick={() => handleCategoryFilter("drama")}
            className={selectedCategory === "drama" ? "active" : ""}
          >
            Drama
          </button>
          <button
            onClick={() => handleCategoryFilter("comedy")}
            className={selectedCategory === "comedy" ? "active" : ""}
          >
            Comedy
          </button>
          <button
            onClick={() => handleCategoryFilter("horror")}
            className={selectedCategory === "horror" ? "active" : ""}
          >
            Horror
          </button>
          <button
            onClick={() => handleCategoryFilter("sci-fi")}
            className={selectedCategory === "sci-fi" ? "active" : ""}
          >
            Sci-Fi
          </button>
          <button
            onClick={() => handleCategoryFilter("romance")}
            className={selectedCategory === "romance" ? "active" : ""}
          >
            Romance
          </button>
          <button
            onClick={() => handleCategoryFilter("thriller")}
            className={selectedCategory === "thriller" ? "active" : ""}
          >
            Thriller
          </button>
          <button
            onClick={() => handleCategoryFilter("documentary")}
            className={selectedCategory === "documentary" ? "active" : ""}
          >
            Documentary
          </button>
          <button
            onClick={() => handleCategoryFilter("animation")}
            className={selectedCategory === "animation" ? "active" : ""}
          >
            Animation
          </button>
        </div>
      </div>

      {error && (
        <div className="error-message">
          {error}
          <button onClick={() => setError("")} className="close-error">×</button>
        </div>
      )}

      {loading ? (
        <div className="loading-container">
          <h2>Loading movies...</h2>
        </div>
      ) : (
        <>
          <div className="movies-grid">
            {movies.length === 0 ? (
              <div className="no-movies">
                <h3>No movies found</h3>
                <p>Try adding some movies or adjusting your search criteria.</p>
              </div>
            ) : (
              movies.map((movie) => (
                <div key={movie.id} className="movie-card">
                  <div className="movie-content">
                    <h3 className="movie-title">{movie.title}</h3>
                    <p className="movie-description">{movie.description}</p>
                    <div className="movie-meta">
                      <span className="movie-type">{movie.type || "General"}</span>
                      <span className="movie-date">
                        {movie.createdAt?.toDate?.() 
                          ? new Date(movie.createdAt.toDate()).toLocaleDateString()
                          : "Date not available"
                        }
                      </span>
                    </div>
                  </div>
                  <div className="movie-actions">
                    <button
                      onClick={() => handleEditMovie(movie.id)}
                      className="edit-btn"
                    >
                      Edit
                    </button>
                    <button
                      onClick={() => handleDeleteMovie(movie.id)}
                      className="delete-btn"
                    >
                      Delete
                    </button>
                  </div>
                </div>
              ))
            )}
          </div>

          {hasMore && (
            <div className="load-more-section">
              <button 
                onClick={loadMoreMovies}
                className="load-more-btn"
              >
                Load More Movies
              </button>
            </div>
          )}
        </>
      )}
    </div>
  );
}
