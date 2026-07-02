from contextlib import asynccontextmanager
from sqlalchemy import func
from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException, Response, status
from sqlalchemy import select, func, or_
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from database import create_tables, get_db
from models import Course,Student, Enrollment
from schemas import CourseCreate, CourseResponse, CourseUpdate,StudentCreate,StudentResponse,EnrollmentCreate, EnrollmentResponse
from models import User
from schemas import UserCreate, UserResponse
from security import (get_password_hash,verify_password, create_access_token)
from jose import JWTError, jwt
from security import (
    oauth2_scheme,
    SECRET_KEY,
    ALGORITHM,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")
def error_response(status_code: int, code: str, message: str, field=None):
    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "code": code,
                "message": message,
                "field": field
            }
        }
    )
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(
    title="Course Management API",
    description="REST API for managing Courses, Students, and Enrollments using FastAPI.",
    version="1.0.0",
    contact={
        "name": "Ezhil",
        "email": "ezhil@example.com"
    },
    lifespan=lifespan
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# OAuth2 Authorization Code Flow:
# 1. User logs in through an authorization server.
# 2. The server returns an authorization code.
# 3. The client exchanges the code for an access token.
#
# JWT Authentication:
# 1. User logs in directly with username/password.
# 2. The server returns a signed JWT.
# 3. The client sends the JWT in the Authorization header for protected requests.


# API Versioning:
# URL Versioning  -> /api/v1/courses/
# Header Versioning -> Accept: application/vnd.api+json;version=1
# URL versioning is simpler and easier to test.
async def get_current_user(
    token: str = Depends(oauth2_scheme),
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

        return email

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )
@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a new course",
    response_description="Course created successfully"
)
async def create_course(
    course: CourseCreate,
    current_user: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    new_course = Course(**course.model_dump())

    # db.add(new_course)
    # await db.commit()
    # await db.refresh(new_course)

    # return new_course
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    headers = {
        "Location": f"/api/v1/courses/{new_course.id}"
    }

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        headers=headers,
        content=CourseResponse.model_validate(new_course).model_dump()
    )

@app.get(
    "/api/v1/courses/",
    tags=["Courses"],
)
async def get_courses(
    page: int = 1,
    page_size: int = 2,
    search: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(Course)

    if search:
        query = query.where(
            or_(
                Course.name.ilike(f"%{search}%"),
                Course.code.ilike(f"%{search}%")
            )
        )

    total = await db.scalar(
        select(func.count()).select_from(query.subquery())
    )

    offset = (page - 1) * page_size

    result = await db.execute(
        query.offset(offset).limit(page_size)
    )

    courses = result.scalars().all()

    next_page = (
        f"/api/v1/courses/?page={page+1}&page_size={page_size}&search={search or ''}"
        if offset + page_size < total
        else None
    )

    previous_page = (
        f"/api/v1/courses/?page={page-1}&page_size={page_size}&search={search or ''}"
        if page > 1
        else None
    )

    return {
        "count": total,
        "next": next_page,
        "previous": previous_page,
        "results": [
            CourseResponse.model_validate(course)
            for course in courses
        ],
    }
@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_course(
    course_id: int,
    current_user: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        # raise HTTPException(
        #     status_code=404,
        #     detail="Course not found"
        # )
        return error_response(
            404,
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )
    await db.delete(course)
    await db.commit()


    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_db),
):
    new_student = Student(**student.model_dump())

    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)

    return new_student


@app.get(
    "/api/students/{student_id}",
    response_model=StudentResponse,
    tags=["Students"]
)
async def get_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        # raise HTTPException(
        #     status_code=404,
        #     detail="Student not found"
        # )
        return error_response(
            404,
            "NOT_FOUND",
            f"Student with id {student_id} does not exist"
        )
    return student


@app.put(
    "/api/students/{student_id}",
    response_model=StudentResponse,
)
async def update_student(
    student_id: int,
    student_data: StudentCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        # raise HTTPException(
        #     status_code=404,
        #     detail="Student not found"
        # )
        return error_response(
            404,
            "NOT_FOUND",
            f"Student with id {student_id} does not exist"
        )
    student.name = student_data.name
    student.email = student_data.email

    await db.commit()
    await db.refresh(student)

    return student


@app.delete(
    "/api/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        # raise HTTPException(
        #     status_code=404,
        #     detail="Student not found"
        # )
        return error_response(
            404,
            "NOT_FOUND",
            f"Student with id {student_id} does not exist"
        )
    await db.delete(student)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# ---------------- ENROLLMENT CRUD ----------------

@app.post(
    "/api/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    new_enrollment = Enrollment(**enrollment.model_dump())

    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    result = await db.execute(
        select(Student).where(Student.id == enrollment.student_id)
    )
    student = result.scalar_one()

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return new_enrollment

@app.get(
    "/api/enrollments/{enrollment_id}",
    response_model=EnrollmentResponse,
    tags=["Enrollments"]
)
async def get_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        # raise HTTPException(
        #     status_code=404,
        #     detail="Enrollment not found"
        # )
        return error_response(
            404,
            "NOT_FOUND",
            f"Enrollment with id {enrollment_id} does not exist"
        )
    return enrollment


@app.put(
    "/api/enrollments/{enrollment_id}",
    response_model=EnrollmentResponse,
)
async def update_enrollment(
    enrollment_id: int,
    enrollment_data: EnrollmentCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        # raise HTTPException(
        #     status_code=404,
        #     detail="Enrollment not found"
        # )
        return error_response(
            404,
            "NOT_FOUND",
            f"Enrollment with id {enrollment_id} does not exist"
        )
    enrollment.student_id = enrollment_data.student_id
    enrollment.course_id = enrollment_data.course_id

    await db.commit()
    await db.refresh(enrollment)

    return enrollment


@app.delete(
    "/api/enrollments/{enrollment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        # raise HTTPException(
        #     status_code=404,
        #     detail="Enrollment not found"
        # )
        return error_response(
            404,
            "NOT_FOUND",
            f"Enrollment with id {enrollment_id} does not exist"
        )

    await db.delete(enrollment)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
)
async def patch_course(
    course_id: int,
    course_data: CourseUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        # raise HTTPException(
        #     status_code=404,
        #     detail="Course not found"
        # )
        return error_response(
            404,
            "NOT_FOUND",
            f"Course with id {course_id} does not exist"
        )
    for key, value in course_data.model_dump(exclude_unset=True).items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)

    return course

@app.post(
    "/api/v1/auth/register",
    response_model=UserResponse,
    status_code=201,
    tags=["Authentication"]
)
async def register(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(User).where(User.email == user.email)
    )

    existing = result.scalar_one_or_none()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    new_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        is_active=True,
    )

    db.add(new_user)

    await db.commit()

    await db.refresh(new_user)

    return new_user
@app.post(
    "/api/v1/auth/login",
    tags=["Authentication"],
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(User).where(User.email == form_data.username)
    )

    db_user = result.scalar_one_or_none()

    if (
        db_user is None
        or not verify_password(
            form_data.password,
            db_user.hashed_password,
        )
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }