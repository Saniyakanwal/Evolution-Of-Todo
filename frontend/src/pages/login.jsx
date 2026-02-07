import { useState } from "react";
import { useRouter } from "next/router";
import Link from "next/link";
import Navbar from "../components/Navbar";
import { api } from "../services/api";

export default function LoginPage() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    email: "",
    password: ""
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Simple validation
    if (!formData.email || !formData.password) {
      setError("Please fill in all fields");
      return;
    }

    setLoading(true);
    setError("");

    try {
      // Call the backend API for login
      const response = await api.login(formData.email, formData.password);

      // Token and user info are now stored in memory by the API service
      console.log("Login successful, token stored in memory:", response.access_token);
      console.log("User ID stored in memory:", response.user_id);
      console.log("Username stored in memory:", response.username);
      
      router.push("/todo-list");
    } catch (err) {
      console.error("Login error:", err);
      if (err.message.includes("fetch failed") || err.message.includes("network")) {
        setError("Backend not running. Please start the server.");
      } else {
        setError(err.message || "Login failed. Please check your credentials.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <Navbar />
      
      <div className="flex items-center justify-center flex-grow">
        <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
          <h1 className="text-2xl font-bold text-center text-gray-800 mb-6">Login</h1>
          
          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
              {error}
            </div>
          )}
          
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label htmlFor="email" className="block text-gray-700 mb-2">
                Email
              </label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                placeholder="Enter your email"
                disabled={loading}
              />
            </div>
            
            <div className="mb-6">
              <label htmlFor="password" className="block text-gray-700 mb-2">
                Password
              </label>
              <input
                type="password"
                id="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                placeholder="Enter your password"
                disabled={loading}
              />
            </div>
            
            <button
              type="submit"
              disabled={loading}
              className={`w-full bg-purple-600 text-white py-2 rounded-md hover:bg-purple-700 transition ${
                loading ? "opacity-50 cursor-not-allowed" : ""
              }`}
            >
              {loading ? "Logging in..." : "Login"}
            </button>
          </form>
          
          <div className="mt-4 text-center">
            <p className="text-gray-600">
              Don't have an account?{" "}
              <Link href="/signup" className="text-purple-600 hover:underline">
                Sign up
              </Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}