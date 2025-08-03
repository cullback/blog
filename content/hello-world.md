+++
title = "Hello World: A Markdown Feature Showcase"
date = 2025-08-03
description = "A demonstration of Markdown features including tables, LaTeX math, and syntax highlighting"

[taxonomies]
tags = ["markdown", "demo", "hello-world"]
+++

Welcome to my new blog! This post demonstrates various Markdown features supported by Zola, including tables, LaTeX math rendering, and code syntax highlighting.

<!-- more -->

## Markdown Tables

Here's an example of a Markdown table showing different programming languages and their features:

| Language | Type System | Paradigm | Year Created |
|----------|-------------|----------|--------------|
| Python | Dynamic | Multi-paradigm | 1991 |
| Rust | Static | Systems | 2010 |
| JavaScript | Dynamic | Multi-paradigm | 1995 |
| Go | Static | Concurrent | 2009 |
| Haskell | Static | Functional | 1990 |

Tables can also be aligned:

| Left Aligned | Center Aligned | Right Aligned |
|:-------------|:--------------:|--------------:|
| Cell 1       | Cell 2         | Cell 3        |
| Lorem        | Ipsum          | Dolor         |
| Sit          | Amet           | Consectetur   |

## LaTeX Math Rendering

Zola supports both inline and display math using KaTeX. Here are some examples:

### Inline Math

The quadratic formula is $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$, which gives us the roots of a quadratic equation.

Euler's identity is often cited as the most beautiful equation in mathematics: $e^{i\pi} + 1 = 0$.

### Display Math

The Gaussian integral:

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

Maxwell's equations in differential form:

$$\begin{align}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{align}$$

The definition of the Fourier transform:

$$\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i x \xi} dx$$

## Code Syntax Highlighting

Zola provides excellent syntax highlighting for various programming languages. Here are some examples:

### Python

```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    
    return sequence

# Example usage
fib_numbers = fibonacci(10)
print(f"First 10 Fibonacci numbers: {fib_numbers}")
```

### Rust

```rust
use std::collections::HashMap;

#[derive(Debug)]
struct User {
    id: u32,
    name: String,
    email: String,
}

impl User {
    fn new(id: u32, name: String, email: String) -> Self {
        User { id, name, email }
    }
    
    fn display(&self) {
        println!("User {}: {} ({})", self.id, self.name, self.email);
    }
}

fn main() {
    let mut users: HashMap<u32, User> = HashMap::new();
    
    users.insert(1, User::new(1, "Alice".to_string(), "alice@example.com".to_string()));
    users.insert(2, User::new(2, "Bob".to_string(), "bob@example.com".to_string()));
    
    for (_, user) in &users {
        user.display();
    }
}
```

### JavaScript

```javascript
// Modern ES6+ JavaScript example
class TodoList {
    constructor() {
        this.todos = [];
        this.nextId = 1;
    }
    
    addTodo(text) {
        const todo = {
            id: this.nextId++,
            text,
            completed: false,
            createdAt: new Date()
        };
        this.todos.push(todo);
        return todo;
    }
    
    toggleTodo(id) {
        const todo = this.todos.find(t => t.id === id);
        if (todo) {
            todo.completed = !todo.completed;
        }
    }
    
    getActiveTodos() {
        return this.todos.filter(todo => !todo.completed);
    }
}

// Usage with async/await
async function fetchAndAddTodos() {
    const todoList = new TodoList();
    
    try {
        const response = await fetch('/api/todos');
        const todos = await response.json();
        
        todos.forEach(todo => {
            todoList.addTodo(todo.text);
        });
        
        console.log(`Added ${todos.length} todos`);
    } catch (error) {
        console.error('Failed to fetch todos:', error);
    }
}
```

### HTML/CSS

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semantic HTML Example</title>
    <style>
        :root {
            --primary-color: #007bff;
            --text-color: #333;
            --bg-color: #f8f9fa;
        }
        
        body {
            font-family: system-ui, -apple-system, sans-serif;
            color: var(--text-color);
            background-color: var(--bg-color);
            line-height: 1.6;
        }
        
        .card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease;
        }
        
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }
    </style>
</head>
<body>
    <main>
        <article class="card">
            <h1>Welcome to Semantic HTML</h1>
            <p>Using proper HTML5 semantic elements improves accessibility and SEO.</p>
        </article>
    </main>
</body>
</html>
```

## Conclusion

This blog is now set up with:

- ✅ Zola static site generator
- ✅ Pico CSS for clean, semantic styling
- ✅ KaTeX for beautiful math rendering
- ✅ Syntax highlighting for code blocks
- ✅ Responsive design out of the box

Feel free to explore these features and start writing your own posts!