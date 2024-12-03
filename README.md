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


## BATCH MST

    db.createCollection("icad_batches_mst", {
      validator: {
        $jsonSchema: {
          bsonType: "object",
          required: ["batch_id", "state", "district", "city", "center_id", "course_id", "batch_name", "batch_type", "description", "sequence", "status", "created_on", "last_modified"],
          properties: {
            batch_id: { bsonType: "int", description: "Must be an integer and is required." },
            state: {
              bsonType: "object",
              required: ["id", "name"],
              properties: {
                id: { bsonType: "int", description: "Must be an integer and is required." },
                name: { bsonType: "string", description: "Must be a string and is required." }
              }
            },
            district: {
              bsonType: "object",
              required: ["id", "name"],
              properties: {
                id: { bsonType: "int", description: "Must be an integer and is required." },
                name: { bsonType: "string", description: "Must be a string and is required." }
              }
            },
            city: {
              bsonType: "object",
              required: ["id", "name"],
              properties: {
                id: { bsonType: "int", description: "Must be an integer and is required." },
                name: { bsonType: "string", description: "Must be a string and is required." }
              }
            },
            center_id: { bsonType: "int", description: "Must be an integer and is required." },
            course_id: { bsonType: "int", description: "Must be an integer and is required." },
            batch_name: { bsonType: "string", description: "Must be a string and is required." },
            target_year: { bsonType: "int", description: "Must be an integer." },
            batch_type: { bsonType: "string", enum: ["REG", "INT", "REP", "FON"], description: "Must be a string and one of the predefined values." },
            description: { bsonType: "string", description: "Must be a string and is required." },
            sequence: { bsonType: "int", description: "Must be an integer and is required." },
            status: { bsonType: "string", enum: ["ENABLE", "DISABLE"], description: "Must be a string and one of the predefined values." },
            remarks: { bsonType: "string", description: "Must be a string." },
            created_on: { bsonType: "date", description: "Must be a date and is required." },
            last_modified: { bsonType: "date", description: "Must be a date and is required." },
            is_deleted: { bsonType: "bool", description: "Must be a boolean." }
          }
        }
      },
      autoIndexId: true
    });

## CENTER MST
        db.createCollection("icad_center_mst", {
          validator: {
            $jsonSchema: {
              bsonType: "object",
              required: ["state_id", "district_id", "city_id", "name", "shortname", "center_address", "center_contact", "sequence", "status", "remarks", "created_on", "last_modified"],
              properties: {
                state_id: { bsonType: "int", description: "Must be an integer and is required." },
                district_id: { bsonType: "int", description: "Must be an integer and is required." },
                city_id: { bsonType: "int", description: "Must be an integer and is required." },
                center_id: { bsonType: "int", description: "Must be an integer and is auto-incremented." },
                name: { bsonType: "string", description: "Must be a string and is required." },
                shortname: { bsonType: "string", description: "Must be a string and is required." },
                center_address: { bsonType: "string", description: "Must be a string and is required." },
                center_contact: { bsonType: "string", description: "Must be a string and is required." },
                sequence: { bsonType: "int", description: "Must be an integer and is required." },
                status: { bsonType: "string", enum: ["ENABLE", "DISABLE"], description: "Must be a string and one of the predefined values." },
                remarks: { bsonType: "string", description: "Must be a string and is required." },
                is_deleted: { bsonType: "bool", description: "Must be a boolean." },
                created_on: { bsonType: "date", description: "Must be a date and is required." },
                last_modified: { bsonType: "date", description: "Must be a date and is required." }
              }
            }
          },
          autoIndexId: true
        });
## TOPIC MST
    
    db.createCollection("icad_topic_mst", {
      validator: {
        $jsonSchema: {
          bsonType: "object",
          required: [
            "course_id", "oldCourseID", "subject_id", "topic_id", "oldTopicID", 
            "topic_name", "description", "sequence", "lecture_count", 
            "total_question", "total_question_subjective", "status", 
            "remarks", "created_on", "last_modified"
          ],
          properties: {
            course_id: { bsonType: "int", description: "Must be an integer and is required." },
            oldCourseID: { bsonType: "int", description: "Must be an integer and is required." },
            subject_id: { bsonType: "int", description: "Must be an integer and is required." },
            topic_id: { bsonType: "int", description: "Must be an integer and is auto-incremented." },
            oldTopicID: { bsonType: "int", description: "Must be an integer and is required." },
            topic_name: { bsonType: "string", description: "Must be a string and is required." },
            description: { bsonType: "string", description: "Must be a string and is required." },
            sequence: { bsonType: "string", description: "Must be a string and is required." },
            lecture_count: { bsonType: "int", description: "Must be an integer and is required." },
            total_question: { bsonType: "int", description: "Must be an integer and is required." },
            total_question_subjective: { bsonType: "int", description: "Must be an integer and is required." },
            status: { bsonType: "string", enum: ["ENABLE", "DISABLE"], description: "Must be a string and one of the predefined values." },
            remarks: { bsonType: "string", description: "Must be a string and is required." },
            is_deleted: { bsonType: "bool", description: "Must be a boolean." },
            created_on: { bsonType: "date", description: "Must be a date and is required." },
            last_modified: { bsonType: "date", description: "Must be a date and is required." }
          }
        }
      },
      autoIndexId: true
    });
    
    // Ensure unique indexes
    db.icad_topic_mst.createIndex({ course_id: 1, subject_id: 1, topic_id: 1 }, { unique: true });
    db.icad_topic_mst.createIndex({ course_id: 1, subject_id: 1, topic_id: 1, topic_name: 1 }, { unique: true });



