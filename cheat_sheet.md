# Markdown to HTML Cheatsheet

## HTML Headings
```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
```

## Markdown Headings
```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

## HTML Paragraphs
```html
<p>This is a paragraph of text.</p>
```

## Markdown Paragraphs
```markdown
This is a paragraph of text.
```

## HTML Bold
```html
<p>This is a <b>bold</b> word.</p>
```

## Markdown Bold
```markdown
This is a **bold** word.
```

## HTML Italics
```html
<p>This is an <i>italic</i> word.</p>
```

## Markdown Italics
```markdown
This is an _italic_ word.
```

**Note:** `*this is italic*` and `_this is italic_` both work in markdown, but we'll use `_italic_` in this project.

## HTML Links
```html
This is a paragraph with a <a href="https://www.google.com">link</a>.
```

## Markdown Links
```markdown
This is a paragraph with a [link](https://www.google.com).
```

## HTML Images
```html
<img src="url/of/image.jpg" alt="Description of image" />
```

## Markdown Images
```markdown
![alt text for image](url/of/image.jpg)
```

## HTML Unordered Lists
```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

## Markdown Unordered Lists
```markdown
- Item 1
- Item 2
- Item 3
```

**Note:** `- Item 1` and `* Item 1` both work in markdown, but we'll use `- Item 1` in this project.

## HTML Ordered Lists
```html
<ol>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ol>
```

## Markdown Ordered Lists
```markdown
1. Item 1
2. Item 2
3. Item 3
```

## HTML Quotes
```html
<blockquote>This is a quote.</blockquote>
```

## Markdown Quotes
```markdown
> This is a quote.
```

## HTML Code (Inline)
```html
<code>This is code</code>
```

## Markdown Code (Inline)
```markdown
`This is code`
```

## HTML Code (Block)
```html
<pre><code>This is a code block</code></pre>
```

## Markdown Code (Block)
```markdown
```
This is a code block
```
```

---

## Project Architecture: Understanding `textnode.py`

### Purpose of `textnode.py`
`textnode.py` is your **core data structure file**. It defines:

- **`TextType` enum** - All the different types of inline text elements your markdown parser can handle (`TEXT`, `BOLD`, `ITALIC`, `CODE`, `LINK`, `IMAGE`)

- **`TextNode` class** - A data structure that represents a piece of text with a specific type. Think of it as the "intermediate representation" between raw markdown and HTML.

- **`text_node_to_html_node()` function** *(when implemented)* - The converter that takes a `TextNode` and turns it into the appropriate HTML (`LeafNode`).

### Its Role Going Forward
`textnode.py` is like the **foundation** of your markdown parser. It's the common language that all your other modules speak:

```
Raw Markdown → (parsing functions) → TextNodes → (conversion function) → HTML
```

So when you create new parsing modules like `inline_markdown.py`, you'll:

1. **Import** from `textnode.py` (the classes and enums)
2. **Create functions** that work with `TextNodes`
3. **Not modify** `textnode.py` itself unless you need new text types

Think of `textnode.py` as your **"vocabulary"** - other files use this vocabulary but don't change it. Your new `inline_markdown.py` file is a **"parser"** that takes raw text and creates `TextNodes` using that vocabulary.

### Example Flow
```python
# 1. Start with raw markdown text
raw_text = "This is **bold** and `code`"

# 2. Parse into TextNodes using inline_markdown.py
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

nodes = [TextNode(raw_text, TextType.TEXT)]
nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

# Result: [
#   TextNode("This is ", TextType.TEXT),
#   TextNode("bold", TextType.BOLD), 
#   TextNode(" and ", TextType.TEXT),
#   TextNode("code", TextType.CODE)
# ]

# 3. Convert TextNodes to HTML (future step)
# Each TextNode becomes appropriate HTML element
```

This architecture keeps your code **modular** and **maintainable**!