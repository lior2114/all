import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { onAuthStateChanged } from "firebase/auth";
import { auth } from "../firebase";
import { getMovies } from "../api/moviesApi";

export default function Home() {
    const [loading, setLoading] = useState(true);
    const [movies, setMovies] = useState([]);
    const [moviesLoading, setMoviesLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            if (!user) {
                navigate("/login", { replace: true });
            } else {
                setLoading(false);
                loadMovies();
            }
        });
        return () => unsubscribe();
    }, [navigate]);

    const loadMovies = async () => {
        try {
            setMoviesLoading(true);
            const moviesData = await getMovies();
            setMovies(moviesData);
        } catch (error) {
            console.error("Error loading movies:", error);
        } finally {
            setMoviesLoading(false);
        }
    };

    if (loading) {
        return (
            <div className="loading-container">
                <h1>Loading...</h1>
            </div>
        )
    }

    return (
        <div className="home-container">
            <div className="home-header">
                <h1>Welcome to My Firebase App</h1>
                <p>Your personal movie collection</p>
                <div className="home-actions">
                    <button 
                        onClick={() => navigate("/add-movie")}
                        className="primary-btn"
                    >
                        + Add New Movie
                    </button>
                    <button 
                        onClick={() => navigate("/movies")}
                        className="secondary-btn"
                    >
                        View All Movies
                    </button>
                </div>
            </div>

            <div className="recent-movies-section">
                <h2>Recent Movies</h2>
                {moviesLoading ? (
                    <div className="loading-movies">
                        <p>Loading movies...</p>
                    </div>
                ) : movies.length === 0 ? (
                    <div className="no-movies">
                        <h3>No movies yet</h3>
                        <p>Start by adding your first movie!</p>
                        <button 
                            onClick={() => navigate("/add-movie")}
                            className="add-first-movie-btn"
                        >
                            Add Your First Movie
                        </button>
                    </div>
                ) : (
                    <div className="movies-preview">
                        {movies.slice(0, 6).map((movie) => (
                            <div key={movie.id} className="movie-preview-card">
                                <h3>{movie.title}</h3>
                                <p>{movie.description}</p>
                                <div className="movie-preview-meta">
                                    <span className="movie-type">{movie.type || "General"}</span>
                                    <span className="movie-date">
                                        {movie.createdAt?.toDate?.() 
                                            ? new Date(movie.createdAt.toDate()).toLocaleDateString()
                                            : "Date not available"
                                        }
                                    </span>
                                </div>
                            </div>
                        ))}
                        {movies.length > 6 && (
                            <div className="view-more-movies">
                                <button 
                                    onClick={() => navigate("/movies")}
                                    className="view-all-btn"
                                >
                                    View All {movies.length} Movies
                                </button>
                            </div>
                        )}
                    </div>
                )}
            </div>
        </div>
    )
}