## SUb TOPIC MST

        db.createCollection("icad_subtopic_mst", {
          validator: {
            $jsonSchema: {
              bsonType: "object",
              required: [
                "subtopic_id", "course_id", "subject_id", "topic_id", "subtopic_name",
                "total_question", "total_question_subjective", "status", "is_deleted",
                "created_on", "last_modified"
              ],
              properties: {
                subtopic_id: { bsonType: "int", description: "Must be an integer and is auto-incremented." },
                course_id: { bsonType: "int", description: "Must be an integer and is required." },
                subject_id: { bsonType: "int", description: "Must be an integer and is required." },
                topic_id: { bsonType: "int", description: "Must be an integer and is required." },
                subtopic_name: { bsonType: "string", description: "Must be a string and is required." },
                sequence: { bsonType: "int", description: "Must be an integer." },
                total_question: { bsonType: "int", description: "Must be an integer and is required." },
                total_question_subjective: { bsonType: "string", description: "Must be a string and is required." },
                status: { bsonType: "string", enum: ["ENABLE", "DISABLE"], description: "Must be a string and one of the predefined values." },
                is_deleted: { bsonType: "string", enum: ["YES", "NO"], description: "Must be a string and one of the predefined values." },
                created_on: { bsonType: "date", description: "Must be a date and is required." },
                last_modified: { bsonType: "date", description: "Must be a date and is required." }
              }
            }
          },
          autoIndexId: true
        });
        
        // Ensure unique indexes
        db.icad_subtopic_mst.createIndex({ course_id: 1, subject_id: 1, topic_id: 1, subtopic_id: 1 }, { unique: true });


## CONCEPT MST

    db.createCollection("icad_concept_mster", {
          validator: {
            $jsonSchema: {
              bsonType: "object",
              required: ["id", "concept_name", "concept_display_name", "sub_topic_id", "is_deleted", "status", "created_at", "updated_at"],
              properties: {
                id: { bsonType: "int", description: "Must be an integer and is auto-incremented." },
                concept_name: { bsonType: "string", description: "Must be a string and is required." },
                concept_display_name: { bsonType: "string", description: "Must be a string and is required." },
                sub_topic_id: { bsonType: "int", description: "Must be an integer and is required." },
                is_deleted: { bsonType: "int", description: "Must be an integer and is required." },
                status: { bsonType: "int", description: "Must be an integer and is required." },
                created_at: { bsonType: "date", description: "Must be a date and is required." },
                updated_at: { bsonType: "date", description: "Must be a date and is required." }
              }
            }
          },
          autoIndexId: true
        });
        
        // Ensure unique indexes
        db.icad_concept_mster.createIndex({ id: 1, sub_topic_id: 1 }, { unique: true });


## SUB CONCEPT MST

        db.createCollection("icad_sub_concept_mster", {
          validator: {
            $jsonSchema: {
              bsonType: "object",
              required: ["id", "concept_id", "sub_concept_name", "sub_concept_display_name", "is_deleted", "status", "created_at", "updated_at"],
              properties: {
                id: { bsonType: "int", description: "Must be an integer and is auto-incremented." },
                concept_id: { bsonType: "int", description: "Must be an integer and is required." },
                sub_concept_name: { bsonType: "string", description: "Must be a string and is required." },
                sub_concept_display_name: { bsonType: "string", description: "Must be a string and is required." },
                is_deleted: { bsonType: "int", description: "Must be an integer and is required." },
                status: { bsonType: "int", description: "Must be an integer and is required." },
                created_at: { bsonType: "date", description: "Must be a date and is required." },
                updated_at: { bsonType: "date", description: "Must be a date and is required." }
              }
            }
          },
          autoIndexId: true
        });

        db.icad_sub_concept_mster.createIndex({ id: 1, concept_id: 1 }, { unique: true });
        
