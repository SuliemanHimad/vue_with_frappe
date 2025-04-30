import frappe
from frappe import auth


@frappe.whitelist(allow_guest=True)
def login(email, password):
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(email, password)
        login_manager.post_login()
   
    
        api_generate = generateKeys(frappe.session.user)
        user = frappe.get_doc("User", frappe.session.user)

        frappe.response["message"] = {
            "success_key": 1,
            "message": "Logged In",
            "sid": frappe.session.sid,
            "api_key": user.api_key,
            "api_secret": api_generate,
            "userName": user.username,
            "userEmail": user.email
        }
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["Message"] ={
            "success_key": 0,
            "message": "Authentication Error"
        }
        return
def generateKeys(user):
    userDetails = frappe.get_doc("User", user)
    api_secret = frappe.generate_hash(length=15)
   
    if not userDetails.api_key:
        api_key = frappe.generate_hash(length=15)
        userDetails.api_key = api_key
    userDetails.api_secret = api_secret
    userDetails.save()
    return api_secret 

@frappe.whitelist(allow_guest=True)
def register_student(std_name):
    try:
        if not std_name:
            frappe.response["message"] = {
                "success_key": 0,
                "message": "Student name is required,and It Must Provided."
            }
            return
        # Check if the student already exists
        existing_student = frappe.get_all("Students", filters={"student_name": std_name})
        if existing_student:
            frappe.response["message"] = {
                "success_key": 0,
                "message": "Student already exists"
            }
            return
        # Create a new student document
        student = frappe.get_doc({
            "doctype": "Students",
            "student_name": std_name
        })
        student.insert()
        frappe.db.commit()
        frappe.response["message"] = {
            "success_key": 1,
            "message": "Student Registered"
        }
    except Exception as e:
        frappe.response["message"] = {
            "success_key": 0,
            "message": str(e)
        }