
# Exam Details
- [Exam checklist](#steps--testing)
- [Exam Day](#exam-details)

## Steps & Testing
### Auth (Log & Reg): 
1. Register Validation
   - [ ] Length for first_name, last_name, email, password length
   - [ ]  REGEX pattern for email 
   - [ ]  Is the email registered?
2. Successful register
   - [ ]  Store the user_id in session
   - [ ]  hash the pw before you save
3. Login Validation
   - [ ]  Check if the email exists
   - [ ]  Check if the form password match with the db password
4. Successful login 
   - [ ]  Store the user_id in session
5. More on session 
   - [ ]  Logout works
   - [ ]  Route protection on pages
   - [ ]  Welcome, Pepper works (Able to get the first_name)

### setup
1. Models
    - CRUD model with all the database keys
    - Include the attributes for classes association
2. Have another controller for the CRUD


### CRUD
1. Create 
   - [ ] Form is showing all the input
   - [ ] request.form is accurate
   - [ ] Validation works
   - [ ] Query works in MySQL
   - [ ] Save works with Foreign key
2. Dashboard (get_all_with_owner)
   - [ ] Query did LEFT JOIN 
   - [ ] Creating a list of Item with User instance (Logic after results) 
   - [ ] Table display the owner.username 
3. Details (get_one_with_owner)
   - [ ] Query did LEFT JOIN with WHERE users.id = %(id)s
   - [ ] Create the Item with User instance
   - [ ] Display is accurate
4. Edit
   - [ ] Similar to Details (Controller) & Create (template)
   - [ ] Edit page template - all pre-populated input
   - [ ] Edit process - Make sure the FK is in 
   - [ ] Make sure the query is correct
   - [ ] Successful update
   - [ ] (Optional) Validation
   - [ ] (Optional) Make sure logged_user is the owner user
5. Delete
   - [ ] Delete should work (either link / post form)
   - [ ] (Optional) Make sure logged_user is the owner user
6. Misc
   - [ ] Route protection on all routes
   - [ ] Welcome, Pepper on dashboard
   - [ ] 1:n is in ERD
   - [ ] Join table in queries
   - [ ] Class association is in dashboard & details
   - [ ] Conditional rendering on edit/delete link

## Requirements & Details
1. completed & submitted 90% of core assignments (14/15)
2. Finished at least 1 code review (Cannot be on the same day)
3. Offical exam day: Week 3 Day 3. (No algo on that day)
4. If you are taking the exam on other dates, you have to attend the algo session first. 
5. Last day of exam: Week 4 Day 3 (Next Wednesday)

### NO CHEATING 
1. Zero-tolerance in cheating. *Students who are found cheating will be expelled from the program immediately*
2. DO NOT find exam on Google/Github 
3. DO NOT use AI tools to complete the task (No Tabnine, Github copilot or ChatGPT)
4. DO NOT communicate with your cohort during the exam

### Available Resources
1. Your own code
2. Platform
3. StackOverflow /Google
4. my github

### Preparations
1. Having a cheatsheet (CRUD & query)
2. Having a log/reg setup before you get started (log/reg won't depend on other tables in most cases)
3. TIPS: DO NOT PRE-BUILD EVERYTHING BEFORE THE EXAM 

### During the exam
2. Exam code will be given in the preparation room
2. Stay in your own room on Zoom by yourself
3. If you want to ask for help/grading, send a message on our discord channel and tag both me and our TA. 

### Getting graded
1. Test your code & Upload to the platform first
2. Live grading based on the submitted file
3. Finished all Red belt features and get it graded first, then work on the black belt features. 

### To pass the exam
1. Full CRUD (Create, Read, Update, Delete)
2. One-to-many relationship with class association
3. Include route protection , Welcome Pepper & conditional rendering
4. Login & Registration
    ##### Red Belt: Uploading the complete project within 5 hours. 


### Black Belt: (Completing stretched goals to achieve mastery) 
1. Completing stretched goals successfully
2. More route protection
3. Advanced queries
4. n:m / multiple 1:n
5. More validation


