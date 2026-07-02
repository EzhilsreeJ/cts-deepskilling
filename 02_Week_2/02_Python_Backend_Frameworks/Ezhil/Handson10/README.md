# Hands-On 10 - Microservices Architecture

## Service Decomposition

| Service | Responsibility | Endpoints | Database |
|----------|---------------|-----------|----------|
| Course Service | Manage Courses | /api/courses | course.db |
| Student Service | Manage Students & Enrollments | /api/students | student.db |
| Auth Service | Authentication | /api/auth | auth.db |
| Notification Service | Email Notifications | Internal | None |

## Microservices Communication

### Synchronous Communication

- Course Service communicates using HTTP.
- Student Service calls Course Service during enrollment.
- API Gateway routes incoming requests to the appropriate service.

### Asynchronous Communication

- Suitable for notifications, emails, and event processing.
- Uses message brokers such as RabbitMQ or Kafka.
- Improves scalability and reliability by decoupling services.

### Services

- Course Service (Port 5001)
- Student Service (Port 5002)
- API Gateway (Port 5000)