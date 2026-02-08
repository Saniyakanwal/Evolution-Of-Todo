import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/router";
import { verifyToken } from "../utils/auth";
import { getUsername, clearAuthToken } from "../services/api";

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState("");
  const router = useRouter();

  useEffect(() => {
    // Check if user is logged in by verifying with backend
    const checkAuthStatus = async () => {
      console.log("Checking auth status in Navbar...");
      try {
        const isValid = await verifyToken();
        console.log("Token verification result:", isValid ? "Valid" : "Invalid");
        
        if (isValid) {
          // Get username from memory since we verified the token is valid
          const storedUsername = getUsername();
          setIsLoggedIn(true);
          if (storedUsername) {
            setUsername(storedUsername);
            console.log("Set username to:", storedUsername);
          }
        } else {
          // If token is invalid, clear it
          console.log("Clearing invalid token from memory");
          clearAuthToken();
          setIsLoggedIn(false);
          setUsername("");
        }
      } catch (error) {
        console.error("Error verifying token in navbar:", error);
        // If backend is unreachable, treat as not logged in
        clearAuthToken();
        setIsLoggedIn(false);
        setUsername("");
      }
    };

    checkAuthStatus();
  }, [router.pathname]); // Re-run when route changes

  const handleLogout = () => {
    console.log("Initiating logout process");
    clearAuthToken();
    console.log("Cleared auth tokens from memory");
    setIsLoggedIn(false);
    setUsername("");
    console.log("Updated auth state to logged out");
    router.push("/login");
  };

  return (
    <nav className="bg-purple-700 text-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          {/* Logo / App Name */}
          <div className="flex-shrink-0 text-2xl font-bold text-yellow-300">
            🌟 TodoApp
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex space-x-6 items-center">
            <Link href="/" className="hover:text-yellow-300 transition">
              Home
            </Link>
            <Link href="/todo-list" className="hover:text-yellow-300 transition">
              My Tasks
            </Link>
            
            {isLoggedIn ? (
              <>
                <span className="text-sm">Welcome, {username}!</span>
                <Link href="/profile" className="hover:text-yellow-300 transition">
                  Profile
                </Link>
                <button 
                  onClick={handleLogout}
                  className="hover:text-yellow-300 transition"
                >
                  Logout
                </button>
              </>
            ) : (
              <>
                <Link href="/signup" className="hover:text-yellow-300 transition">
                  Sign Up
                </Link>
                <Link href="/login" className="hover:text-yellow-300 transition">
                  Login
                </Link>
              </>
            )}
          </div>

          {/* Mobile Menu Button */}
          <div className="md:hidden flex items-center">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="focus:outline-none text-white"
            >
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                {isOpen ? (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M6 18L18 6M6 6l12 12"
                  />
                ) : (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                )}
              </svg>
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden px-2 pt-2 pb-4 space-y-1 bg-purple-600">
          <Link href="/" className="block px-3 py-2 rounded hover:bg-purple-500 transition">
            Home
          </Link>
          <Link href="/todo-list" className="block px-3 py-2 rounded hover:bg-purple-500 transition">
            My Tasks
          </Link>
          
          {isLoggedIn ? (
            <>
              <span className="block px-3 py-2 rounded">Welcome, {username}!</span>
              <Link href="/profile" className="block px-3 py-2 rounded hover:bg-purple-500 transition">
                Profile
              </Link>
              <button 
                onClick={handleLogout}
                className="block w-full text-left px-3 py-2 rounded hover:bg-purple-500 transition"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <Link href="/signup" className="block px-3 py-2 rounded hover:bg-purple-500 transition">
                Sign Up
              </Link>
              <Link href="/login" className="block px-3 py-2 rounded hover:bg-purple-500 transition">
                Login
              </Link>
            </>
          )}
        </div>
      )}
    </nav>
  );
}
