import random
from faker import Faker
from django.core.management.base import BaseCommand
from employer.models import employer_table, company, Job, req_skill

fake = Faker()
possible_job_types = ['Full time', 'Part time',  'Internship', 'Hourly', 'Freelance']
possible_education_levels = ['High School', 'Diploma', 'Bachelor\'s Degree', 'Master\'s Degree', 'PhD']
possible_languages = ['English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Korean', 'Arabic', 'Russian', 'Portuguese', 'Italian', 'Dutch', 'Turkish', 'Polish', 'Swedish', 'Danish', 'Norwegian', 'Finnish', 'Greek', 'Czech', 'Hungarian', 'Romanian', 'Ukrainian', 'Bulgarian', 'Croatian', 'Serbian', 'Slovak', 'Slovenian', 'Lithuanian', 'Latvian', 'Estonian', 'Maltese', 'Icelandic', 'Faroese', 'Luxembourgish', 'Irish', 'Welsh', 'Scottish Gaelic', 'Breton', 'Basque', 'Catalan', 'Galician', 'Occitan', 'Albanian', 'Macedonian', 'Bosnian', 'Montenegrin', 'Azerbaijani', 'Georgian', 'Armenian', 'Kazakh', 'Uzbek', 'Turkmen', 'Kyrgyz']
possible_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Visakhapatnam', 'Indore', 'Thane', 'Bhopal', 'Patna', 'Vadodara', 'Ghaziabad', 'Ludhiana', 'Agra', 'Nashik', 'Faridabad', 'Meerut', 'Rajkot', 'Kalyan-Dombivali', 'Vasai-Virar', 'Varanasi', 'Srinagar', 'Aurangabad', 'Dhanbad', 'Amritsar', 'Navi Mumbai', 'Allahabad', 'Ranchi', 'Howrah', 'Coimbatore', 'Jabalpur', 'Gwalior', 'Vijayawada', 'Jodhpur', 'Madurai', 'Raipur', 'Kota', 'Chandigarh', 'Guwahati', 'Solapur', 'Hubli-Dharwad', 'Bareilly', 'Moradabad', 'Mysore', 'Gurgaon', 'Aligarh', 'Jalandhar', 'Tiruchirappalli', 'Bhubaneswar', 'Salem', 'Mira-Bhayandar', 'Warangal', 'Thiruvananthapuram', 'Guntur', 'Bhiwandi', 'Saharanpur', 'Gorakhpur', 'Bikaner', 'Amravati', 'Noida', 'Jamshedpur', 'Bhilai', 'Cuttack', 'Firozabad', 'Kochi', 'Nellore', 'Bhavnagar', 'Dehradun', 'Durgapur', 'Asansol', 'Rourkela', 'Nanded', 'Kolhapur', 'Ajmer', 'Akola', 'Gulbarga', 'Jamnagar', 'Ujjain', 'Loni', 'Siliguri', 'Jhansi', 'Ulhasnagar', 'Jammu', 'Sangli-Miraj & Kupwad', 'Mangalore', 'Erode', 'Belgaum']
possible_skill = ['Python', 'Java', 'C++', 'C#', 'JavaScript', 'Ruby', 'PHP', 'Swift', 'Kotlin', 'Rust', 'Go', 'TypeScript', 'HTML', 'CSS', 'SQL', 'NoSQL', 'React', 'Angular', 'Vue', 'Django', 'Flask', 'Spring', 'Laravel', 'Express', 'Ruby on Rails', 'Node.js', 'jQuery', 'Bootstrap', 'Tailwind CSS', 'Sass', 'Less', 'PostgreSQL', 'MySQL', 'MongoDB', 'SQLite', 'Firebase', 'Docker', 'Kubernetes', 'Jenkins', 'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Jira', 'Confluence', 'Slack', 'Trello', 'Asana', 'Notion', 'Figma', 'Sketch', 'Adobe XD', 'Photoshop', 'Illustrator', 'InDesign', 'Premiere Pro', 'After Effects', 'Final Cut Pro', 'Logic Pro', 'Ableton Live', 'Pro Tools', 'FL Studio', 'Audacity', 'GarageBand', 'Unity', 'Unreal Engine', 'Blender', 'Maya', '3ds Max', 'AutoCAD', 'SolidWorks', 'Figma', 'Sketch', 'Adobe XD', 'Photoshop', 'Illustrator', 'InDesign', 'Premiere Pro', 'After Effects', 'Final Cut Pro', 'Logic Pro', 'Ableton Live', 'Pro Tools', 'FL Studio', 'Audacity', 'GarageBand', 'Unity', 'Unreal Engine', 'Blender', 'Maya', '3ds Max', 'AutoCAD', 'SolidWorks', 'Figma', 'Sketch', 'Adobe XD', 'Photoshop', 'Illustrator', 'InDesign', 'Premiere Pro', 'After Effects', 'Final Cut Pro', 'Logic Pro', 'Ableton Live', 'Pro Tools', 'FL Studio', 'Audacity', 'GarageBand', 'Unity', 'Unreal Engine', 'Blender', 'Maya', '3ds Max', 'AutoCAD', 'SolidWorks', 'Figma', 'Sketch', 'Adobe XD', 'Photoshop', 'Illustrator', 'InDesign', 'Premiere Pro', 'After Effects', 'Final Cut Pro', 'Logic Pro', 'Ableton Live']

