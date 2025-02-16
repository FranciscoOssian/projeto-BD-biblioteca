import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { DashboardTab } from "@/components/common/dashboard-tab";
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
        <p className="text-muted-foreground">Manage your library efficiently</p>
      </div>

      <Tabs defaultValue="dashboard" className="space-y-4">
        <TabsList>
          <TabsTrigger value="dashboard">Dashboard</TabsTrigger>
          <TabsTrigger value="books">Books</TabsTrigger>
          <TabsTrigger value="readers">Readers</TabsTrigger>
          <TabsTrigger value="loans">Loans</TabsTrigger>
          <TabsTrigger value="employees">Employees</TabsTrigger>
          <TabsTrigger value="categories">Categories</TabsTrigger>
        </TabsList>
        <TabsContent value="dashboard">
          <DashboardTab />
        </TabsContent>
        <TabsContent value="books">
          <BooksTab />
        </TabsContent>
        <TabsContent value="readers">
          <ReadersTab />
        </TabsContent>
        <TabsContent value="loans">
          <LoansTab />
        </TabsContent>
        <TabsContent value="employees">
          <EmployeesTab />
        </TabsContent>
        <TabsContent value="categories">
          <CategoriesTab />
        </TabsContent>
      </Tabs>
    </div>
  );
}
