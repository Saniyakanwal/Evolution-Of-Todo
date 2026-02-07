export default function Button({ children, onClick, variant = "primary", type = "button", className = "" }) {
  const baseClasses = "px-4 py-2 rounded transition";
  
  const variants = {
    primary: "bg-purple-600 hover:bg-purple-700 text-white",
    secondary: "bg-gray-500 hover:bg-gray-600 text-white",
    danger: "bg-red-500 hover:bg-red-600 text-white",
    success: "bg-green-500 hover:bg-green-600 text-white"
  };
  
  const classes = `${baseClasses} ${variants[variant]} ${className}`;
  
  return (
    <button 
      type={type}
      onClick={onClick}
      className={classes}
    >
      {children}
    </button>
  );
}
