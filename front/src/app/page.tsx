import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { BooksTab } from "@/components/common/books-tab";
import { ReadersTab } from "@/components/common/readers-tab";
import { LoansTab } from "@/components/common/loans-tab";
import { EmployeesTab } from "@/components/common/employees-tab";
import { CategoriesTab } from "@/components/common/categories-tab";

export default function LibraryDashboard() {
  return (
    <div className="container mx-auto py-6 space-y-8">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">
          Library Management System
        </h1>
        <p className="text-muted-foreground">
          Manage books, readers, loans, and more.
        </p>
      </div>

      <Tabs defaultValue="books" className="space-y-4">
        <TabsList>
          <TabsTrigger value="books">Books</TabsTrigger>
          <TabsTrigger value="readers">Readers</TabsTrigger>
          <TabsTrigger value="loans">Loans</TabsTrigger>
          <TabsTrigger value="employees">Employees</TabsTrigger>
          <TabsTrigger value="categories">Categories</TabsTrigger>
        </TabsList>
        <TabsContent value="books" className="space-y-4">
          <BooksTab />
        </TabsContent>
        <TabsContent value="readers" className="space-y-4">
          <ReadersTab />
        </TabsContent>
        <TabsContent value="loans" className="space-y-4">
          <LoansTab />
        </TabsContent>
        <TabsContent value="employees" className="space-y-4">
          <EmployeesTab />
        </TabsContent>
        <TabsContent value="categories" className="space-y-4">
          <CategoriesTab />
        </TabsContent>
      </Tabs>
    </div>
  );
}
