# API Usage Examples with Route Protection

## Overview
This document shows how to use the API endpoints with the new authentication decorators.

## Authentication Decorators

### @admin_required
- Requires admin role (role_id = 1)
- Expects `admin_user_id` in request data
- Returns 403 if not admin or missing admin_user_id

### @user_required  
- Requires any authenticated user
- Expects `user_id` in request data
- Returns 403 if user not found or missing user_id

### @optional_auth
- Optionally checks authentication
- If `user_id` provided, validates it
- Sets request context with user info if authenticated

## Vacation Routes

### Create Vacation (Admin Only)
```bash
POST /api/vacations
Content-Type: application/json

{
    "admin_user_id": 1,
    "country_id": 1,
    "vacation_description": "Amazing vacation to Greece",
    "vacation_start": "2024-06-01",
    "vacation_ends": "2024-06-07",
    "vacation_price": 1500.00
}
```

### Get All Vacations (Public)
```bash
GET /api/vacations
# No authentication required, but can include user_id for context
```

### Get All Vacations with User Context
```bash
GET /api/vacations?user_id=2
# Optional: provides user context for personalized responses
```

### Update Vacation (Admin Only)
```bash
PUT /api/vacations/update/1
Content-Type: application/json

{
    "admin_user_id": 1,
    "vacation_description": "Updated description",
    "vacation_price": 1600.00
}
```

### Delete Vacation (Admin Only)
```bash
DELETE /api/vacations/delete/1?admin_user_id=1
# Or with JSON body
```

```bash
DELETE /api/vacations/delete/1
Content-Type: application/json

{
    "admin_user_id": 1
}
```

## Country Routes

### Create Country (Admin Only)
```bash
POST /api/countries
Content-Type: application/json

{
    "admin_user_id": 1,
    "country_name": "Japan"
}
```

### Get All Countries (Public)
```bash
GET /api/countries
# No authentication required
```

### Update Country (Admin Only)
```bash
PUT /api/countries/1
Content-Type: application/json

{
    "admin_user_id": 1,
    "country_name": "Updated Japan"
}
```

### Delete Country (Admin Only)
```bash
DELETE /api/countries/1?admin_user_id=1
```

## Error Responses

### Missing Admin User ID
```json
{
    "Error": "Missing admin_user_id",
    "message": "Admin authentication required"
}
```

### Invalid Admin User ID
```json
{
    "Error": "Invalid admin_user_id format",
    "message": "Admin user ID must be a valid number"
}
```

### Admin User Not Found
```json
{
    "Error": "Admin user not found",
    "message": "Invalid admin user ID"
}
```

### Insufficient Permissions
```json
{
    "Error": "Insufficient permissions",
    "message": "Only administrators can perform this action"
}
```

## Frontend Integration

### JavaScript Example
```javascript
// Create vacation (admin only)
const createVacation = async (vacationData, adminUserId) => {
    const response = await fetch('/api/vacations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            ...vacationData,
            admin_user_id: adminUserId
        })
    });
    
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || 'Failed to create vacation');
    }
    
    return response.json();
};

// Get all vacations (public)
const getVacations = async (userId = null) => {
    const url = userId ? `/api/vacations?user_id=${userId}` : '/api/vacations';
    const response = await fetch(url);
    return response.json();
};

// Update vacation (admin only)
const updateVacation = async (vacationId, updateData, adminUserId) => {
    const response = await fetch(`/api/vacations/update/${vacationId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            ...updateData,
            admin_user_id: adminUserId
        })
    });
    
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || 'Failed to update vacation');
    }
    
    return response.json();
};
```

## Testing with curl

### Test Admin Access
```bash
# This should work (assuming user ID 1 is admin)
curl -X POST http://localhost:5000/api/vacations \
  -H "Content-Type: application/json" \
  -d '{"admin_user_id": 1, "country_id": 1, "vacation_description": "Test", "vacation_start": "2024-06-01", "vacation_ends": "2024-06-07", "vacation_price": 1000}'
```

### Test Missing Admin ID
```bash
# This should return 403 error
curl -X POST http://localhost:5000/api/vacations \
  -H "Content-Type: application/json" \
  -d '{"country_id": 1, "vacation_description": "Test", "vacation_start": "2024-06-01", "vacation_ends": "2024-06-07", "vacation_price": 1000}'
```

### Test Public Access
```bash
# This should work without authentication
curl -X GET http://localhost:5000/api/vacations
```
