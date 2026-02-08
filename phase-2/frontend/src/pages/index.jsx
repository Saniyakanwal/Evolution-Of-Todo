import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import Link from "next/link";
import { isAuthenticated, verifyToken } from "../utils/auth";
import Navbar from "../components/Navbar";

export default function Home() {
  const router = useRouter();
  const [checkingAuth, setCheckingAuth] = useState(true);
  const [isAuthenticatedUser, setIsAuthenticatedUser] = useState(false);

  useEffect(() => {
    // Check authentication status by calling backend
    const checkAuth = async () => {
      try {
        const isValid = await isAuthenticated();
        setIsAuthenticatedUser(isValid);
      } catch (error) {
        console.error("Error checking authentication status:", error);
        // If backend is unreachable, treat as not authenticated
        setIsAuthenticatedUser(false);
      } finally {
        setCheckingAuth(false);
      }
    };

    checkAuth();
  }, []);

  // Show a simple loading indicator while checking auth status
  if (checkingAuth) {
    return (
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        fontSize: '18px',
        fontWeight: 'bold'
      }}>
        Loading...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <main className="max-w-3xl mx-auto p-6">
        <div className="bg-white rounded-lg shadow-md p-6">
          <h1 className="text-2xl font-bold text-gray-800 mb-4">Welcome to TodoApp</h1>
          <p className="text-gray-600 mb-6">
            {isAuthenticatedUser 
              ? "You are logged in! Click on 'My Tasks' to manage your todos."
              : "Please sign up or log in to start managing your tasks."}
          </p>
          
          <div className="flex space-x-4">
            {!isAuthenticatedUser && (
              <>
                <Link 
                  href="/signup" 
                  className="bg-purple-600 text-white px-4 py-2 rounded-md hover:bg-purple-700 transition"
                >
                  Sign Up
                </Link>
                <Link 
                  href="/login" 
                  className="bg-gray-600 text-white px-4 py-2 rounded-md hover:bg-gray-700 transition"
                >
                  Log In
                </Link>
              </>
            )}
            {isAuthenticatedUser && (
              <Link 
                href="/todo-list" 
                className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 transition"
              >
                View My Tasks
              </Link>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
