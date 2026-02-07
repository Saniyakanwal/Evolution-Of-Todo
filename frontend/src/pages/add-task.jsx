import { useState } from "react";
import { useRouter } from "next/router";
import Navbar from "../components/Navbar";
import ProtectedRoute from "../components/ProtectedRoute";
import { api } from "../services/api";

export default function AddTaskPage() {
  const router = useRouter();
  const [taskTitle, setTaskTitle] = useState("");
  const [taskDescription, setTaskDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!taskTitle.trim()) {
      setError("Task title is required");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const newTodo = await api.createTodo({
        title: taskTitle,
        description: taskDescription,
        status: "pending"
      });

      setTaskTitle("");
      setTaskDescription("");
      // Optionally, we can redirect to the todo list or stay on the page
      router.push("/todo-list");
    } catch (err) {
      if (err.message.includes("fetch failed") || err.message.includes("network")) {
        setError("Backend not running. Please start the server.");
      } else {
        setError(err.message || "Failed to create task.");
      }
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-gray-100">
        <Navbar />

        <main className="max-w-3xl mx-auto p-6">
          <div className="bg-white rounded-lg shadow-md p-6">
            <h1 className="text-2xl font-bold text-gray-800 mb-6">Add New Task</h1>

            {error && (
              <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                {error}
              </div>
            )}

            <form onSubmit={handleSubmit}>
              <div className="mb-4">
                <label htmlFor="taskTitle" className="block text-gray-700 mb-2">
                  Task Title
                </label>
                <input
                  type="text"
                  id="taskTitle"
                  value={taskTitle}
                  onChange={(e) => setTaskTitle(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                  placeholder="What needs to be done?"
                  disabled={loading}
                />
              </div>

              <div className="mb-4">
                <label htmlFor="taskDescription" className="block text-gray-700 mb-2">
                  Description (optional)
                </label>
                <textarea
                  id="taskDescription"
                  value={taskDescription}
                  onChange={(e) => setTaskDescription(e.target.value)}
                  rows="3"
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                  placeholder="Add details about this task..."
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
                {loading ? "Creating..." : "Create Task"}
              </button>
            </form>
          </div>
        </main>
      </div>
    </ProtectedRoute>
  );
}