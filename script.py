import pymysql
from pymongo import MongoClient
from datetime import datetime

# MySQL database connection
mysql_conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Java@123',
    db='icad_online'
)

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['ai_icad']
streams_collection = mongo_db['streams']
courses_collection = mongo_db['courses']
students_collection = mongo_db['icad_student_mst']
topics_collection = mongo_db['topics']
subtopics_collection = mongo_db['icad_subtopic_mst']
concepts_collection = mongo_db['icad_concept_mster']
sub_concepts_collection = mongo_db['icad_sub_concept_mster']

# Function to handle datetime formatting
def handle_datetime(dt):
    return dt if isinstance(dt, datetime) else None

# Cache for stream_id and course_id mappings
stream_id_mapping = {}
course_id_mapping = {}
subtopic_id_mapping = {}
concept_id_mapping = {}

def migrate_streams(cursor):
    """Migrate streams from MySQL to MongoDB."""
    cursor.execute("SELECT * FROM icad_stream_mst")
    for row in cursor.fetchall():
        stream_document = {
            "stream_code": row["STREAM_ID"],
            "stream_name": row["STREAM_NAME"],
            "description": row["DESCRIPTION"],
            "sequence": row["SEQUENCE"],
            "status": row["STATUS"],
            "remark": row["REMARKS"],
            "deleted_at": None if row["IS_DELETED"] == 'NO' else datetime.now(),
            "created_at": handle_datetime(row["CREATED_ON"]),
            "last_modified": handle_datetime(row["LAST_MODIFIED"]),
        }
        result = streams_collection.insert_one(stream_document)
        stream_id_mapping[row["STREAM_ID"]] = result.inserted_id

def migrate_courses(cursor):
    """Migrate courses from MySQL to MongoDB."""
    cursor.execute("SELECT * FROM icad_course_mst")
    for row in cursor.fetchall():
        stream_id = stream_id_mapping.get(row["STREAM_ID"])
        if not stream_id:
            print(f"Stream ID {row['STREAM_ID']} not found. Skipping course ID {row['COURSE_ID']}.")
            continue

        course_document = {
            "course_code": row["COURSE_ID"],
            "stream_id": stream_id,
            "course_name": row["COURSE_NAME"],
            "total_marks": row["RT_CAT_EXAM_TOTAL_MARK"],
            "description": row["DESCRIPTION"],
            "status": row["STATUS"],
            "deleted_at": None if row["IS_DELETED"] == 'NO' else datetime.now(),
            "created_at": handle_datetime(row["CREATED_ON"]),
            "last_modified": handle_datetime(row["LAST_MODIFIED"]),
        }
        result = courses_collection.insert_one(course_document)
        course_id_mapping[row["COURSE_ID"]] = result.inserted_id

def migrate_topics(cursor):
    """Migrate topics from MySQL to MongoDB."""
    cursor.execute("SELECT * FROM icad_topic_mst")
    for row in cursor.fetchall():
        course_id = course_id_mapping.get(row["COURSE_ID"])
        if not course_id:
            print(f"Course ID {row['COURSE_ID']} not mapped. Skipping topic ID {row['TOPIC_ID']}.")
            continue

        topic_document = {
            "course_id": course_id,
            "topic_code": row["TOPIC_ID"],
            "topic_name": row["TOPIC_NAME"],
            "description": row["DESCRIPTION"],
            "sequence": row["SEQUENCE"],
            "lecture_count": row["LECTURE_COUNT"],
            "total_questions": row["TOTAL_QUESTION"],
            "total_subjective_questions": row["TOTAL_QUESTION_SUBJECTIVE"],
            "status": row["STATUS"],
            "remark": row["REMARKS"],
            "deleted_at": None if row["IS_DELETED"] == 'NO' else datetime.now(),
            "created_at": handle_datetime(row["CREATED_ON"]),
            "last_modified": handle_datetime(row["LAST_MODIFIED"]),
        }
        topics_collection.insert_one(topic_document)

