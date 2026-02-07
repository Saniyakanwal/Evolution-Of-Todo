import { useState } from "react";
import { useRouter } from "next/router";
import { api } from "../services/api";

export default function TodoModal({ isOpen, onClose, addTodo }) {
  const router = useRouter();
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!title.trim()) {
      setError("Task title is required");
      return;
    }
    
    setLoading(true);
    setError("");
    
    try {
      const newTodo = await api.createTodo({
        title: title,
        description: description,
        status: "pending"
      });
      
      if (addTodo) {
        addTodo(newTodo);
      }
      
      setTitle("");
      setDescription("");
      onClose();
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
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg shadow-xl w-full max-w-md">
        <div className="p-6">
          <h2 className="text-xl font-bold text-gray-800 mb-4">Add New Task</h2>
          
          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
              {error}
            </div>
          )}
          
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label htmlFor="title" className="block text-gray-700 mb-2">
                Task Title *
              </label>
              <input
                type="text"
                id="title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                placeholder="What needs to be done?"
                disabled={loading}
              />
            </div>
            
            <div className="mb-4">
              <label htmlFor="description" className="block text-gray-700 mb-2">
                Description
              </label>
              <textarea
                id="description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                rows="3"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                placeholder="Add details about this task..."
                disabled={loading}
              />
            </div>
            
            <div className="flex justify-end space-x-3">
              <button
                type="button"
                onClick={onClose}
                className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded"
                disabled={loading}
              >
                Cancel
              </button>
              <button
                type="submit"
                className="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded"
                disabled={loading}
              >
                {loading ? "Creating..." : "Add Task"}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
