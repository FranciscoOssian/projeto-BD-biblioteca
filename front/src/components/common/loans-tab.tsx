"use client";

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
import { createLoan, getAllBooks, getAllLoans } from "@/lib/api";

type Loan = {
  id: string;
  bookTitle: string;
  readerName: string;
  checkoutDate: string;
  dueDate: string;
  status: "Active" | "Returned" | "Overdue";
};

const mockLoans: Loan[] = [
  {
    id: "L001",
    bookTitle: "Harry Potter and the Philosopher's Stone",
    readerName: "John Doe",
    checkoutDate: "2024-02-01",
    dueDate: "2024-02-15",
    status: "Active",
  },
  {
    id: "L002",
    bookTitle: "The Hobbit",
    readerName: "Jane Smith",
    checkoutDate: "2024-01-15",
    dueDate: "2024-01-29",
    status: "Returned",
  },
];

export function LoansTab() {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const [loans, setLoans] = useState<any[]>([]);
  useEffect(() => {
    const run = async () => {
      let bd_loans = await getAllLoans();
      let bd_books = await getAllBooks();

      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      bd_books = bd_books.map((book: any) => ({
        id: book.id,
        title: book.titulo,
        publisher: book.editora,
        isbn: book.isbn,
        publicationYear: book.ano_publicacao,
        author: book.autor,
        id_loan: book.id_loan,
      }));

      console.log(bd_books);

      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      bd_loans = bd_loans.map((loan: any) => ({
        bookTitle:
          bd_books.find(
            // eslint-disable-next-line @typescript-eslint/no-explicit-any
            (book: { id_loan: any }) => book.id_loan === loan?.id
          )?.title ?? "",
        data_retirado: loan.data_retirado,
        data_devolucao: loan.data_devolucao,
        id_leitor: loan.id_leitor,
        id_livro: loan.id_livro,
        id: loan.id,
        status: loan.data_retirado ? "Returned" : "Active",
      }));

      setLoans(bd_loans);
    };
    run();
  }, []);

  const [searchTerm, setSearchTerm] = useState("");

  const filteredLoans = loans.filter(
    (loan) =>
      loan.bookTitle.toLowerCase().includes(searchTerm.toLowerCase()) ||
      loan.readerName.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const onHandleCreateLoan = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = event.currentTarget as HTMLFormElement;
    const formData = new FormData(form);

    const dueDate = formData.get("dueDate");
    const bookId = formData.get("book-id");
    const readerId = formData.get("reader-id");

    createLoan({
      data_devolucao: dueDate,
      id_leitor: readerId,
      id_livro: bookId,
    });
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div className="relative w-72">
          <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
          <Input
            placeholder="Search loans..."
            className="pl-8"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
        <Dialog>
          <DialogTrigger asChild>
            <Button>
              <Plus className="mr-2 h-4 w-4" />
              New Loan
            </Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>Create New Loan</DialogTitle>
              <DialogDescription>
                Enter the loan details below.
              </DialogDescription>
            </DialogHeader>
            <form onSubmit={onHandleCreateLoan} className="grid gap-4 py-4">
              <div className="grid gap-2">
                <Label htmlFor="book">Book ID</Label>
                <Input id="book-id" name="book-id" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="reader">Reader ID</Label>
                <Input id="reader" name="reader-id" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="dueDate">Due Date</Label>
                <Input id="dueDate" name="dueDate" type="date" />
              </div>
              <Button type="submit">Create Loan</Button>
            </form>
          </DialogContent>
        </Dialog>
      </div>

      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>ID</TableHead>
              <TableHead>Book</TableHead>
              <TableHead>Due Date</TableHead>
              <TableHead>Status</TableHead>
              <TableHead>Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filteredLoans.map((loan, i) => (
              <TableRow key={i}>
                <TableCell>{loan.id}</TableCell>
                <TableCell>{loan.bookTitle}</TableCell>
                <TableCell>{loan.data_devolucao}</TableCell>
                <TableCell>
                  <span
                    className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${
                      loan.status === "Active"
                        ? "bg-green-100 text-green-800"
                        : loan.status === "Overdue"
                        ? "bg-red-100 text-red-800"
                        : "bg-gray-100 text-gray-800"
                    }`}
                  >
                    {loan.status}
                  </span>
                </TableCell>
                <TableCell>
                  <Button
                    variant="ghost"
                    size="sm"
                    disabled={loan.status === "Returned"}
                  >
                    Return
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
