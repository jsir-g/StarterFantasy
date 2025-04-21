export default function Standings() {
    const dummyData = [
      { name: 'You', wins: 3, losses: 1 },
      { name: 'CPU Team 1', wins: 2, losses: 2 },
      { name: 'CPU Team 2', wins: 1, losses: 3 },
    ];
  
    return (
      <div className="p-6">
        <h2 className="text-2xl font-semibold mb-4">League Standings</h2>
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-gray-200">
              <th className="p-2 border">Team</th>
              <th className="p-2 border">Wins</th>
              <th className="p-2 border">Losses</th>
            </tr>
          </thead>
          <tbody>
            {dummyData.map((team, index) => (
              <tr key={index}>
                <td className="p-2 border">{team.name}</td>
                <td className="p-2 border">{team.wins}</td>
                <td className="p-2 border">{team.losses}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
  