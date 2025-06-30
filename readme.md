# No JS, No overhead Server-Side Rendering with FastAPI & Jinja2

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
  ![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
  ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

  *A minimalist approach to web development — just HTML and two Python libraries*

</div>

---

## ✨ Overview

This repository serves as a focused exploration of **server-side rendering (SSR)** using Python — specifically leveraging **FastAPI** with **Jinja2 templates**. The motivation arose during the development of my full-stack project, **nabu-archive**, where I encountered the increasing overhead and complexity of modern frontend frameworks like React and Next.js, particularly for handling simple data operations.

Modern SPAs often require a significant amount of boilerplate: defining components, making API calls inside lifecycle hooks like `useEffect`, setting up state management, and then rendering data dynamically. For straightforward use cases, this can be unnecessarily heavy — both in terms of developer experience and runtime performance.

Instead, this project takes a more **minimalist and declarative approach**, where the backend directly renders HTML views by embedding data within Jinja templates. This paradigm allows the backend to **define the shape of the UI** and return pre-rendered HTML over HTTP, significantly reducing client-side complexity and increasing performance. In many cases, it's a leaner, more maintainable solution that eliminates the need for redundant frontend logic.

This approach is not only elegant but practical: it's fast, efficient, and easily composable. For example, if I wanted to reuse this rendered view within a Next.js application, I could simply embed it using an `<iframe>`. Ultimately, the goal is not to chase trends or toolchains, but to prioritize **clarity, performance, and functionality** — and this project is a study in achieving exactly that.

Certain components of the *Full Stagnable Archive* project are being reimagined under this paradigm, with an emphasis on declarative, server-driven rendering where it makes architectural sense.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL

## 📁 Project Structure

```
├── app.py              # Main FastAPI application
├── model.py            # Database models
├── schema.py           # Pydantic schemas
└── templates/
    └── item.html       # Jinja2 template with Apple-inspired UI
```

---

## 🛠 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/items/` | List all items (JSON) |
| `POST` | `/items/` | Create new item |
| `GET` | `/items/{id}` | View item (HTML) |
| `DELETE` | `/items/{id}` | Delete item |

---

## 🎨 Features

- **Apple-inspired UI** — Clean, minimalist design with glassmorphism effects
- **Server-side rendering** — No client-side JavaScript required
- **Responsive design** — Works seamlessly on desktop and mobile
- **Database integration** — PostgreSQL with SQLAlchemy
- **Type safety** — Pydantic schemas for data validation

---

## 🧪 Testing

```bash
# Create a test item
curl -X POST "http://127.0.0.1:8000/items/" \
     -H "Content-Type: application/json" \
     -d '{"title": "iPhone 15", "description": "Latest Apple smartphone", "price": "$999"}'

# View the rendered HTML
open http://127.0.0.1:8000/items/1
```

---

## 🤔 Why This Approach?

### Traditional SPA Complexity
```javascript
// React component with unnecessary overhead
useEffect(() => {
  fetch('/api/items/1')
    .then(res => res.json())
    .then(data => setItem(data))
}, [])

return (
  <div>
    {item ? (
      <div>
        <h1>{item.title}</h1>
        <p>{item.description}</p>
      </div>
    ) : (
      <div>Loading...</div>
    )}
  </div>
)
```

### Our Simplified Approach
```html
<!-- Direct, declarative rendering -->
<h1>{{ item.title }}</h1>
<p>{{ item.description }}</p>
```

**Result:** Faster load times, simpler codebase, better SEO, and reduced complexity.

---

## 🔧 Stack Simplicity

This entire application runs on just **two Python libraries**:
- **FastAPI** — Modern, fast web framework
- **Jinja2** — Powerful templating engine

Plus standard HTML/CSS for the frontend. No build tools, no bundlers, no complex state management — just clean, server-rendered web pages.

---

## 📈 Performance Benefits

- **Faster initial page load** — No client-side hydration
- **Better SEO** — Fully rendered HTML served to crawlers
- **Reduced complexity** — No state management or lifecycle hooks
- **Lower bandwidth** — No heavy JavaScript bundles
- **Improved accessibility** — Works without JavaScript

---

## 🎯 Use Cases

Perfect for:
- **Content-heavy websites** — Blogs, documentation, portfolios
- **Admin dashboards** — Internal tools with simple interactions
- **MVP development** — Rapid prototyping without frontend complexity
- **SEO-critical pages** — Landing pages, product catalogs
- **Legacy system modernization** — Incremental improvements

---


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p><strong>Built with curiosity for simplicity and performance</strong></p>
</div>