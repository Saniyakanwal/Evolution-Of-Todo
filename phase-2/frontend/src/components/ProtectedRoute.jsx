import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import { isAuthenticated, verifyToken } from '../utils/auth';

const ProtectedRoute = ({ children }) => {
  const router = useRouter();
  const [checkingAuth, setCheckingAuth] = useState(true);
  const [isAuthorized, setIsAuthorized] = useState(false);
  const [authError, setAuthError] = useState(null);

  useEffect(() => {
    // Check if we're in the browser (not during SSR)
    if (typeof window !== 'undefined') {
      // Check authentication status by calling backend
      const checkAuth = async () => {
        try {
          const isValid = await isAuthenticated();
          if (!isValid) {
            // Either no token stored or token is invalid, redirect to login
            router.push('/login');
          } else {
            setIsAuthorized(true);
          }
        } catch (error) {
          console.error('Error verifying authentication:', error);
          // Show error instead of redirecting silently if backend is unreachable
          setAuthError(error.message || 'Unable to verify authentication. Please check if the backend is running.');
        } finally {
          setCheckingAuth(false);
        }
      };

      // Delay the auth check until after mount to prevent SSR issues
      const timer = setTimeout(checkAuth, 0);
      return () => clearTimeout(timer);
    }
  }, [router]);

  // If still checking auth status, show loading
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
        Checking authentication...
      </div>
    );
  }

  // If there's an auth error (backend unreachable), show error message
  if (authError) {
    console.log("Auth error occurred:", authError);
    return (
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="bg-white p-8 rounded-lg shadow-md max-w-md w-full mx-4">
          <h2 className="text-xl font-bold text-red-600 mb-4">Backend Not Running</h2>
          <p className="text-gray-700 mb-6">Backend not running. Please start the server.</p>
          <button
            onClick={() => router.push('/login')}
            className="w-full bg-purple-600 text-white py-2 rounded-md hover:bg-purple-700 transition"
          >
            Return to Login
          </button>
        </div>
      </div>
    );
  }

  // If not authenticated or token is invalid, don't render children
  if (!isAuthorized) {
    console.log("Access denied - user not authenticated or token invalid");
    return null; // Will be redirected by useEffect
  }

  console.log("Access granted - user authenticated and authorized");
  return children;
};

export default ProtectedRoute;