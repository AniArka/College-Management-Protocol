import pymongo


# Admin Login database connection
def admin_login_db(enrollment_no,username,password):
    client = pymongo.MongoClient("mongodb+srv://sambhranta1123:SbGgIK3dZBn9uc2r@cluster0.jjcc5or.mongodb.net/")
    # Acessing project Database
    db = client['project']
    # Acessing creators/admins Collection
    collection = db.creators
    admins = collection.find_one({"username": username , "enrollment_no": enrollment_no , "password": password})
    if admins == None:
        return 0
    else:
        return 1
    

# Teacher Login database connection
def teacher_login_db(enrollment_no,username,password):
    client = pymongo.MongoClient("mongodb+srv://sambhranta1123:SbGgIK3dZBn9uc2r@cluster0.jjcc5or.mongodb.net/")
    # Acessing project Database
    db = client['project']
    # Acessing creators/admins Collection
    collection = db.teachers
    teachers = collection.find_one({"username": username , "enrollment_no": enrollment_no , "password": password})
    if teachers == None:
        return 0
    else:
        return 1
    
# Student Login database connection
def student_login_db(enrollment_no,username,password):
    client = pymongo.MongoClient("mongodb+srv://sambhranta1123:SbGgIK3dZBn9uc2r@cluster0.jjcc5or.mongodb.net/")
    # Acessing project Database
    db = client['project']
    # Acessing creators/admins Collection
    collection = db.students
    students = collection.find_one({"username": username , "enrollment_no": enrollment_no , "password": password})
    if students == None:
        return 0
    else:
        return 1

def test(username):
    client = pymongo.MongoClient("mongodb+srv://sambhranta1123:SbGgIK3dZBn9uc2r@cluster0.jjcc5or.mongodb.net/")
    db = client['project']  
    users_collection = db['creators']
    admin_details = users_collection.find_one({'username': username})
    return admin_details

def count_students():
    client = pymongo.MongoClient("mongodb+srv://sambhranta1123:SbGgIK3dZBn9uc2r@cluster0.jjcc5or.mongodb.net/")
    db = client['project']  
    students_collection = db['students']
    total_student_count = students_collection.count_documents({})
    return total_student_count

def count_teachers():
    client = pymongo.MongoClient("mongodb+srv://sambhranta1123:SbGgIK3dZBn9uc2r@cluster0.jjcc5or.mongodb.net/")
    db = client['project']  
    teachers_collection = db['teachers']
    total_teachers_count = teachers_collection.count_documents({})
    return total_teachers_count


# Edited start by satyadeep at 3/6/24

# Add student database connection
def add_student_db(enrollment_no,username,password,email,branch,year,gender,phone,dob,parent_name,parent_no,address,profile_pic_location):
    client = pymongo.MongoClient("mongodb+srv://sambhranta1123:SbGgIK3dZBn9uc2r@cluster0.jjcc5or.mongodb.net/")
    # Acessing project Database
    db = client['project']
    # Acessing students Collection
    collection = db.students
    #Checking if enrollment no. is already present in DB
    students = collection.find_one({"enrollment_no": enrollment_no})
    
    if students == None:
        # Adding students record
        student_info = {
            "enrollment_no" : enrollment_no ,
            "password" : password ,
            "username" : username ,
            "email" : email ,
            "branch" : branch ,
            "academic_year" : int(year) ,
            "gender" : gender ,
            "phone_no" : phone ,
            "dob" : dob ,
            "parent_name" : parent_name ,
            "parent_no" : parent_no ,
            "current_address" : address ,
            "profile_pic" : profile_pic_location
        }
        student_id = collection.insert_one(student_info).inserted_id
        return 1
    else:
        return 0


# Remove Student from database connection
def remove_student_db(enrollment_no):
    client = pymongo.MongoClient("mongodb+srv://sambhranta1123:SbGgIK3dZBn9uc2r@cluster0.jjcc5or.mongodb.net/")
    # Acessing project Database
    db = client['project']
    # Acessing students Collection
    collection = db.students
    students = collection.find_one({"enrollment_no": enrollment_no})
    if students == None:
        return 0
    else:
        x = students.get('profile_pic')
        r = collection.delete_one({"enrollment_no": enrollment_no})
        return x

# Edited end by satyadeep at 3/6/24
