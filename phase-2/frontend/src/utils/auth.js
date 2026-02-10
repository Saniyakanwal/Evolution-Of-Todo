// Utility functions for authentication
import { api, clearAuthToken, getUserId } from '../services/api';

// Check authentication status by making a backend API call
// This function will only return true if the backend confirms the user is authenticated

export const isAuthenticated = async () => {
  try {
    // Get user ID from memory
    const userId = getUserId();

    if (!userId) {
      console.log("Authentication check failed: Missing user ID in memory");
      return false;
    }

    console.log("Making API call to verify authentication...");
    const response = await api.getUserProfile(parseInt(userId));
    
    console.log("Authentication verification response:", !!response && !!response.id ? "Valid" : "Invalid");
    return !!response && !!response.id;
  } catch (error) {
    console.error('Authentication verification failed:', error);
    // Clear any stored tokens on failure
    clearAuthToken();
    return false;
  }
};

// Verify token validity with the backend
export const verifyToken = async () => {
  try {
    // This function now just calls isAuthenticated since they do the same thing
    return await isAuthenticated();
  } catch (error) {
    console.error('Token verification failed:', error);
    return false;
  }
};

export const logout = () => {
  clearAuthToken();
};