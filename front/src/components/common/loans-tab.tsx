"use client";

import { useState } from "react";
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
  const [loans] = useState<Loan[]>(mockLoans);
  const [searchTerm, setSearchTerm] = useState("");

  const filteredLoans = loans.filter(
    (loan) =>
      loan.bookTitle.toLowerCase().includes(searchTerm.toLowerCase()) ||
      loan.readerName.toLowerCase().includes(searchTerm.toLowerCase())
  );

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
            <div className="grid gap-4 py-4">
              <div className="grid gap-2">
                <Label htmlFor="book">Book ISBN</Label>
                <Input id="book" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="reader">Reader ID</Label>
                <Input id="reader" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="dueDate">Due Date</Label>
                <Input id="dueDate" type="date" />
              </div>
            </div>
            <Button>Create Loan</Button>
          </DialogContent>
        </Dialog>
      </div>

      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>ID</TableHead>
              <TableHead>Book</TableHead>
              <TableHead>Reader</TableHead>
              <TableHead>Checkout Date</TableHead>
              <TableHead>Due Date</TableHead>
              <TableHead>Status</TableHead>
              <TableHead>Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filteredLoans.map((loan) => (
              <TableRow key={loan.id}>
                <TableCell>{loan.id}</TableCell>
                <TableCell>{loan.bookTitle}</TableCell>
                <TableCell>{loan.readerName}</TableCell>
                <TableCell>{loan.checkoutDate}</TableCell>
                <TableCell>{loan.dueDate}</TableCell>
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
