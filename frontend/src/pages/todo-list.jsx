"use client";

import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import TodoCard from "../components/TodoCard";
import FloatingActionButton from "../components/FloatingActionButton";
import ProtectedRoute from "../components/ProtectedRoute";
import { api } from "../services/api";

export default function TodoListPage() {
  const [todos, setTodos] = useState([]);
  const [filter, setFilter] = useState("all"); // all, active, completed
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await api.getTodos();
      setTodos(data);
    } catch (error) {
      console.error("Error fetching todos:", error);
      // More specific error message based on the error type
      let errorMessage = "Failed to load todos. ";
      if (error.message.includes("fetch failed") || error.message.includes("network")) {
        errorMessage = "Backend not running. Please start the server.";
      } else {
        errorMessage += error.message || "Please try again later.";
      }
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const toggleStatus = async (id) => {
    const todo = todos.find(t => t.id === id);
    if (!todo) return;

    try {
      const updatedStatus = todo.status === "pending" ? "completed" : "pending";
      const updatedTodo = await api.updateTodo(id, { ...todo, status: updatedStatus });

      setTodos(
        todos.map(t =>
          t.id === id
            ? { ...t, status: updatedTodo.status }
            : t
        )
      );
    } catch (error) {
      console.error("Error updating todo:", error);
      if (error.message.includes("fetch failed") || error.message.includes("network")) {
        setError("Backend not running. Please start the server.");
      } else {
        setError(error.message || "Failed to update todo.");
      }
    }
  };

  const deleteTodo = async (id) => {
    try {
      await api.deleteTodo(id);
      setTodos(todos.filter(t => t.id !== id));
    } catch (error) {
      console.error("Error deleting todo:", error);
      if (error.message.includes("fetch failed") || error.message.includes("network")) {
        setError("Backend not running. Please start the server.");
      } else {
        setError(error.message || "Failed to delete todo.");
      }
    }
  };

  // Filter todos based on selection
  const filteredTodos = todos.filter(todo => {
    if (filter === "active") return todo.status === "pending";
    if (filter === "completed") return todo.status === "completed";
    return true; // "all"
  });

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-gray-100">
        <Navbar />

        <main className="max-w-3xl mx-auto p-6">
          <div className="bg-white rounded-lg shadow-md p-6 mb-6">
            <h1 className="text-2xl font-bold text-gray-800 mb-4">My Tasks</h1>

            <div className="flex space-x-4 mb-6">
              <button
                onClick={() => setFilter("all")}
                className={`px-4 py-2 rounded ${
                  filter === "all"
                    ? "bg-purple-600 text-white"
                    : "bg-gray-200 text-gray-700 hover:bg-gray-300"
                }`}
              >
                All Tasks
              </button>
              <button
                onClick={() => setFilter("active")}
                className={`px-4 py-2 rounded ${
                  filter === "active"
                    ? "bg-purple-600 text-white"
                    : "bg-gray-200 text-gray-700 hover:bg-gray-300"
                }`}
              >
                Active
              </button>
              <button
                onClick={() => setFilter("completed")}
                className={`px-4 py-2 rounded ${
                  filter === "completed"
                    ? "bg-purple-600 text-white"
                    : "bg-gray-200 text-gray-700 hover:bg-gray-300"
                }`}
              >
                Completed
              </button>
            </div>

            {loading ? (
              <p className="text-center text-gray-500 py-8">Loading tasks...</p>
            ) : error ? (
              <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                {error}
              </div>
            ) : filteredTodos.length === 0 ? (
              <p className="text-center text-gray-500 py-8">
                {filter === "all"
                  ? "No tasks yet"
                  : filter === "active"
                    ? "No active tasks"
                    : "No completed tasks"}
              </p>
            ) : (
              <div className="space-y-4">
                {filteredTodos.map((todo) => (
                  <TodoCard
                    key={todo.id}
                    todo={todo}
                    toggleStatus={toggleStatus}
                    onDelete={deleteTodo}
                  />
                ))}
              </div>
            )}
          </div>
        </main>

        <FloatingActionButton />
      </div>
    </ProtectedRoute>
  );
}