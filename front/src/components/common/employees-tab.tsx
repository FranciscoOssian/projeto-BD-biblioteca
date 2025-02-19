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
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Plus, Search } from "lucide-react";
import { createEmployee, getAllEmployees } from "@/lib/api";

type Employee = {
  id: string;
  name: string;
  role: "Librarian" | "Intern";
  phone: string;
  email: string;
  startDate: string;
};

export function EmployeesTab() {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [selectedType, setSelectedType] = useState("librarian");
  useEffect(() => {
    const run = async () => {
      let bd_employees = await getAllEmployees();

      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      bd_employees = bd_employees.map((employee: any) => ({
        name: employee.nome,
        phone: employee.telefone,
        role: employee.role,
        intern_attributes: employee.intern_attributes,
        librarian_attributes: employee.librarian_attributes,
      }));

      setEmployees(bd_employees);
    };
    run();
  }, []);

  const [searchTerm, setSearchTerm] = useState("");

  const filteredEmployees = employees.filter(
    (employee) =>
      employee.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      employee.email.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const onHandleCreateEmployee = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = event.currentTarget as HTMLFormElement;
    const formData = new FormData(form);
    formData.append("type", selectedType);

    const name = formData.get("name");
    const phone = formData.get("phone");
    const dueDate = formData.get("due-date");

    createEmployee({
      nome: name,
      telefone: phone,
      role: selectedType,
      intern_attributes:
        selectedType === "intern" ? { fim_estagio: dueDate } : undefined,
      librarian_attributes:
        selectedType === "librarian" ? { tempo_trabalhado: 0 } : undefined,
    });
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div className="relative w-72">
          <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
          <Input
            placeholder="Search employees..."
            className="pl-8"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
        <Dialog>
          <DialogTrigger asChild>
            <Button>
              <Plus className="mr-2 h-4 w-4" />
              Add Employee
            </Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>Add New Employee</DialogTitle>
              <DialogDescription>
                Enter the employee details below.
              </DialogDescription>
            </DialogHeader>
            <form onSubmit={onHandleCreateEmployee} className="grid gap-4 py-4">
              <div className="grid gap-2">
                <Label htmlFor="name">Name</Label>
                <Input id="name" name="name" required />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="role">Role</Label>
                <Select
                  value={selectedType}
                  onValueChange={setSelectedType}
                  required
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select role" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="librarian">Librarian</SelectItem>
                    <SelectItem value="intern">Intern</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div className="grid gap-2">
                <Label htmlFor="phone">Phone</Label>
                <Input id="phone" name="phone" required type="tel" />
              </div>
              {selectedType === "intern" && (
                <div className="grid gap-2">
                  <Label htmlFor="age">Due Date</Label>
                  <Input id="due-date" type="date" name="due-date" required />
                </div>
              )}
              <Button type="submit">Save Employee</Button>
            </form>
          </DialogContent>
        </Dialog>
      </div>

      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Name</TableHead>
              <TableHead>Role</TableHead>
              <TableHead>Phone</TableHead>
              <TableHead>Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filteredEmployees.map((employee, i) => (
              <TableRow key={i}>
                <TableCell>{employee.name}</TableCell>
                <TableCell>{employee.role}</TableCell>
                <TableCell>{employee.phone}</TableCell>
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
