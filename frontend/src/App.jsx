import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/home';
import CreateLeague from './pages/create';
import Standings from './pages/standings';
import './App.css'; // Ensure the CSS file is imported

function App() {
  return (
    <div className="App">
      <nav className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/create">Create League</Link>
        <Link to="/standings">Standings</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create" element={<CreateLeague />} />
        <Route path="/standings" element={<Standings />} />
      </Routes>
    </div>
  );
}

export default App;