# Django Debugging project
This project was created as a practice exercise for **Debugging and optimization in Django**.
The goal is to identify and fix common errors while also using debugging tools (`print` and `logging`) to trace the execution flow.

---

## Intentional Bugs Added
1. **Missing migrations**
   - The `Student` model was created with a field typo (`agee`).  
   - Without running `makemigrations` and `migrate`, Django raises a migration warning/error.  

2. **Incorrect field name**  
   - In `views.py`, `student["namee"]` was used instead of `student["name"]`.  
   - **Result:** `500 Internal Server Error (KeyError)`.  

3. **Wrong template variable**  
   - In `home.html`, the template tried to access `{{ username }}`, but the context did not provide this variable.  
   - **Result:** The page loads, but the value is missing.  

4. **HTTP 404**  
   - The `missing_page_view` was created but **not registered in `urls.py`**.  
   - **Result:** Navigating to `/missing/` returned a 404 page not found.  

5. **HTTP 500**  
   - Due to the wrong dictionary key (`namee`), the app raised an exception.  
   - **Result:** Django displayed a **500 Internal Server Error**.  

---

## How the Errors Were Fixed

- Running migrations properly:  
  ```bash
  python manage.py makemigrations
  python manage.py migrate