def migrate_subtopics(cursor):
    """Migrate subtopics from MySQL to MongoDB."""
    cursor.execute("SELECT * FROM icad_subtopic_mst")
    for row in cursor.fetchall():
        course_id = course_id_mapping.get(row["COURSE_ID"])
        if not course_id:
            print(f"Course ID {row['COURSE_ID']} not mapped. Skipping subtopic ID {row['SUBTOPIC_ID']}.")
            continue

        subtopic_document = {
            "subtopic_id": row["SUBTOPIC_ID"],
            "course_id": course_id,
            "subject_id": row["SUBJECT_ID"],
            "topic_id": row["TOPIC_ID"],
            "subtopic_name": row["SUBTOPIC_NAME"],
            "sequence": row["SEQUENCE"],
            "total_question": row["TOTAL_QUESTION"],
            "total_question_subjective": row["TOTAL_QUESTION_SUBJECTIVE"],
            "status": row["STATUS"],
            "is_deleted": row["IS_DELETED"],
            "created_on": handle_datetime(row["CREATED_ON"]),
            "last_modified": handle_datetime(row["LAST_MODIFIED"]),
        }
        try:
            result = subtopics_collection.insert_one(subtopic_document)
            subtopic_id_mapping[row["SUBTOPIC_ID"]] = result.inserted_id
        except Exception as e:
            print(f"Failed to insert subtopic: {row['SUBTOPIC_ID']} - Error: {e}")

def migrate_concepts(cursor):
    """Migrate concepts from MySQL to MongoDB."""
    cursor.execute("SELECT * FROM icad_concept_mster")
    for row in cursor.fetchall():
        subtopic_id = subtopic_id_mapping.get(row["SUB_TOPIC_ID"])
        if not subtopic_id:
            print(f"Subtopic ID {row['SUB_TOPIC_ID']} not mapped. Skipping concept ID {row['ID']}.")
            continue

        concept_document = {
            "id": row["ID"],
            "concept_name": row["CONCEPT_NAME"],
            "concept_display_name": row["CONCEPT_DISPLAY_NAME"],
            "sub_topic_id": subtopic_id,
            "is_deleted": row["IS_DELETED"],
            "status": row["STATUS"],
            "created_at": handle_datetime(row["CREATED_AT"]),
            "updated_at": handle_datetime(row["UPDATED_AT"]),
        }
        try:
            result = concepts_collection.insert_one(concept_document)
            concept_id_mapping[row["ID"]] = result.inserted_id
        except Exception as e:
            print(f"Failed to insert concept: {row['ID']} - Error: {e}")

def migrate_sub_concepts(cursor):
    """Migrate sub concepts from MySQL to MongoDB."""
    cursor.execute("SELECT * FROM icad_sub_concept_mster")
    for row in cursor.fetchall():
        concept_id = concept_id_mapping.get(row["CONCEPT_ID"])
        if not concept_id:
            print(f"Concept ID {row['CONCEPT_ID']} not mapped. Skipping sub concept ID {row['ID']}.")
            continue

        sub_concept_document = {
            "id": row["ID"],
            "concept_id": concept_id,
            "sub_concept_name": row["SUB_CONCEPT_NAME"],
            "sub_concept_display_name": row["SUB_CONCEPT_DISPLAY_NAME"],
            "is_deleted": row["IS_DELETED"],
            "status": row["STATUS"],
            "created_at": handle_datetime(row["CREATED_AT"]),
            "updated_at": handle_datetime(row["UPDATED_AT"]),
        }
        try:
            sub_concepts_collection.insert_one(sub_concept_document)
        except Exception as e:
            print(f"Failed to insert sub concept: {row['ID']} - Error: {e}")


