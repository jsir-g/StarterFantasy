import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/home';
import CreateLeague from './pages/create';
import Standings from './pages/standings';

function App() {
  return (
    <div className="App">
      <nav style={{ marginBottom: '1rem' }}>
        <Link to="/" style={{ marginRight: '1rem' }}>Home</Link>
        <Link to="/create" style={{ marginRight: '1rem' }}>Create League</Link>
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
