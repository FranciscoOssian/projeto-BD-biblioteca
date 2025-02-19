import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export const createBooks = async (books: unknown[]) => {
  try {
    const payload = { books };
    const response = await api.post("/create/books/", payload);
    return response.data;
  } catch (error) {
    console.error("Erro ao criar livros:", error);
    throw error;
  }
};

export const getAllBooks = async () => {
  try {
    const response = await api.get("/read/book/");
    return response.data;
  } catch (error) {
    console.error("Erro ao criar livros:", error);
    throw error;
  }
};

export const getAllReaders = async () => {
  try {
    const response = await api.get("/read/readers/");
    return response.data;
  } catch (error) {
    console.error("Erro ao ler livros:", error);
    throw error;
  }
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const createReader = async (reader: any) => {
  Object.keys(reader).forEach((key) => {
    if (reader[key] === undefined) {
      delete reader[key];
    }
  });
  console.log(reader);
  try {
    const payload = { reader };
    const response = await api.post("/create/reader/", payload);
    return response.data;
  } catch (error) {
    console.error("Erro ao criar reader:", error);
    throw error;
  }
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const createEmployee = async (employee: any) => {
  Object.keys(employee).forEach((key) => {
    if (employee[key] === undefined) {
      delete employee[key];
    }
  });
  console.log(employee);
  try {
    const payload = { employee };
    const response = await api.post("/create/employee/", payload);
    return response.data;
  } catch (error) {
    console.error("Erro ao criar funcionário:", error);
    throw error;
  }
};

export const getAllEmployees = async () => {
  try {
    const response = await api.get("/read/employees");
    return response.data;
  } catch (error) {
    console.error("Erro ao ler employee:", error);
    throw error;
  }
};

export const getAllLoans = async () => {
  try {
    const response = await api.get("/read/loans");
    return response.data;
  } catch (error) {
    console.error("Erro ao ler loans:", error);
    throw error;
  }
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const createLoan = async (loan: any) => {
  console.log(loan);
  try {
    const payload = { loan };
    const response = await api.post("/create/loan", payload);
    return response.data;
  } catch (error) {
    console.error("Erro ao criar loan:", error);
    throw error;
  }
};

export default api;
