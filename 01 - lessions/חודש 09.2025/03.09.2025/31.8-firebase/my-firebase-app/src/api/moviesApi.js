import { 
  collection, 
  addDoc, 
  getDocs, 
  getDoc, 
  doc, 
  updateDoc, 
  deleteDoc, 
  serverTimestamp,
  query,
  orderBy,
  limit,
  where,
  startAfter
} from "firebase/firestore";
import { db } from "../firebase";

// Add a new movie to the database
export async function addMovie(title, description, type = "general") {
  try {
    const docRef = await addDoc(collection(db, "movies"), {
      title,
      description,
      type,
      createdAt: serverTimestamp()
    });
    return { id: docRef.id };
  } catch (error) {
    console.error("Error adding movie: ", error);
    throw error;
  }
}

// Get all movies from the database
export async function getMovies() {
  try {
    const snapshot = await getDocs(collection(db, "movies"));
    return snapshot.docs.map(d => ({ id: d.id, ...d.data() }));
  } catch (error) {
    console.error("Error getting movies: ", error);
    throw error;
  }
}

// Get a single movie by ID
export async function getMoviebyid(id) {
  try {
    const docRef = doc(db, "movies", id);
    const docSnap = await getDoc(docRef);
    //אם יש לך סרט עם ID "abc123":
    // שורה 48 יוצרת הפניה ל: movies/abc123
    // שורה 49 קוראת את כל המידע של הסרט הזה (שם, שנה, תיאור וכו')
    
    if (docSnap.exists()) {
      return { id: docSnap.id, ...docSnap.data() };
    } else {
      throw new Error("Movie not found");
    }
  } catch (error) {
    console.error("Error getting movie: ", error);
    throw error;
  }
}

// Update an existing movie
export async function updateMovie(id, updates) {
  try {
    const docRef = doc(db, "movies", id);
    await updateDoc(docRef, {
      ...updates,
      updatedAt: serverTimestamp()
    });
    return { success: true };
  } catch (error) {
    console.error("Error updating movie: ", error);
    throw error;
  }
}

// Delete a movie by ID
export async function deleteMovie(id) {
  try {
    const docRef = doc(db, "movies", id);
    await deleteDoc(docRef);
    return { success: true };
  } catch (error) {
    console.error("Error deleting movie: ", error);
    throw error;
  }
}

// Get movies with pagination
export async function getMoviesPaginated(pageSize = 10, lastDoc = null) {
  try {
    let q = query(
      collection(db, "movies"),
      orderBy("createdAt", "desc"),
      limit(pageSize)
    );
    
    if (lastDoc) {
      q = query(q, startAfter(lastDoc));
    }
    
    const snapshot = await getDocs(q);
    const movies = snapshot.docs.map(d => ({ id: d.id, ...d.data() }));
    
    return {
      movies,
      lastDoc: snapshot.docs[snapshot.docs.length - 1],
      hasMore: snapshot.docs.length === pageSize
    };
  } catch (error) {
    console.error("Error getting paginated movies: ", error);
    throw error;
  }
}

// Search movies by title
export async function searchMovies(searchTerm) {
  try {
    const q = query(
      collection(db, "movies"),
      where("title", ">=", searchTerm),
      where("title", "<=", searchTerm + "\uf8ff")
    );
    
    const snapshot = await getDocs(q);
    return snapshot.docs.map(d => ({ id: d.id, ...d.data() }));
  } catch (error) {
    console.error("Error searching movies: ", error);
    throw error;
  }
}

// Get movies by category (if you add category field later)
export async function getMoviesByCategory(category) {
  try {
    if (category === "all") {
      return await getMovies();
    }
    
    const q = query(
      collection(db, "movies"),
      where("type", "==", category),
      orderBy("createdAt", "desc")
    );
    
    const snapshot = await getDocs(q);
    return snapshot.docs.map(d => ({ id: d.id, ...d.data() }));
  } catch (error) {
    console.error("Error getting movies by category:", error);
    // If there's an error with the query, fall back to getting all movies
    return await getMovies();
  }
}
