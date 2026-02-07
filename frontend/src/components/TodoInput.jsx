import { useState } from "react";
import TodoModal from "./TodoModel";
import Link from "next/link";

export default function TodoInput({ addTodo }) {
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <div className="bg-white p-5 rounded-xl shadow space-y-3">
      <div className="flex justify-between items-center">
        <h2 className="text-lg font-semibold text-gray-800">Add New Task</h2>
        <div className="flex space-x-2">
          <button
            onClick={() => setIsModalOpen(true)}
            className="bg-purple-600 text-white px-4 py-2 rounded"
          >
            Quick Add
          </button>
          <Link href="/add-task">
            <button className="bg-blue-600 text-white px-4 py-2 rounded">
              Detailed Form
            </button>
          </Link>
        </div>
      </div>
      
      <TodoModal 
        isOpen={isModalOpen} 
        onClose={() => setIsModalOpen(false)} 
        addTodo={addTodo} 
      />
    </div>
  );
}
