import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Book, Users, BookCopy } from "lucide-react";

const stats = [
  {
    title: "Total Books",
    value: "2,345",
    icon: Book,
    description: "Active inventory",
  },
  {
    title: "Total Readers",
    value: "1,234",
    icon: Users,
    description: "Registered users",
  },
  {
    title: "Current Loans",
    value: "89",
    icon: BookCopy,
    description: "Books checked out",
  },
  {
    title: "Available Books",
    value: "1,890",
    icon: Book,
    description: "Ready for checkout",
  },
];

export function DashboardTab() {
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
      {stats.map((stat) => (
        <Card key={stat.title}>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">{stat.title}</CardTitle>
            <stat.icon className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stat.value}</div>
            <p className="text-xs text-muted-foreground">{stat.description}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