## QUESTION MST

        db.createCollection("icad_question_mst", {
          validator: {
            $jsonSchema: {
              bsonType: "object",
              required: [
                "question_id", "question_dtl", "answer_option_6", 
                "answer_option_7", "answer_option_8", "status", "is_canceled", "is_deleted"
              ],
              properties: {
                question_id: { bsonType: "int", description: "Must be an integer and is auto-incremented." },
                bulk_question_id: { bsonType: "int", description: "Must be an integer." },
                course: { 
                  bsonType: "object", 
                  required: ["id", "name"], 
                  properties: {
                    id: { bsonType: "int", description: "Must be an integer." },
                    name: { bsonType: "string", description: "Must be a string." }
                  },
                  description: "Contains course ID and name."
                },
                exam_type: { 
                  bsonType: "object", 
                  required: ["id", "name"], 
                  properties: {
                    id: { bsonType: "int", description: "Must be an integer." },
                    name: { bsonType: "string", description: "Must be a string." }
                  },
                  description: "Contains exam type ID and name."
                },
                is_partial: { bsonType: "string", enum: ["YES", "NO"], description: "Must be a string and one of the predefined values." },
                exam: { 
                  bsonType: "object", 
                  required: ["id", "name"], 
                  properties: {
                    id: { bsonType: "int", description: "Must be an integer." },
                    name: { bsonType: "string", description: "Must be a string." }
                  },
                  description: "Contains exam ID and name."
                },
                subject: { 
                  bsonType: "object", 
                  required: ["id", "name"], 
                  properties: {
                    id: { bsonType: "int", description: "Must be an integer." },
                    name: { bsonType: "string", description: "Must be a string." }
                  },
                  description: "Contains subject ID and name."
                },
                exam_subject_section_id: { bsonType: "int", description: "Must be an integer." },
                topic: { 
                  bsonType: "object", 
                  required: ["id", "name"], 
                  properties: {
                    id: { bsonType: "int", description: "Must be an integer." },
                    name: { bsonType: "string", description: "Must be a string." }
                  },
                  description: "Contains topic ID and name."
                },
                step_id: { bsonType: "int", description: "Must be an integer." },
                lecture_id: { bsonType: "int", description: "Must be an integer." },
                questions_type_id: { bsonType: "int", description: "Must be an integer." },
                exam_marks_dtl_id: { bsonType: "int", description: "Must be an integer." },
                question_dtl: { bsonType: "string", description: "Must be a string and is required." },
                number_of_options: { bsonType: "string", description: "Must be a string." },
                answer_option_1: { bsonType: "string", description: "Must be a string." },
                answer_option_2: { bsonType: "string", description: "Must be a string." },
                answer_option_3: { bsonType: "string", description: "Must be a string." },
                answer_option_4: { bsonType: "string", description: "Must be a string." },
                answer_option_5: { bsonType: "string", description: "Must be a string." },
                answer_option_6: { bsonType: "string", description: "Must be a string and is required." },
                answer_option_7: { bsonType: "string", description: "Must be a string and is required." },
                answer_option_8: { bsonType: "string", description: "Must be a string and is required." },
                correct_answer_option: { bsonType: "string", description: "Must be a string." },
                correct_answer_multiple: { bsonType: "string", description: "Must be a string." },
                correct_answer_text_from: { bsonType: "string", description: "Must be a string." },
                correct_answer_text_to: { bsonType: "string", description: "Must be a string." },
                solution: { bsonType: "string", description: "Must be a string." },
                hint: { bsonType: "string", description: "Must be a string." },
                status: { bsonType: "string", enum: ["ENABLE", "DISABLE"], description: "Must be a string and one of the predefined values." },
                is_canceled: { bsonType: "string", enum: ["YES", "NO"], description: "Must be a string and one of the predefined values." },
                concept_id: { bsonType: "int", description: "Must be an integer." },
                sub_concept_id: { bsonType: "int", description: "Must be an integer." },
                source_question: { bsonType: "string", description: "Must be a string." },
                remarks: { bsonType: "string", description: "Must be a string." },
                is_deleted: { bsonType: "string", enum: ["YES", "NO"], description: "Must be a string and one of the predefined values." },
                created_on: { bsonType: "date", description: "Must be a date." },
                last_modified: { bsonType: "date", description: "Must be a date." },
                bm_old: { bsonType: "string", description: "Must be a string." }
              }
            }
          },
          autoIndexId: true
        });

        db.icad_question_mst.createIndex({ question_id: 1 }, { unique: true });
        db.icad_question_mst.createIndex({ question_id: 1, "course.id": 1, "topic.id": 1, lecture_id: 1 }, { unique: true });
        db.icad_question_mst.createIndex({ question_id: 1, "course.id": 1, "topic.id": 1, lecture_id: 1, step_id: 1 }, { unique: true });
        db.icad_question_mst.createIndex({ "course.id": 1, "subject.id": 1, "topic.id": 1, exam_type_id: 1, question_id: 1 }, { unique: true });
        db.icad_question_mst.createIndex({ exam_id: 1, exam_type_id: 1, exam_subject_section_id: 1, question_id: 1 }, { unique: true });
        db.icad_question_mst.createIndex({ exam_type_id: 1, is_deleted: 1 });








