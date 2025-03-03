
### **CRUD Library System using FastAPI**  

#### **Project Overview**  
You will build a simple **Library Management System API** using **FastAPI**. This API will allow users to:  
1. **Create** books in the library.  
2. **Read** book details by ID or list all books.  
3. **Update** book information.  
4. **Delete** books from the library.  

This project will help you understand:  
* How to set up a FastAPI project.  
* How to define API endpoints.  
* How to work with a database (SQLite with SQLAlchemy).  
* How to handle request validation with Pydantic.  

---

### **Project Tasks**  

#### **1. Set Up the Project**  
* Install dependencies: `FastAPI`, `Uvicorn`, `SQLAlchemy`, `Pydantic`, `SQLite`.  
* Set up a **virtual environment** (optional but recommended).  
* Initialize a FastAPI project structure.  

#### **2. Define the Book Model**  
* Use **SQLAlchemy** to create a `Book` table with:  
  - `id` (int, primary key)  
  - `title` (str)  
  - `author` (str)  
  - `published_year` (int)  
  - `isbn` (str, unique)  

#### **3. Implement CRUD Endpoints**  
* **POST /books/** → Add a new book.  
* **GET /books/** → Get all books.  
* **GET /books/{book_id}** → Get book details by ID.  
* **PUT /books/{book_id}** → Update book details.  
* **DELETE /books/{book_id}** → Remove a book from the library.  

#### **4. Connect to a Database**  
* Use **SQLAlchemy ORM** to interact with SQLite.  
* Create a session for handling database operations.  

#### **5. Add Validation and Error Handling**  
* Use **Pydantic** models for input validation.  
* Handle errors (e.g., book not found, invalid data).  

#### **6. Test the API**  
* Use **Swagger UI** (FastAPI provides it by default).  
* Test using **Postman** or `curl`.  

#### **7. Optional Enhancements**  
* Add authentication (JWT).  
* Implement pagination and filtering.  
* Deploy the API using **Render**, **Railway**, or **Docker**.  

---

### **Deliverables**  
* A GitHub repository with a structured FastAPI project.  
* A `README.md` with setup instructions.  
* A working API with CRUD operations.  


