"use client";

import type React from "react";

import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Plus, Search } from "lucide-react";
import { Textarea } from "@/components/ui/textarea";
import { createBooks, getAllBooks } from "@/lib/api";

type Book = {
  isbn: string;
  title: string;
  author: string;
  publicationYear: number;
  id_loan: number;
};

const mockBooks: Book[] = [
  {
    isbn: "978-0-7475-3269-9",
    title: "Harry Potter and the Philosopher's Stone",
    author: "J.K. Rowling",
    publicationYear: 1997,
    category: "Fantasy",
    status: "Available",
    copies: 5,
  },
  {
    isbn: "978-0-06-112008-4",
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    publicationYear: 1937,
    category: "Fantasy",
    status: "Loaned",
    copies: 3,
  },
];

export function BooksTab() {
  const [books, setBooks] = useState<Book[]>([]);
  useEffect(() => {
    const run = async () => {
      let bd_books = await getAllBooks();

      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      bd_books = bd_books.map((book: any) => ({
        title: book.titulo,
        publisher: book.editora,
        isbn: book.isbn,
        publicationYear: book.ano_publicacao,
        author: book.autor,
        id_loan: book.id_loan,
      }));

      setBooks(bd_books);
    };
    run();
  }, []);

  const [searchTerm, setSearchTerm] = useState("");
  const [showBulkAdd, setShowBulkAdd] = useState(false);

  const filteredBooks = books.filter(
    (book) =>
      book.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      book.author.toLowerCase().includes(searchTerm.toLowerCase()) ||
      book.isbn.includes(searchTerm)
  );

  const handleBulkAdd = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = event.currentTarget as HTMLFormElement;
    const formData = new FormData(form);
    const booksData = formData.get("books") as string;

    const newBooks = booksData
      .split("\n")
      .map((line) => {
        const parts = line.split(",").map((part) => part.trim());
        if (parts.length < 5) return null; // Ignorar linhas inválidas

        const [isbn, title, author, publicationYear, publisher] = parts;

        return {
          titulo: title,
          editora: publisher,
          isbn: isbn,
          ano_publicacao: `${Number.parseInt(publicationYear)}`,
          autor: author,
        };
      })
      .filter(Boolean); // Remove entradas inválidas

    if (newBooks.length > 0) {
      console.log(newBooks);
      createBooks(newBooks);
    }
  };

  const handleAdd = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = event.currentTarget as HTMLFormElement;
    const formData = new FormData(form);

    const isbn = formData.get("isbn");
    const title = formData.get("title");
    const author = formData.get("author");
    const publicationYear = formData.get("publicationYear");
    const publisher = formData.get("publisher");

    createBooks([
      {
        titulo: title,
        editora: publisher,
        isbn: isbn,
        ano_publicacao: publicationYear,
        autor: author,
      },
    ]);
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div className="relative w-72">
          <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
          <Input
            placeholder="Search books..."
            className="pl-8"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
        <div className="flex gap-2">
          <Dialog>
            <DialogTrigger asChild>
              <Button>
                <Plus className="mr-2 h-4 w-4" />
                Add Book
              </Button>
            </DialogTrigger>
            <DialogContent>
              <DialogHeader>
                <DialogTitle>Add New Book</DialogTitle>
                <DialogDescription>
                  Enter the book details below. All fields are required.
                </DialogDescription>
              </DialogHeader>
              <form onSubmit={handleAdd} className="grid gap-4 py-4">
                <div className="grid grid-cols-2 gap-4">
                  <div className="grid gap-2">
                    <Label htmlFor="isbn">ISBN</Label>
                    <Input
                      id="isbn"
                      name="isbn"
                      placeholder="978-0-7475-3269-9"
                      required
                    />
                  </div>
                  <div className="grid gap-2">
                    <Label htmlFor="title">Title</Label>
                    <Input id="title" name="title" required />
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div className="grid gap-2">
                    <Label htmlFor="author">Author</Label>
                    <Input id="author" name="author" required />
                  </div>
                  <div className="grid gap-2">
                    <Label htmlFor="publicationYear">Publication Year</Label>
                    <Input
                      id="publicationYear"
                      name="publicationYear"
                      type="number"
                      required
                    />
                  </div>
                </div>
                <div className="">
                  <div className="">
                    <Label htmlFor="publisher">publisher</Label>
                    <Input id="publisher" name="publisher" required />
                  </div>
                </div>
                <Button type="submit">Save Book</Button>
              </form>
            </DialogContent>
          </Dialog>
          <Button variant="outline" onClick={() => setShowBulkAdd(true)}>
            Bulk Add Books
          </Button>
        </div>
      </div>

      {showBulkAdd && (
        <Dialog open={showBulkAdd} onOpenChange={setShowBulkAdd}>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>Bulk Add Books</DialogTitle>
              <DialogDescription>
                Enter book details in CSV format: ISBN, Title, Author,
                Publication Year, Category, Copies One book per line.
              </DialogDescription>
            </DialogHeader>
            <form onSubmit={handleBulkAdd} className="space-y-4">
              <Textarea
                name="books"
                placeholder="978-0-7475-3269-9, Harry Potter, J.K. Rowling, 1997, Fantasy, 5"
                rows={10}
                required
              />
              <Button type="submit">Add Books</Button>
            </form>
          </DialogContent>
        </Dialog>
      )}

      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>ISBN</TableHead>
              <TableHead>Title</TableHead>
              <TableHead>Author</TableHead>
              <TableHead>Publication Year</TableHead>
              <TableHead>Category</TableHead>
              <TableHead>Action</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filteredBooks.map((book, i) => (
              <TableRow key={book.isbn + i}>
                <TableCell>{book.isbn}</TableCell>
                <TableCell>{book.title}</TableCell>
                <TableCell>{book.author}</TableCell>
                <TableCell>{book.publicationYear}</TableCell>
                <TableCell>
                  <span
                    className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${
                      book.id_loan
                        ? "bg-green-100 text-green-800"
                        : "bg-yellow-100 text-yellow-800"
                    }`}
                  >
                    {book.id_loan ? "Loaned" : "Available"}
                  </span>
                </TableCell>
                <TableCell>
                  <Button variant="ghost" size="sm">
                    Edit
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
}
