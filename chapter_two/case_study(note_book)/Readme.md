# Notebook System Design

## 📓 Notebook Class (`notebook.py`)

A container class for managing multiple notes with search and modification capabilities.

### Attributes
- `notes`: List[Note] - Collection of `Note` objects

### Methods
| Method            | Parameters                  | Return Type | Description                                                                 |
|-------------------|-----------------------------|-------------|-----------------------------------------------------------------------------|
| `search`          | `filter: str`               | List[Note]  | Returns notes containing the filter text in memo or tags                   |
| `new_note`        | `memo: str`, `tags: str=''` | None        | Creates new note and adds it to the collection                             |
| `modify_memo`     | `note_id: int`, `memo: str` | None        | Updates the memo content of specified note                                 |
| `modify_tags`     | `note_id: int`, `tags: str` | None        | Updates the tags of specified note                                         |

## 📝 Note Class (`notebook.py`)

Individual note entity with content and metadata.

### Attributes
- `memo: str` - Note content text
- `created_at: datetime` - Timestamp of note creation 
- `tags: str` - Space-separated tags (e.g., "important todo")

### Methods
| Method            | Parameters                  | Return Type | Description                                                                 |
|-------------------|-----------------------------|-------------|-----------------------------------------------------------------------------|
| `match`           | `search_filter: str`        | bool        | Returns True if filter is found in memo or tags (case-insensitive)         |

## Project Structure
- case_study(note_book)/
    - command_option.py     # CLI command parser and handler
    - menu.py    # User interface components 
    - note_book/
        - note_book.py      # Notebook and Note class implementations

