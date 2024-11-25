## STREAM
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

