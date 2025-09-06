import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { addMovie } from "../api/moviesApi";
import { useUser } from "../contexts/UserContext";

export default function AddMovies() {
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [type, setType] = useState("general");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");
  const { user } = useUser();

  useEffect(() => {
    if (!user) {
      navigate("/login", { replace: true });
    } else {
      setLoading(false);
    }
  }, [navigate, user]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!title.trim() || !description.trim()) {
      setError("Please fill in both title and description");
      return;
    }

    setSubmitting(true);
    setError("");

    try {
      await addMovie(title.trim(), description.trim(), type);
      setTitle("");
      setDescription("");
      setType("general");
      navigate("/");
    } catch (err) {
      console.error("Error adding movie:", err);
      setError("Failed to add movie. Please try again.");
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="loading-container">
        <h2>Loading...</h2>
      </div>
    )
  }

  return (
    <div className="add-movie-container">
      <div className="add-movie-form">
        <h2>Add New Movie</h2>
        
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="title">Movie Title:</label>
            <input
              type="text"
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Enter movie title"
              required
              disabled={submitting}
            />
          </div>

          <div className="form-group">
            <label htmlFor="description">Description:</label>
            <textarea
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Enter movie description"
              rows="4"
              required
              disabled={submitting}
            />
          </div>

          <div className="form-group">
            <label htmlFor="type">Movie Type:</label>
            <select
              id="type"
              value={type}
              onChange={(e) => setType(e.target.value)}
              disabled={submitting}
              className="type-select"
            >
              <option value="general">General</option>
              <option value="action">Action</option>
              <option value="drama">Drama</option>
              <option value="comedy">Comedy</option>
              <option value="horror">Horror</option>
              <option value="sci-fi">Sci-Fi</option>
              <option value="romance">Romance</option>
              <option value="thriller">Thriller</option>
              <option value="documentary">Documentary</option>
              <option value="animation">Animation</option>
            </select>
          </div>

          <div className="form-actions">
            <button
              type="submit"
              disabled={submitting}
              className="submit-btn"
            >
              {submitting ? "Adding..." : "Add Movie"}
            </button>
            
            <button
              type="button"
              onClick={() => navigate("/")}
              disabled={submitting}
              className="cancel-btn"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
