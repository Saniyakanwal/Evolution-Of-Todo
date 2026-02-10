// Ensure API_BASE_URL doesn't end with a slash to prevent double slashes in URLs
let API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://127.0.0.1:8000/api/v1';
API_BASE_URL = API_BASE_URL.trim(); // Remove leading/trailing whitespace
// Remove all trailing slashes
while (API_BASE_URL.endsWith('/')) {
  API_BASE_URL = API_BASE_URL.slice(0, -1);
}

// Memory storage for authentication data
let authToken = null;
let userId = null;
let username = null;

// Helper function to set auth data in memory
export const setAuthData = (token, id, name) => {
  authToken = token;
  userId = id;
  username = name;
};

// Helper function to get token from memory
const getToken = () => {
  return authToken;
};

// Helper function to get user ID from memory
export const getUserId = () => {
  return userId;
};

// Helper function to get username from memory
export const getUsername = () => {
  return username;
};

// Helper function to clear all auth data from memory
export const clearAuthToken = () => {
  authToken = null;
  userId = null;
  username = null;
};

// Helper function to add auth header to requests
const getAuthHeaders = () => {
  const token = getToken();
  return {
    'Content-Type': 'application/json',
    ...(token && { 'Authorization': `Bearer ${token}` })
  };
};

export const api = {
  // Authentication methods
  login: async (email, password) => {
    const response = await fetch(`${API_BASE_URL}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email,
        password
      })
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Login failed');
    }

    const result = await response.json();
    // Store auth data in memory
    setAuthData(result.access_token, result.user_id, result.username);
    return result;
  },

  signup: async (userData) => {
    const response = await fetch(`${API_BASE_URL}/users`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Signup failed');
    }

    const result = await response.json();
    // Store auth data in memory
    setAuthData(result.access_token, result.user_id, result.username);
    return result;
  },

  getUserProfile: async (id) => {
    const response = await fetch(`${API_BASE_URL}/users/${id}`, {
      headers: getAuthHeaders(),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to fetch user profile');
    }

    return await response.json();
  },

  updateUserProfile: async (id, userData) => {
    const response = await fetch(`${API_BASE_URL}/users/${id}`, {
      method: 'PATCH',
      headers: getAuthHeaders(),
      body: JSON.stringify(userData),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to update user profile');
    }

    return await response.json();
  },

  // Get all todos
  getTodos: async () => {
    const response = await fetch(`${API_BASE_URL}/todos`, {
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to fetch todos');
    }
    return await response.json();
  },

  // Get single todo
  getTodoById: async (id) => {
    const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to fetch todo');
    }
    return await response.json();
  },

  // Create a new todo
  createTodo: async (todoData) => {
    const response = await fetch(`${API_BASE_URL}/todos`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify(todoData),
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to create todo');
    }
    return await response.json();
  },

  // Update a todo
  updateTodo: async (id, todoData) => {
    const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
      method: 'PATCH',
      headers: getAuthHeaders(),
      body: JSON.stringify(todoData),
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to update todo');
    }
    return await response.json();
  },

  // Delete a todo
  deleteTodo: async (id) => {
    const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
      method: 'DELETE',
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Failed to delete todo');
    }
    return await response.json();
  },
};
