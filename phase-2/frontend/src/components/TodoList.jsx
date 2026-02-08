import TodoCard from "./TodoCard";

export default function TodoList({ todos, toggleStatus }) {
  if (todos.length === 0) {
    return (
      <p className="text-center text-gray-400">
        No tasks yet 👈
      </p>
    );
  }

  return (
    <div className="space-y-4">
      {todos.map((todo) => (
        <TodoCard
          key={todo.id}
          todo={todo}
          toggleStatus={toggleStatus}
        />
      ))}
    </div>
  );
}
