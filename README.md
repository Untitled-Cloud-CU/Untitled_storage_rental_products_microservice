# Storage Rental Service - Storage Units & Rentals Microservice (Team: Wali + Aashish)

This repository implements the **Storage Rental microservice** for a **Storage Rental Platform** (like Airbnb for storage). It provides endpoints for managing storage unit listings and rental bookings, and serves as the **Swagger/API-first** microservice in the architecture.

---

## 🏗️ Architecture Overview

This service manages two main resources:

- **Storage Units**: Listings of available storage spaces (like property listings on Airbnb)
- **Rentals**: Booking records when users rent storage units (like reservations)

### Key Concepts

- **Owners**: Users who list their storage spaces for rent
- **Renters**: Users who book/rent storage spaces
- **Storage Units**: Physical storage spaces with details like size, type, location, and pricing
- **Rentals**: Booking agreements between owners and renters

---

## 📋 Endpoints Overview

### Storage Units

| Path                                           | Method             | Description                                |
| ---------------------------------------------- | ------------------ | ------------------------------------------ |
| `/api/v1/storage-units`                        | GET / POST         | List or create storage units               |
| `/api/v1/storage-units/{unit_id}`              | GET / PUT / DELETE | Retrieve, update, or delete a storage unit |
| `/api/v1/storage-units/{unit_id}/rentals`      | GET                | Get storage unit with rental history       |
| `/api/v1/storage-units/owner/{owner_user_id}`  | GET                | Get all units owned by a user              |
| `/api/v1/storage-units/location/{location_id}` | GET                | Get all units at a location                |

### Rentals

| Path                                             | Method             | Description                          |
| ------------------------------------------------ | ------------------ | ------------------------------------ |
| `/api/v1/rentals`                                | GET / POST         | List or create rentals               |
| `/api/v1/rentals/{rental_id}`                    | GET / PUT / DELETE | Retrieve, update, or delete a rental |
| `/api/v1/rentals/{rental_id}/confirm`            | POST               | Confirm a pending rental             |
| `/api/v1/rentals/{rental_id}/activate`           | POST               | Activate a confirmed rental          |
| `/api/v1/rentals/{rental_id}/complete`           | POST               | Complete an active rental            |
| `/api/v1/rentals/{rental_id}/cancel`             | POST               | Cancel a rental                      |
| `/api/v1/rentals/renter/{renter_user_id}`        | GET                | Get rentals by renter                |
| `/api/v1/rentals/owner/{owner_user_id}`          | GET                | Get rentals by owner                 |
| `/api/v1/rentals/storage-unit/{storage_unit_id}` | GET                | Get rentals for a storage unit       |
| `/api/v1/rentals/location/{location_id}`         | GET                | Get rentals at a location            |

All endpoints currently return `501 Not Implemented` as placeholders for Sprint 1.

---

## How to Run Locally

### Clone the Repository

```bash
git clone <repository-url>
cd products_microservice
```

### Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# or
.venv\Scripts\activate      # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Service

```bash
uvicorn app.main:app --reload --port 8080
```

### View API Documentation

**Option 1: Swagger Editor (API-First Spec - Recommended)**

1. Go to https://editor.swagger.io
2. Click **File → Import file...**
3. Select `docs/openapi.yaml` from this repository
4. The Swagger Editor will render all endpoints and schemas with validation

## 🗄️ Database Schema

The database schema is defined in `/db/db/products.sql`:

### Tables

1. **storage_units**: Storage unit listings

   - id, name, description, size, unit_type, dimensions
   - location_id (FK to location service), owner_user_id
   - price_amount, price_currency
   - available, features (JSON)
   - timestamps

2. **rentals**: Rental bookings
   - id, storage_unit_id (FK), renter_user_id, owner_user_id
   - start_date, end_date
   - monthly_rate_amount, monthly_rate_currency
   - total_paid_amount, total_paid_currency
   - status (pending, confirmed, active, completed, cancelled)
   - notes, timestamps

---

## Data Models

### StorageUnit

- **Size categories**: small, medium, large, extra_large
- **Types**: indoor, outdoor, climate_controlled, vehicle, warehouse
- **Features**: array of amenities (24/7 access, security cameras, etc.)

### Rental

- **Status flow**: pending → confirmed → active → completed
- Can be cancelled at any time
- Tracks monthly rate and total amount paid

---

## 🎯 Swagger-First Approach

This microservice uses a **Swagger/API-first** design approach:

- The `docs/openapi.yaml` file is the **source of truth** for the API contract
- Models in code align with the OpenAPI spec
- Spec is hand-written and validated before implementation
- Complementary to other microservices using code-first approaches

---

## 👥 Team

**Wali + Aashish**

---
