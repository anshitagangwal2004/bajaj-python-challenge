# Bajaj Finserv Health | Python Qualifier Task

This repository contains the solution for the **Bajaj Finserv Health Python Qualifier 1**.

## ✅ Task Summary

- On application startup:
  - A POST request is sent to generate a unique webhook and access token.
  - Based on the regNo, a specific SQL question is assigned.
  - The application solves the SQL query based on provided employee, department, and payment data.
  - The final SQL query is submitted to the webhook using the provided token.

## 📄 Question

> Find the highest salary **not paid on the 1st day** of any month.  
> Return the following:
- `SALARY`
- `NAME` (First name + Last name)
- `AGE` (calculated from DOB)
- `DEPARTMENT_NAME`

## 🧠 SQL Solution (used in Python script)

```sql
SELECT 
    P.AMOUNT AS SALARY,
    E.FIRST_NAME || ' ' || E.LAST_NAME AS NAME,
    CAST((strftime('%Y', 'now') - strftime('%Y', E.DOB)) AS INTEGER) AS AGE,
    D.DEPARTMENT_NAME
FROM PAYMENTS P
JOIN EMPLOYEE E ON P.EMP_ID = E.EMP_ID
JOIN DEPARTMENT D ON E.DEPARTMENT = D.DEPARTMENT_ID
WHERE strftime('%d', P.PAYMENT_TIME) != '01'
ORDER BY P.AMOUNT DESC
LIMIT 1;
