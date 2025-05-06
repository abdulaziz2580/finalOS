Project Description

This project provides a simple API to manage student information, including student ID, age, gender, study hours, social media hours, and other relevant details. It uses Flask to handle the API endpoints and PostgreSQL for data storage.

Features

Retrieve all student data.
Add a new student to the database.
Delete an existing student from the database.

Set up EC2 Instance:
Configure the security group to allow traffic on ports: 80, 22, 443, 5432, 8000, and all traffic. Set up RDS PostgreSQL:

Make sure the RDS instance allows all traffic from the EC2 instance (public access). SSH into EC2:

2.Run: ssh -i "C:\your_key_2_ec2.pem" ubuntu@<EC2_Public_IP>

3.Install dependencies:

sudo apt update
sudo apt install python3 python3-pip postgresql-client -y
4.Connect to the RDS instance using psql: psql -h <RDS_End_Point> -U <RDS_User> -d <RDS_Database_Name>

5.Your PostgreSQL table tbl_mahmud_data should look like this:
CREATE TABLE tbl_students (
    student_id VARCHAR PRIMARY KEY,
    age INT,
    gender VARCHAR,
    study_hours_per_day FLOAT,
    social_media_hours FLOAT,
    part_time_job VARCHAR,
    sleep_hours FLOAT,
    diet_quality VARCHAR,
    parental_education_level VARCHAR,
    internet_quality VARCHAR
);
6.INSERT INTO tbl_students (student_id, age, gender, study_hours_per_day, social_media_hours, part_time_job, sleep_hours, diet_quality, parental_education_level, internet_quality) VALUES
('S1000', 23, 'Female', 0.0, 1.2, 'No', 8.0, 'Fair', 'Master', 'Average'),
('S1001', 20, 'Female', 6.9, 2.8, 'No', 4.6, 'Good', 'High School', 'Average'),
-- Add more student records here

DELETE /api/students/<student_id>: Delete a student.
student_id: The ID of the student to delete.
Returns a JSON message indicating success or failure.

7.6.Create Project Directory and Flask Application: Create the project directory and Python file:

mkdir webb_abdulaziz
cd webb_abdulaziz
touch app.py
8.Install Python Dependencies: Install python3-venv (if not already installed)

cd final_project
sudo apt update
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate


9. run python app.py