possible_job_title = ['Software Engineer', 'Data Scientist', 'Product Manager', 'UX Designer', 'UI Designer', 'Frontend Developer', 'Backend Developer', 'Full Stack Developer', 'Mobile Developer', 'Web Developer', 'DevOps Engineer', 'QA Engineer', 'Machine Learning Engineer', 'AI Engineer', 'Cybersecurity Analyst', 'Network Engineer', 'Database Administrator', 'Cloud Engineer', 'IT Support Specialist', 'Technical Writer', 'Technical Support Specialist', 'Systems Analyst', 'Business Analyst', 'Project Manager', 'Scrum Master', 'Product Owner', 'Data Analyst', 'Data Engineer', 'Data Architect', 'Data Warehouse Specialist', 'Data Governance Specialist', 'Data Quality Analyst', 'Data Security Analyst', 'Data Visualization Specialist', 'Database Developer', 'Database Manager', 'Database Specialist', 'Database Tester', 'Database Tuner', 'Database User Support Specialist', 'Database Administrator', 'Database Analyst', 'Database Architect', 'Database Consultant', 'Database Coordinator', 'Database Designer', 'Database Developer', 'Database Engineer', 'Database Manager', 'Database Modeler', 'Database Programmer', 'Database Specialist', 'Database Support Specialist', 'Database Tester', 'Database Tuner', 'Database User Support Specialist', 'Database Administrator', 'Database Analyst', 'Database Architect', 'Database Consultant', 'Database Coordinator', 'Database Designer', 'Database Developer', 'Database Engineer', 'Database Manager', 'Database Modeler', 'Database Programmer', 'Database Specialist', 'Database Support Specialist', 'Database Tester', 'Database Tuner', 'Database User Support Specialist', 'Database Administrator', 'Database Analyst', 'Database Architect', 'Database Consultant', 'Database Coordinator', 'Database Designer', 'Database Developer', 'Database Engineer', 'Database Manager', 'Database Modeler', 'Database Programmer', 'Database Specialist', 'Database Support Specialist', 'Database Tester', 'Database Tuner', 'Database User Support Specialist', 'Database Administrator', 'Database Analyst', 'Database Architect', 'Database Consultant', 'Database Coordinator', 'Database Designer', 'Database Developer', 'Database Engineer', 'Database Manager', 'Database Modeler', 'Database Programmer', 'Database Specialist', 'Database Support Specialist', 'Database Tester', 'Database Tuner', 'Database User Support Specialist', 'Database Administrator', 'Database Analyst', 'Database Architect', 'Database Consultant', 'Database Coordinator', 'Database Designer', 'Database Developer', 'Database Engineer', 'Database Manager', 'Database Modeler', 'Database Programmer', 'Database Specialist', 'Database Support Specialist', 'Database Tester', 'Database Tuner', 'Database User Support Specialist', 'Database Administrator', 'Database Analyst', 'Database Architect', 'Database Consultant', 'Database Coordinator', 'Database Designer', 'Database Developer', 'Database Engineer', 'Database Manager', 'Database Modeler', 'Database Programmer', 'Database Specialist', 'Database Support Specialist', 'Database Tester', 'Database Tuner', 'Database User Support Specialist', 'Database Administrator', 'Database Analyst', 'Database Architect', 'Database Consultant', 'Database Coordinator', 'Database Designer', 'Database Developer', 'Database Engineer', 'Database Manager', 'Database Modeler', 'Database Programmer', 'Database Specialist', 'Database Support Specialist', 'Database Tester', 'Database Tuner', 'Database User Support Specialist', 'Database Administrator', 'Database Analyst', 'Database Architect', 'Database Consultant']
class Command(BaseCommand):
    help = "Generate  fake entries for the employer_table, company, Job, and req_skill models."

    def handle(self, *args, **kwargs):
        # Generate 10 fake employers
        employers = []
        for _ in range(50):
            employer = employer_table.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_no=fake.unique.random_int(min=1000000000, max=9999999999),
                email=fake.unique.email(),
                password="password123", 
                age=str(fake.random_int(min=22, max=60)),
            )
            employers.append(employer)

        # Generate 10 fake companies
        companies = []
        for employer in employers:
            company_instance = company.objects.create(
                recruiter=employer,
                cmp_email=fake.unique.company_email(),
                name=fake.company(),
                bio=fake.paragraph(nb_sentences=3),
                city=random.choice(possible_cities),
                employees=random.randint(10, 500),
                image=fake.image_url(),
            )
            companies.append(company_instance)

        # Generate 30 fake jobs
        jobs = []
        for _ in range(30):
            job = Job.objects.create(
                company=random.choice(companies),
                title=random.choice(possible_job_title),
                job_type=random.choice(possible_job_types),
                description=fake.text(max_nb_chars=200),
                location=random.choice(possible_cities),
                salary=f"${random.randint(30000, 120000)}",
            )
            jobs.append(job)

        # Generate 50 fake required skills
        for _ in range(50):
            req_skill.objects.create(
                job=random.choice(jobs),
                imp_skill=random.choice(possible_skill),
                skill_2=random.choice(possible_skill),
                skill_3=random.choice(possible_skill),
                skill_4=random.choice(possible_skill),
                education=random.choice(possible_education_levels),
                speak_lng_1=random.choice(possible_languages),
                speak_lng_2=random.choice(possible_languages)
                )

        self.stdout.write(self.style.SUCCESS("Successfully added 50 fake data entries!"))
