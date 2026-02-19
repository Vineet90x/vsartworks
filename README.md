# VSART – Commission-Based Art Platform

VSART is a commission-driven art platform designed to sell ready-made artworks and manage limited monthly custom art commissions with strict business logic and controlled workflow.

This project is built as both:
- A revenue-generating art platform
- A production-grade backend architecture project using FastAPI

---

## 🚀 Tech Stack

### Frontend
- Next.js (SEO-optimized)
- Server-side rendering + static generation

### Backend
- FastAPI
- Service-layer architecture
- JWT Authentication
- SQLAlchemy ORM
- Alembic migrations

### Database
- PostgreSQL

### Storage
- Cloudinary (image hosting + CDN)

### Payments
- Razorpay (Webhook-based payment verification)

### Hosting
- Vercel (Frontend)
- Render (Backend)
- Neon/Supabase (PostgreSQL)

---

## 🎯 Core Business Rules

- Maximum **2 commission slots per month**
- Public visibility of available commission slots
- 50% advance or 100% full payment for commissions
- 24-hour refund window (after that non-refundable)
- Maximum 5 revisions (Sketch stage only)
- Dynamic shipping cost based on country
- Ready-made artworks automatically hidden when sold out

---

## 🏗 Architecture Overview

Browser
↓
Next.js (Vercel)
↓
FastAPI Backend (Render)
↓
PostgreSQL (Neon)
↓
Cloudinary (Images CDN)
↓
Razorpay (Payments + Webhook)
↓
Email Provider


The backend follows a strict service-layer architecture:

Routes → Services → Database

No business logic is written directly inside route handlers.

---

## 🔁 Order Lifecycle (Commission)

1. Commission request submitted
2. Admin approval or rejection
3. Advance payment required
4. Monthly slot booked after payment success
5. Order enters queue
6. Sketch shared
7. Revision stage (max 5 revisions)
8. Final payment required
9. Ready to ship
10. Shipped
11. Completed

All transitions are validated using a strict state machine.

---

## 📦 Features

### Public
- View artworks
- View available commission slots
- SEO-optimized artwork detail pages
- Category-based filtering

### User
- Register / Login
- Submit commission request
- Upload reference images
- Track live queue position
- Request revisions (max 5)
- Cancel within 24 hours
- View order history

### Admin
- Approve / reject commission requests
- Manage monthly slot capacity
- Update order statuses
- Upload sketch previews
- Manage shipping rates
- Manage coupon codes
- View analytics dashboard

---

## 💳 Payment Flow

Integrated with Razorpay.

- Backend creates Razorpay order
- Razorpay webhook verifies payment
- Signature validation enforced
- Slot booking occurs only after verified payment
- Refund logic enforced within 24-hour window

Frontend never directly marks payment success.

---

## 📊 Analytics

Admin dashboard provides:

- Total revenue
- Monthly revenue
- Orders per month
- Conversion rate
- Active commission queue

All analytics are computed via database aggregation.

---

## 🔐 Security

- JWT-based authentication
- Role-based access control
- Webhook signature verification
- Strict order state transition validation
- Concurrency-safe monthly slot handling
- Input validation using Pydantic

---

## 🧠 Technical Highlights

- Service-layer backend architecture
- Explicit order state machine
- Concurrency-safe monthly slot booking
- Dynamic queue calculation
- Coupon-ready pricing system
- Scalable infrastructure design

---

## 🛠 Development Roadmap

**Phase 1**
- Core database schema
- Monthly slot logic
- Order state machine

**Phase 2**
- Commission request + approval flow
- Payment integration (Razorpay)

**Phase 3**
- Queue calculation
- Revision control system

**Phase 4**
- Ready-made sales flow
- Shipping logic

**Phase 5**
- Coupons
- Analytics dashboard

**Phase 6**
- Production deployment

---

## 📌 Project Goals

- Build a real-world, production-ready FastAPI backend
- Enforce strict business logic at the backend level
- Maintain clean, scalable architecture
- Generate sustainable art income through structured workflow

---

## ⚠️ Design Philosophy

This system prioritizes:

- Business integrity over UI complexity
- Backend correctness over premature optimization
- Controlled workload through strict slot limits
- Clear separation of concerns

---

## 📜 License

This project is proprietary and intended for personal commercial use.
