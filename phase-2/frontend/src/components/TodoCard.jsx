import Link from "next/link";

export default function TodoCard({ todo, toggleStatus, onDelete }) {
  const isCompleted = todo.status === "completed";

  return (
    <div className={`p-4 bg-white rounded-xl shadow flex justify-between ${isCompleted ? 'opacity-70' : ''}`}>
      <div>
        <div className="flex items-start">
          <input
            type="checkbox"
            checked={isCompleted}
            onChange={() => toggleStatus(todo.id)}
            className="mt-1 mr-3 h-5 w-5 text-purple-600 rounded focus:ring-purple-500"
          />
          <div>
            <h3 className={`font-semibold text-lg ${isCompleted ? 'line-through text-gray-500' : 'text-gray-800'}`}>
              {todo.title}
            </h3>
            <p className="text-gray-500 text-sm">{todo.description}</p>

            <span
              className={`inline-block mt-2 px-2 py-1 text-xs font-medium rounded-full ${
                isCompleted ? "bg-green-100 text-green-800" : "bg-yellow-100 text-yellow-800"
              }`}
            >
              {isCompleted ? "Completed" : "Pending"}
            </span>
          </div>
        </div>
      </div>

      <div className="flex space-x-2">
        <Link href={`/edit-task/${todo.id}`}>
          <button className="text-blue-600 font-semibold">
            Edit
          </button>
        </Link>
        
        {onDelete && (
          <button
            onClick={() => onDelete(todo.id)}
            className="text-red-600 font-semibold"
          >
            Delete
          </button>
        )}
      </div>
    </div>
  );
}
