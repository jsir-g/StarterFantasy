import { useState } from 'react';

export default function CreateLeague() {
  const [leagueName, setLeagueName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`League "${leagueName}" created!`);
    // Later: POST to Flask backend
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold mb-4">Create a New League</h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4 max-w-md mx-auto">
        <input
          type="text"
          value={leagueName}
          onChange={(e) => setLeagueName(e.target.value)}
          placeholder="Enter league name"
          className="border p-2 rounded"
          required
        />
        <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded">
          Create League
        </button>
      </form>
    </div>
  );
}
