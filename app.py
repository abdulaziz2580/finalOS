from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database configuration
DB_HOST = 'db-abdulazizz.ct6ei6agkus4.ap-south-1.rds.amazonaws.com'  # Replace with your RDS endpoint
DB_NAME = 'postgres'
DB_USER = 'postgres'    # Replace with your RDS username
DB_PASS = 'postgres'  # Replace with your RDS password
DB_PORT = '5432'

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

@app.route('/api/students', methods=['GET'])
def get_student_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT student_id, age, gender, study_hours_per_day, social_media_hours, part_time_job, sleep_hours, diet_quality, parental_education_level, internet_quality FROM tbl_students")
    students = cur.fetchall()
    cur.close()
    conn.close()

    students_list = [{'student_id': student[0], 'age': student[1], 'gender': student[2],
                      'study_hours_per_day': float(student[3]), 'social_media_hours': float(student[4]),
                      'part_time_job': student[5], 'sleep_hours': float(student[6]), 'diet_quality': student[7],
                      'parental_education_level': student[8], 'internet_quality': student[9]} for student in students]
    return jsonify(students_list)

@app.route('/api/students', methods=['POST'])
def add_new_student():
    data = request.get_json()
    student_id = data.get('student_id')
    age = data.get('age')
    gender = data.get('gender')
    study_hours_per_day = data.get('study_hours_per_day')
    social_media_hours = data.get('social_media_hours')
    part_time_job = data.get('part_time_job')
    sleep_hours = data.get('sleep_hours')
    diet_quality = data.get('diet_quality')
    parental_education_level = data.get('parental_education_level')
    internet_quality = data.get('internet_quality')

    if not all([student_id, age, gender, study_hours_per_day, social_media_hours, sleep_hours, diet_quality, parental_education_level, internet_quality]):
        return jsonify({'message': 'Missing required fields'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO tbl_students (student_id, age, gender, study_hours_per_day, social_media_hours, part_time_job, sleep_hours, diet_quality, parental_education_level, internet_quality) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (student_id, age, gender, study_hours_per_day, social_media_hours, part_time_job, sleep_hours, diet_quality, parental_education_level, internet_quality))
        conn.commit()
        return jsonify({'message': f'Student with ID {student_id} added successfully'}), 201
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return jsonify({'message': f'Student with ID {student_id} already exists'}), 409
    except Exception as e:
        conn.rollback()
        return jsonify({'message': f'Error adding student: {str(e)}'}), 500
    finally:
        cur.close()
        conn.close()

@app.route('/api/students/<string:student_id>', methods=['DELETE'])
def delete_existing_student(student_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM tbl_students WHERE student_id = %s", (student_id,))
        if cur.rowcount > 0:
            conn.commit()
            return jsonify({'message': f'Student with ID {student_id} deleted successfully'}), 200
        else:
            return jsonify({'message': f'Student with ID {student_id} not found'}), 404
    except Exception as e:
        conn.rollback()
        return jsonify({'message': f'Error deleting student: {str(e)}'}), 500
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)