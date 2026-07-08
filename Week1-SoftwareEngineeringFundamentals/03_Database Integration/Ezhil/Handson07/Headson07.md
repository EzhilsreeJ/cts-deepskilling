# Hands-On 7 – Database Version Control with Alembic

## Objective

Implement database schema version control using Alembic by generating, applying, upgrading, and downgrading database migrations with SQLAlchemy.

---

# Task 1 – Alembic Setup and Initial Migration

## Step 92 – Initialize Alembic

Install Alembic and initialize the migration environment.

```bash
pip install alembic

alembic init migrations
```

### Output

![Step 92 Output](Screenshot/image.png)

---

## Step 93 – Configure Alembic

Update the database connection in `alembic.ini`.

```ini
sqlalchemy.url = mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/college_db
```

Update `migrations/env.py` to import the SQLAlchemy metadata.

```python
from models import Base

target_metadata = Base.metadata
```

---

## Step 94 – Configure SQLAlchemy Metadata

Use the metadata from `models.py` so Alembic can detect schema changes automatically.

```python
from models import Base

target_metadata = Base.metadata
```

---

## Step 95 – Generate the Initial Migration

Generate the first migration using the existing SQLAlchemy models.

```bash
alembic revision --autogenerate -m "initial schema"
```

### Output

![Step 95 Output](Screenshot/image-1.png)

---

## Step 96 – Inspect the Generated Migration

Open the generated migration file under:

```text
migrations/
└── versions/
```

Verify that it contains both migration methods.

```python
def upgrade():
    ...

def downgrade():
    ...
```

### Output

![Step 96 Output](Screenshot/image-2.png)

---

## Step 97 – Apply the Initial Migration

Apply the generated migration.

```bash
alembic upgrade head
```

Verify that Alembic creates the `alembic_version` table.

### Output

![Step 97 Output](Screenshot/image-3.png)

---

# Task 2 – Modify Existing Schema

## Step 98 – Add the `is_active` Column

Modify the `Student` model.

```python
from sqlalchemy import Boolean

is_active = Column(Boolean, default=True)
```

---

## Step 99 – Generate Migration for the New Column

Generate a migration after modifying the model.

```bash
alembic revision --autogenerate -m "add is_active column"
```

### Output

![Step 99 Output](Screenshot/image-4.png)

---

# Task 2 – Modify Existing Schema (Continued)

## Step 100 – Verify the Generated Migration

Open the newly generated migration file and verify that the `upgrade()` and `downgrade()` methods contain the required schema changes.

```python
def upgrade():
    op.add_column(
        'students',
        sa.Column('is_active', sa.Boolean(), nullable=True)
    )

def downgrade():
    op.drop_column(
        'students',
        'is_active'
    )
```

### Output

![Step 100 Output](Screenshot/image-5.png)

---

## Step 101 – Apply the Migration

Apply the migration to update the database schema.

```bash
alembic upgrade head
```

Verify that the `students` table now contains the `is_active` column.

### Output

![Step 101 Output](Screenshot/image-6.png)

---

## Step 102 – Create the `CourseSchedule` Model

Add a new SQLAlchemy model.

```python
class CourseSchedule(Base):
    __tablename__ = "course_schedules"

    schedule_id = Column(Integer, primary_key=True)

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    day_of_week = Column(String(20))
    start_time = Column(String(20))
    end_time = Column(String(20))
```

---

## Step 103 – Generate and Apply Migration

Generate and apply the migration for the new model.

```bash
alembic revision --autogenerate -m "create course_schedule"

alembic upgrade head
```

Verify that the `course_schedules` table has been created.

### Output

![Step 103 Output](Screenshot/image-7.png)

---

# Task 3 – Rollback and Recovery

## Step 104 – Check the Current Migration Revision

```bash
alembic current
```

### Output

![Step 104 Output](Screenshot/image-8.png)

---

## Step 105 – Roll Back One Migration

```bash
alembic downgrade -1
```

### Observation

The latest migration is rolled back and the most recent schema changes are removed.

---

## Step 106 – Roll Back to the Base Version

```bash
alembic downgrade base
```

### Observation

All Alembic-managed migrations are rolled back, restoring the database to its initial state.

---

## Step 107 – Upgrade Back to the Latest Revision

```bash
alembic upgrade head
```

Verify that all migrations are applied successfully and the latest schema is restored.

### Output

![Step 107 Output](Screenshot/image-9.png)

---

## Step 108 – Django Migrations (Bonus)

**Note:** This is an optional bonus task in the handbook. The hands-on was completed using SQLAlchemy ORM and Alembic migrations.

---

# Learning Outcomes

After completing this hands-on, I was able to:

- Configure Alembic with SQLAlchemy.
- Generate database migrations automatically.
- Apply schema changes using Alembic.
- Track database versions using migration revisions.
- Modify existing database schemas through migrations.
- Roll back and reapply database migrations.
- Understand database version control using Alembic.

---

# Author

**Name:** Ezhil Sree J

**Program:** Cognizant Digital Nurture 5.0 – Python Full Stack Engineer (FSE)