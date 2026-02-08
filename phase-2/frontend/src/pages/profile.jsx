import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import Navbar from "../components/Navbar";
import ProtectedRoute from "../components/ProtectedRoute";
import { api, getUserId } from "../services/api";

export default function ProfilePage() {
  const router = useRouter();
  const [user, setUser] = useState({
    username: "",
    email: "",
    full_name: "",
    bio: "",
    avatar_url: ""
  });
  const [isEditing, setIsEditing] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Load user profile data from backend
    fetchUserProfile();
  }, []);

  const fetchUserProfile = async () => {
    try {
      const userId = getUserId();
      if (!userId) {
        router.push("/login");
        return;
      }

      const userData = await api.getUserProfile(parseInt(userId));
      setUser(userData);
      setLoading(false);
    } catch (err) {
      if (err.message.includes("fetch failed") || err.message.includes("network")) {
        setError("Backend not running. Please start the server.");
      } else {
        setError(err.message || "Failed to load profile. Please try again.");
      }
      console.error("Profile fetch error:", err);
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUser(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userId = getUserId();

    try {
      // Update profile data on backend
      const updatedUser = await api.updateUserProfile(parseInt(userId), user);
      setUser(updatedUser);
      setIsEditing(false);
      alert("Profile updated successfully!");
    } catch (err) {
      if (err.message.includes("fetch failed") || err.message.includes("network")) {
        setError("Backend not running. Please start the server.");
      } else {
        setError(err.message || "Failed to update profile. Please try again.");
      }
      console.error("Profile update error:", err);
    }
  };

  if (loading) {
    return (
      <ProtectedRoute>
        <div className="min-h-screen bg-gray-100 flex items-center justify-center">
          <div className="text-xl">Loading profile...</div>
        </div>
      </ProtectedRoute>
    );
  }

  if (error) {
    return (
      <ProtectedRoute>
        <div className="min-h-screen bg-gray-100 flex items-center justify-center">
          <div className="text-xl text-red-500">{error}</div>
        </div>
      </ProtectedRoute>
    );
  }

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-gray-100">
        <Navbar />

        <main className="max-w-3xl mx-auto p-6">
          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="flex justify-between items-center mb-6">
              <h1 className="text-2xl font-bold text-gray-800">User Profile</h1>
              {!isEditing && (
                <button
                  onClick={() => setIsEditing(true)}
                  className="bg-purple-600 text-white px-4 py-2 rounded hover:bg-purple-700 transition"
                >
                  Edit Profile
                </button>
              )}
            </div>

            {isEditing ? (
              <form onSubmit={handleSubmit}>
                <div className="space-y-4">
                  <div>
                    <label htmlFor="username" className="block text-sm font-medium text-gray-700 mb-1">
                      Username
                    </label>
                    <input
                      type="text"
                      id="username"
                      name="username"
                      value={user.username}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                      placeholder="Enter your username"
                    />
                  </div>

                  <div>
                    <label htmlFor="full_name" className="block text-sm font-medium text-gray-700 mb-1">
                      Full Name
                    </label>
                    <input
                      type="text"
                      id="full_name"
                      name="full_name"
                      value={user.full_name}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                      placeholder="Enter your full name"
                    />
                  </div>

                  <div>
                    <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
                      Email
                    </label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={user.email}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                      placeholder="Enter your email"
                    />
                  </div>

                  <div>
                    <label htmlFor="bio" className="block text-sm font-medium text-gray-700 mb-1">
                      Bio
                    </label>
                    <textarea
                      id="bio"
                      name="bio"
                      value={user.bio}
                      onChange={handleInputChange}
                      rows="4"
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                      placeholder="Tell us about yourself"
                    ></textarea>
                  </div>

                  <div>
                    <label htmlFor="avatar_url" className="block text-sm font-medium text-gray-700 mb-1">
                      Avatar URL
                    </label>
                    <input
                      type="text"
                      id="avatar_url"
                      name="avatar_url"
                      value={user.avatar_url}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                      placeholder="Enter URL to your avatar image"
                    />
                  </div>

                  <div className="flex space-x-3 pt-4">
                    <button
                      type="submit"
                      className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition"
                    >
                      Save Changes
                    </button>
                    <button
                      type="button"
                      onClick={() => setIsEditing(false)}
                      className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600 transition"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              </form>
            ) : (
              <div className="space-y-6">
                <div className="flex items-center space-x-6">
                  {user.avatar_url ? (
                    <img
                      src={user.avatar_url}
                      alt="User avatar"
                      className="w-24 h-24 rounded-full object-cover border-4 border-purple-200"
                    />
                  ) : (
                    <div className="w-24 h-24 rounded-full bg-purple-200 flex items-center justify-center text-purple-800 text-3xl">
                      {user.username ? user.username.charAt(0).toUpperCase() : '?'}
                    </div>
                  )}
                  <div>
                    <h2 className="text-xl font-semibold text-gray-800">{user.username || "New User"}</h2>
                    <p className="text-gray-600">{user.email || "Email not provided"}</p>
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <h3 className="text-sm font-medium text-gray-500">Full Name</h3>
                    <p className="mt-1 text-gray-800">
                      {user.full_name || "Not provided"}
                    </p>
                  </div>

                  <div>
                    <h3 className="text-sm font-medium text-gray-500">Bio</h3>
                    <p className="mt-1 text-gray-800">
                      {user.bio || "No bio provided yet. Click 'Edit Profile' to add one."}
                    </p>
                  </div>
                </div>
              </div>
            )}
          </div>
        </main>
      </div>
    </ProtectedRoute>
  );
}