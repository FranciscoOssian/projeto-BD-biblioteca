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
import { createReader, getAllReaders } from "@/lib/api";

type Reader = {
  id: string;
  name: string;
  type: "Student" | "Teacher";
  registration_date: string;
};

export function ReadersTab() {
  const [readers, setReaders] = useState<Reader[]>([]);
  const [selectedType, setSelectedType] = useState("student");
  useEffect(() => {
    const run = async () => {
      let bd_readers = await getAllReaders();

      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      bd_readers = bd_readers.map((reader: any) => ({
        name: reader.nome,
        address: reader.address,
        registration_date: reader.data_registro,
        type: reader.tipo_leitor,
        student_attributes: reader.student_attributes,
        teacher_attributes: reader.teacher_attributes,
      }));

      setReaders(bd_readers);
    };
    run();
  }, []);

  const [searchTerm, setSearchTerm] = useState("");

  const filteredReaders = readers.filter((reader) =>
    reader.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const onHandleNewReader = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = event.currentTarget as HTMLFormElement;
    const formData = new FormData(form);
    formData.append("type", selectedType);

    const name = formData.get("name");
    const address = formData.get("address");
    const type = formData.get("type");
    const email = formData.get("email");
    const subject = formData.get("course");
    const age = formData.get("age");
    const school = formData.get("school");

    createReader({
      name,
      address,
      registration_date: new Date().toISOString(),
      type,
      student_attributes: type === "student" ? { age, school } : undefined,
      teacher_attributes: type === "teacher" ? { subject, email } : undefined,
    });
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div className="relative w-72">
          <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
          <Input
            placeholder="Search readers..."
            className="pl-8"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
        <Dialog>
          <DialogTrigger asChild>
            <Button>
              <Plus className="mr-2 h-4 w-4" />
              Add Reader
            </Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>Add New Reader</DialogTitle>
              <DialogDescription>
                Enter the details of the new reader below.
              </DialogDescription>
            </DialogHeader>
            <form onSubmit={onHandleNewReader} className="grid gap-4 py-4">
              <div className="grid gap-2">
                <Label htmlFor="name">Name</Label>
                <Input id="name" name="name" required />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="address">Address</Label>
                <Input id="address" name="address" required />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="type">Type</Label>
                <Select
                  value={selectedType}
                  onValueChange={setSelectedType}
                  required
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select type" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="student">Student</SelectItem>
                    <SelectItem value="teacher">Teacher</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              {selectedType === "student" && (
                <>
                  <div className="grid gap-2">
                    <Label htmlFor="age">Age</Label>
                    <Input id="age" type="number" name="age" required />
                    <Label htmlFor="age">School</Label>
                    <Input id="school" name="school" required />
                  </div>
                </>
              )}
              {selectedType === "teacher" && (
                <>
                  <div className="grid gap-2">
                    <Label htmlFor="email">Email</Label>
                    <Input id="email" type="email" name="email" required />
                    <Label htmlFor="course">Course</Label>
                    <Input id="course" name="course" required />
                  </div>
                </>
              )}
              <Button type="submit">Save Reader</Button>
            </form>
          </DialogContent>
        </Dialog>
      </div>

      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>ID</TableHead>
              <TableHead>Name</TableHead>
              <TableHead>Type</TableHead>
              <TableHead>Registration Date</TableHead>
              <TableHead>Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filteredReaders.map((reader, i) => (
              <TableRow key={i}>
                <TableCell>{i}</TableCell>
                <TableCell>{reader.name}</TableCell>
                <TableCell>{reader.type}</TableCell>
                <TableCell>
                  {new Date(reader.registration_date).toLocaleDateString(
                    "pt-BR",
                    {
                      weekday: "long",
                      year: "numeric",
                      month: "long",
                      day: "numeric",
                      hour: "2-digit",
                      minute: "2-digit",
                      second: "2-digit",
                      timeZoneName: "short",
                    }
                  )}
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
