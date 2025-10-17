# Products / Orders Microservice (Team: Wali + Aashish)

This repository implements the **Products/Orders microservice**, one of three services in our team’s distributed
application for **Sprint 1**. It provides endpoints for managing product inventory and customer orders, and serves
as the **Swagger-first** microservice in the architecture.

---

## 📦 Architecture Overview

This service defines resources for **Products** and **Orders** and provides integration endpoints to connect with
the other microservices.

### Endpoints Overview
| Path | Method | Description |
|------|---------|-------------|
| `/api/v1/products` | GET / POST | List or create products |
| `/api/v1/products/{product_id}` | GET / PUT / DELETE | Retrieve, update, or delete a product |
| `/api/v1/orders` | GET / POST | List or create orders |
| `/api/v1/orders/{order_id}` | GET / PUT / DELETE | Retrieve, update, or delete an order |
| `/api/v1/orders/user/{user_id}` | GET | Get all orders for a given user (integrates with Users service) |
| `/api/v1/orders/facility/{facility_id}` | GET | Get all orders for a given facility (integrates with Locations service) |

All endpoints currently return `501 Not Implemented` as placeholders for Sprint 1.

---

## Folder Structure

```
products-orders-service-v2/
├── app/
│   ├── main.py
│   ├── models.py
│   └── routers/
│       ├── products.py
│       └── orders.py
├── docs/
│   └── openapi.yaml
├── requirements.txt
└── .gitignore
```

---

## How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/products-orders-service.git
cd products-orders-service
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# or
.venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Service
```bash
uvicorn app.main:app --reload --port 8080
```

### 5️⃣ Open in Browser
•	Official Swagger spec (API-first design): open /docs/openapi.yaml in Swagger Editor
This file is the true API contract for this microservice in Sprint 1.
        You can open the spec visually in Swagger Editor:
        1.	Go to 👉 https://editor.swagger.io
        2.	In the top-left menu, click File → Import file…
        3.	Select docs/openapi.yaml from this repository.
        4.	Swagger Editor will render all endpoints and schemas. You can expand each operation (GET, POST, PUT, DELETE) and check parameters, request bodies, and responses.

        Swagger Editor automatically checks for:
        •	Missing or invalid path parameters
        •	Schema or type mismatches
        •	Duplicated operation IDs
        •	Invalid YAML indentation

•	Auto-generated FastAPI docs (for stub testing): http://localhost:8080/docs
These are generated automatically by FastAPI from the placeholder routes.
---

## 🧱 Integration Notes

- **Users Service (Sahasra + Molly)** → provides `/users/{id}` and authentication data used by orders.
- **Locations Service (Thai + Rebecca)** → provides `/facilities/{id}` data used for mapping orders to facilities.
- **Products / Orders Service (Wali + Aashish)** → defines the product and order management endpoints and integration routes.

These services will later communicate via REST calls or service registry (to be defined in later sprints).

---

## 📋 Sprint 1 Deliverables (for this repo)

- [x] Swagger/OpenAPI spec (`/docs/openapi.yaml`)
- [x] Placeholder endpoints returning 501
- [x] Versioned routes `/api/v1/...`
- [x] Integration endpoints added
- [ ] Deploy service on a VM and connect from browser
- [ ] Connect to MySQL instance on separate VM (future work)

---

## 🧠 Summary

This microservice establishes the **API contract** for product and order data and demonstrates a **Swagger‑first design**
workflow. It complements the other two microservices and sets the stage for data persistence and real integration in later sprints.