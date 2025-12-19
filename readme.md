### All the validations must be implemented in the site backend.

#### User Registration API details

Must be in the /user-app/register endpoint

##### Contract [Request Body]

```json
{
  "name": "John Doe",
  "username": "johndoe@123",
  "password": "j0HN@xyz1",
  "favoriteFood": "Grilled Cheese Pizza"
}
```

###### Response Body

response status code: 200

```json
{
  "message": "User created successfully with username johndoe@123!"
}
```

#### User Registration Validation Requirements

- All the validations must be done after stripping (removing starting and ending whitespaces) the incoming parameter values if they're of string format.
- All the constraints in the provided SiteUser model must be validated while creating the user in signup page. e.g. `models.CharField(max_length=20)` means a max length of 20 must be checked in the validation layer. There can be more complex validations required based on the attribute type and constraints, need to implement all such scenarios.
- All attributes must have a None/blank check (after strip) unless mentioned as null=True or blank=True in the model.
- password must be a minimum of 8 characters, max of 20 characters, and cannot be same as username (case sensitive). Password cannot start/end with empty spaces. It'll be stripped before checking for constraints and hashing it. That's the exact requirement, it should be followed strictly.
- once a raw password string comes to the backend, it must be hashed using sha256 and then save to DB.
- If any of these validations are not satisfied, 4xx status code should be returned according to the HTTP practices, e.g. if name is blank, 400 bad request should be thrown, 409 for conflict etc.
