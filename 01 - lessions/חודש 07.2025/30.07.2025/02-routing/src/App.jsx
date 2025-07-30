import { Routes, Route, Link } from 'react-router-dom';
import Home from './Pages/Home';
import About from './Pages/About';
import NotFound from './Pages/NotFound';

function App() {
  return (
    <div>
      <nav>
        <Link to="/">בית</Link> |
        <Link to="/about">אודות</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
