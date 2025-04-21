import { useEffect, useState } from "react";
import "./teams.css";

export default function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const apiBase = import.meta.env.VITE_API_URL || "http://localhost:5000";
    fetch(`${apiBase}/api/teams`)
      .then((res) => res.json())
      .then((data) => {
        setTeams(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch teams:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p className="teams-container">Loading teams...</p>;

  return (
    <div className="teams-container">
      <h1 className="teams-title">NFL Teams</h1>
      <div className="team-grid">
        {teams.map((team) => (
          <div key={team.id} className="team-card">
            <h2 className="team-name">{team.name}</h2>
            <p className="team-details">{team.conference} — {team.division}</p>
            <p className="team-record">Record: {team.wins}-{team.losses}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
