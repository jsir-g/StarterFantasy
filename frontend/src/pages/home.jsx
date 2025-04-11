import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="p-6 text-center">
      <h1 className="text-3xl font-bold mb-4">Welcome to Starter Fantasy</h1>
      <p className="mb-6">Create your own fantasy league and compete weekly!</p>
      <Link to="/create" className="bg-blue-600 text-white px-4 py-2 rounded">
        Get Started
      </Link>
    </div>
  );
}
