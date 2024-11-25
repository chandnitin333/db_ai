## STREAM
    db.streams.createIndex({ stream_code: 1 }, { unique: true });

    db.createCollection("streams", {
      validator: {
        $jsonSchema: {
          bsonType: "object",
          required: ["stream_code", "stream_name", "created_at", "last_modified"],
          properties: {
            stream_code: { bsonType: "string", description: "Must be a string and is required." },
            stream_name: { bsonType: "string", description: "Must be a string and is required." },
            description: { bsonType: "string", description: "Optional description of the stream." },
            sequence: { bsonType: "number", description: "Optional sequence number." },
            status: { bsonType: "string", description: "Must be a string indicating status." },
            remark: { bsonType: "string", description: "Optional remarks field." },
            deleted_at: { bsonType: ["null", "date"], description: "Timestamp or null if not deleted." },
            created_at: { bsonType: "date", description: "Required creation timestamp." },
            last_modified: { bsonType: "date", description: "Required last modification timestamp." }
          }
        }
      }
    });

## COURSE
    db.courses.createIndex({ course_code: 1 }, { unique: true });
    db.courses.createIndex({ stream_id: 1 });

    
    db.createCollection("courses", {
      validator: {
        $jsonSchema: {
          bsonType: "object",
          required: ["course_code", "stream_id", "course_name", "total_marks", "created_at", "last_modified"],
          properties: {
            course_code: { bsonType: "string", description: "Must be a string and is required." },
            stream_id: { bsonType: "objectId", description: "Must be an ObjectId referring to the stream." },
            course_name: { bsonType: "string", description: "Must be a string and is required." },
            total_marks: { bsonType: "number", description: "Must be a number representing total marks." },
            description: { bsonType: "string", description: "Optional description of the course." },
            status: { bsonType: "string", description: "Must be a string indicating the status of the course." },
            deleted_at: { bsonType: ["null", "date"], description: "Timestamp or null if not deleted." },
            created_at: { bsonType: "date", description: "Required creation timestamp." },
            last_modified: { bsonType: "date", description: "Required last modification timestamp." }
          }
        }
      }
    });

## STUDENT
    db.courses.createIndex({ course_code: 1 }, { unique: true });
    db.courses.createIndex({ stream_id: 1 });
    db.icad_student_mst.createIndex({ student_id: 1 }, { unique: true });

    {
      "student_id": "number",                   // Primary key
      "personal_details": {
        "first_name": "string",
        "middle_name": "string|null",
        "last_name": "string",
        "dob": "ISODate|null",
        "gender_id": "number|null",
        "contact": "string|null",
        "email": "string|null",
        "address": {
          "street": "string|null",
          "landmark": "string|null",
          "city": "string|null",
          "district": "string|null",
          "state": "string|null",
          "pincode": "string|null"
        },
        "aadhar_no": "string|null"
      },
      "academic_details": {
        "course_id": "number",
        "admission_course_id": "number",
        "center_id": "number",
        "batch_id": "number",
        "group_id": "number|null",
        "batch_allocation_date": "ISODate|null",
        "registration_number": "string|null",
        "roll_number": "string"
      },
      "school_details": {
        "school_name": "string|null",
        "school_address": "string|null",
        "medium_of_study": "string|null",
        "education_board_name": "string|null",
        "prefer_of_11std_board": "string|null"
      },
      "fees_details": {
        "total_fees_after_scholarship": "string|null",
        "scholarship_discount_id": "number|null",
        "installments": [
          {
            "amount": "string",
            "paid_status": "string",
            "paid_date": "ISODate|null"
          }
        ],
        "total_amount_paid": "string|null",
        "total_amount_balance": "string|null"
      },
      "parent_details": {
        "father": {
          "first_name": "string|null",
          "middle_name": "string|null",
          "last_name": "string|null",
          "contact": "string|null",
          "email": "string|null",
          "age": "string|null",
          "occupation": "string|null"
        },
        "mother": {
          "first_name": "string|null",
          "middle_name": "string|null",
          "last_name": "string|null",
          "contact": "string|null",
          "email": "string|null",
          "age": "string|null",
          "occupation": "string|null"
        },
        "parents_total_annual_income": "string|null"
      },
      "registration_details": {
        "registration_date": "ISODate|null",
        "approval_status": "string",
        "approval_date": "ISODate|null",
        "approved_by": "string|null"
      },
      "status_details": {
        "is_activated": "string",
        "is_suspended": "string",
        "suspended_on": "ISODate|null",
        "status": "string"
      },
      "meta": {
        "created_on": "ISODate",
        "last_modified": "ISODate",
        "is_deleted": "boolean"
      }
    }



