import { Routes, Route, useNavigate } from 'react-router-dom';
import Home from './pages/home';
import CreateLeague from './pages/create';
import Standings from './pages/standings';
import './App.css';

function App() {
  const navigate = useNavigate();

  return (
    <div className="App">
<div className="button-container">
  <button className="nav-buttons" onClick={() => navigate('/')}>Home</button>
  <button className="nav-buttons" onClick={() => navigate('/create')}>Create League</button>
  <button className="nav-buttons" onClick={() => navigate('/standings')}>Standings</button>
</div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create" element={<CreateLeague />} />
        <Route path="/standings" element={<Standings />} />
      </Routes>
    </div>
  );
}

export default App;