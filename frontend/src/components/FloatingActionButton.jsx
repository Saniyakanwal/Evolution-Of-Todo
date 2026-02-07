import Link from "next/link";

export default function FloatingActionButton() {
  return (
    <Link href="/add-task">
      <button className="fixed bottom-8 right-8 bg-purple-600 hover:bg-purple-700 text-white w-14 h-14 rounded-full text-3xl shadow-lg transition flex items-center justify-center">
        +
      </button>
    </Link>
  );
}