def migrate_students(cursor):
    """Migrate students from MySQL to MongoDB."""
    cursor.execute("SELECT * FROM icad_student_mst")
    
    for row in cursor.fetchall():
        print("COURSE ID===", row["COURSE_ID"])
        course_id = course_id_mapping.get(row["COURSE_ID"])
        admission_course_id = course_id_mapping.get(row["COURSE_ID"])
        if not course_id:
            print(f"Course ID {row['COURSE_ID']} not mapped. Defaulting to None.")
        if not admission_course_id:
            print(f"Admission Course ID {row['COURSE_ID']} not mapped. Defaulting to None.")

        document = {
            "student_id": row["STUDENT_ID"],
            "personal_details": {
                "first_name": row["FIRST_NAME"],
                "middle_name": row["MIDDLE_NAME"],
                "last_name": row["LAST_NAME"],
                "dob": handle_datetime(row["DOB"]),
                "gender_id": row["GENDER_ID"],
                "contact": row["CONTACT"],
                "email": row["EMAIL"],
                "address": {
                    "street": row["ADDRESS"],
                    "landmark": row["LANDMARK"],
                    "city": row["CITY"],
                    "district": row["DISTRICT"],
                    "state": row["STATE"],
                    "pincode": row["PINCODE"]
                },
                "aadhar_no": row["AADHAR_NO"]
            },
            "academic_details": {
                "course_id": course_id,
                "admission_course_id": admission_course_id,
                "center_id": row["CENTER_ID"],
                "batch_id": row["BATCH_ID"],
                "group_id": row["GROUP_ID"],
                "batch_allocation_date": handle_datetime(row["BATCH_ALLOCATION_DATE"]),
                "registration_number": row["REGISTRATION_NUMBER"],
                "roll_number": row["ROLL_NUMBER"]
            },
            "school_details": {
                "school_name": row["SCHOOL_NAME"],
                "school_address": row["SCHOOL_ADDRESS"],
                "medium_of_study": row["MEDIUM_OF_STUDY"],
                "education_board_name": row["EDUCATION_BOARD_NAME"],
                "prefer_of_11std_board": row["PREFER_OF_11STD_BOARD"]
            },
            "fees_details": {
                "total_fees_after_scholarship": row["TOTAL_FEES_AFTER_SCHOLARSHIP"],
                "scholarship_discount_id": row["SCHOLARSHIP_DISCOUNT_ID"],
                "installments": [
                    {
                        "amount": row.get(f"INSTALLMENT_{i}_AMOUNT"),
                        "paid_status": row.get(f"INSTALLMENT_{i}_AMOUNT_PAID_STATUS"),
                        "paid_date": handle_datetime(row.get(f"INSTALLMENT_{i}_AMOUNT_PAID_DATE"))
                    }
                    for i in range(1, 6)
                ],
                "total_amount_paid": row["TOTAL_AMOUNT_PAID"],
                "total_amount_balance": row["TOTAL_AMOUNT_BALANCE"]
            },
            "parent_details": {
                "father": {
                    "first_name": row["FATHER_PARENT_FIRST_NAME"],
                    "middle_name": row["FATHER_PARENT_MIDDLE_NAME"],
                    "last_name": row["FATHER_PARENT_LAST_NAME"],
                    "contact": row["FATHER_PARENT_CONTACT"],
                    "email": row["FATHER_PARENT_EMAIL"],
                    "age": row["FATHER_PARENT_AGE"],
                    "occupation": row["FATHER_PARENT_OCCUPATION"]
                },
                "mother": {
                    "first_name": row["MOTHER_FIRST_NAME"],
                    "middle_name": row["MOTHER_MIDDLE_NAME"],
                    "last_name": row["MOTHER_LAST_NAME"],
                    "contact": row["MOTHER_CONTACT"],
                    "email": row["MOTHER_EMAIL"],
                    "age": row["MOTHER_AGE"],
                    "occupation": row["MOTHER_OCCUPATION"]
                },
                "parents_total_annual_income": row["PARENTS_TOTAL_ANNUAL_INCOME"]
            },
            "registration_details": {
                "registration_date": handle_datetime(row["STUDENT_REGISTRATION_DATE"]),
                "approval_status": row["APPROVAL_STATUS"],
                "approval_date": handle_datetime(row["APPROVAL_DATE"]),
                "approved_by": row["APPROVED_BY"]
            },
            "status_details": {
                "is_activated": row["IS_ACTIVATED"],
                "is_suspended": row["IS_SUSPENDED"],
                "suspended_on": handle_datetime(row["SUSPENDED_ON"]),
                "status": row["STATUS"]
            },
            "meta": {
                "created_on": handle_datetime(row["CREATED_ON"]),
                "last_modified": handle_datetime(row["LAST_MODIFIED"]),
                "is_deleted": row["IS_DELETED"] == 'YES'
            }
        }
        students_collection.insert_one(document)

try:
    with mysql_conn.cursor(pymysql.cursors.DictCursor) as cursor:
        migrate_streams(cursor)
        migrate_courses(cursor)
        migrate_topics(cursor)
        migrate_subtopics(cursor)
        migrate_concepts(cursor)
        migrate_sub_concepts(cursor)
        migrate_students(cursor)
finally:
    mysql_conn.close()
    mongo_client.close()
