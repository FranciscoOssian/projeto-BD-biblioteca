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

export default api;
