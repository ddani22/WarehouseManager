# Copilot Instructions for Proyecto Gestión Almacén

## Project Architecture
- **src/** contains all application logic, organized by domain:
  - **core/**: Business logic (e.g., `inventory_manager.py`).
  - **database/**: Database access layer, including `db_manager.py` (MySQL connection/queries) and DAOs for each entity.
  - **models/**: Data models for entities (Client, Product, Movement, Supplier).
  - **ui/**: User interface components (main window, product view).
- **config/**: Configuration files (e.g., `settings.py`).
- **tests/**: Unit tests for database and core logic.

## Database Integration
- Uses MySQL via `mysql.connector`. Connection parameters are hardcoded in `db_manager.py`.
- All database operations go through `db_manager` and DAO classes. Reuse connections; do not close after each query.
- Error handling: Print errors, rollback on failure, commit only for modifying queries.

## Developer Workflows
- **Run the app**: Execute `src/app.py` (entry point).
- **Run tests**: Use Python's unittest or pytest on files in `tests/`.
- **Install dependencies**: `pip install -r requirements.txt`.
- **Debugging**: Print statements are used for connection/query status. No advanced logging.

## Conventions & Patterns
- Class names use lowercase (e.g., `db_manager`), but models use PascalCase.
- DAOs encapsulate CRUD for each entity; do not mix business logic in DAOs.
- UI logic is separated from business/data layers.
- Spanish is used for comments and docstrings.

## Integration Points
- MySQL server must be running and accessible with credentials in `db_manager.py`.
- No external APIs or microservices; all logic is local.

## Examples
- To add a new entity: Create model in `models/`, DAO in `database/dao/`, update business logic in `core/`.
- To add a new query: Implement in DAO, call via business logic, expose via UI if needed.

## Key Files
- `src/database/db_manager.py`: MySQL connection/query manager.
- `src/database/dao/`: DAOs for each entity.
- `src/core/inventory_manager.py`: Main business logic.
- `src/ui/main_window.py`: Main UI entry.

---
Update this file if project structure or conventions change. For questions, ask for clarification on unclear workflows or patterns.
