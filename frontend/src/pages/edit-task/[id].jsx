import { useState, useEffect } from 'react';
import Navbar from '../../components/Navbar';
import Button from '../../components/Button';
import { api } from '../../services/api';
import { useRouter } from 'next/router';

const EditTaskPage = () => {
  const router = useRouter();
  const { id } = router.query;
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [status, setStatus] = useState('pending');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    if (id) {
      fetchTask();
    }
  }, [id]);

  const fetchTask = async () => {
    try {
      setLoading(true);
      const task = await api.getTodoById(parseInt(id));
      setTitle(task.title);
      setDescription(task.description);
      setStatus(task.status);
    } catch (err) {
      if (err.message.includes("fetch failed") || err.message.includes("network")) {
        setError("Backend not running. Please start the server.");
      } else {
        setError(err.message || 'Failed to load task.');
      }
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!title.trim()) {
      setError('Title is required');
      return;
    }

    try {
      await api.updateTodo(parseInt(id), { title, description, status });
      router.push('/todo-list');
    } catch (err) {
      if (err.message.includes("fetch failed") || err.message.includes("network")) {
        setError("Backend not running. Please start the server.");
      } else {
        setError(err.message || 'Failed to update task.');
      }
      console.error(err);
    }
  };

  if (loading) return <div className="text-center py-10">Loading...</div>;

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <div className="container mx-auto py-8 px-4 max-w-2xl">
        <h1 className="text-3xl font-bold text-gray-800 mb-6">Edit Task</h1>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md">
          <div className="mb-4">
            <label htmlFor="title" className="block text-gray-700 font-medium mb-2">
              Title *
            </label>
            <input
              type="text"
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter task title"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="description" className="block text-gray-700 font-medium mb-2">
              Description
            </label>
            <textarea
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              rows="4"
              placeholder="Enter task description (optional)"
            ></textarea>
          </div>

          <div className="mb-6">
            <label className="block text-gray-700 font-medium mb-2">
              Status
            </label>
            <div className="flex space-x-4">
              <label className="inline-flex items-center">
                <input
                  type="radio"
                  checked={status === 'pending'}
                  onChange={() => setStatus('pending')}
                  className="form-radio h-4 w-4 text-blue-600"
                />
                <span className="ml-2">Pending</span>
              </label>
              <label className="inline-flex items-center">
                <input
                  type="radio"
                  checked={status === 'completed'}
                  onChange={() => setStatus('completed')}
                  className="form-radio h-4 w-4 text-blue-600"
                />
                <span className="ml-2">Completed</span>
              </label>
            </div>
          </div>

          <div className="flex justify-end space-x-3">
            <Button
              variant="secondary"
              onClick={() => router.push('/todo-list')}
            >
              Cancel
            </Button>
            <Button type="submit" variant="primary">
              Update Task
            </Button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default EditTaskPage;