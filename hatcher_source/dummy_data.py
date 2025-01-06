import random
from faker import Faker
from employer.models import *
fake = Faker()
Faker.seed(313)

possible_job_types = ['Full-time', 'Part-time', 'Contract', 'Internship', 'Temporary', 'Freelance']
possible_education_levels = ['High School', 'Diploma', 'Bachelor\'s Degree', 'Master\'s Degree', 'PhD']
possible_languages = ['English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Korean', 'Arabic', 'Russian', 'Portuguese', 'Italian', 'Dutch', 'Turkish', 'Polish', 'Swedish', 'Danish', 'Norwegian', 'Finnish', 'Greek', 'Czech', 'Hungarian', 'Romanian', 'Ukrainian', 'Bulgarian', 'Croatian', 'Serbian', 'Slovak', 'Slovenian', 'Lithuanian', 'Latvian', 'Estonian', 'Maltese', 'Icelandic', 'Faroese', 'Luxembourgish', 'Irish', 'Welsh', 'Scottish Gaelic', 'Breton', 'Basque', 'Catalan', 'Galician', 'Occitan', 'Albanian', 'Macedonian', 'Bosnian', 'Montenegrin', 'Azerbaijani', 'Georgian', 'Armenian', 'Kazakh', 'Uzbek', 'Turkmen', 'Kyrgyz']

possible_skill = ['Python', 'Java', 'C++', 'C#', 'JavaScript', 'Ruby', 'PHP', 'Swift', 'Kotlin', 'Rust', 'Go', 'TypeScript', 'HTML', 'CSS', 'SQL', 'NoSQL', 'React', 'Angular', 'Vue', 'Django', 'Flask', 'Spring', 'Laravel', 'Express', 'Ruby on Rails', 'Node.js', 'jQuery', 'Bootstrap', 'Tailwind CSS', 'Sass', 'Less', 'PostgreSQL', 'MySQL', 'MongoDB', 'SQLite', 'Firebase', 'Docker', 'Kubernetes', 'Jenkins', 'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Jira', 'Confluence', 'Slack', 'Trello', 'Asana', 'Notion', 'Figma', 'Sketch', 'Adobe XD', 'Photoshop', 'Illustrator', 'InDesign', 'Premiere Pro', 'After Effects', 'Final Cut Pro', 'Logic Pro', 'Ableton Live', 'Pro Tools', 'FL Studio', 'Audacity', 'GarageBand', 'Unity', 'Unreal Engine', 'Blender', 'Maya', '3ds Max', 'AutoCAD', 'SolidWorks', 'Figma', 'Sketch', 'Adobe XD', 'Photoshop', 'Illustrator', 'InDesign', 'Premiere Pro', 'After Effects', 'Final Cut Pro', 'Logic Pro', 'Ableton Live', 'Pro Tools', 'FL Studio', 'Audacity', 'GarageBand', 'Unity', 'Unreal Engine', 'Blender', 'Maya', '3ds Max', 'AutoCAD', 'SolidWorks', 'Figma', 'Sketch', 'Adobe XD', 'Photoshop', 'Illustrator', 'InDesign', 'Premiere Pro', 'After Effects', 'Final Cut Pro', 'Logic Pro', 'Ableton Live', 'Pro Tools', 'FL Studio', 'Audacity', 'GarageBand', 'Unity', 'Unreal Engine', 'Blender', 'Maya', '3ds Max', 'AutoCAD', 'SolidWorks', 'Figma', 'Sketch', 'Adobe XD', 'Photoshop', 'Illustrator', 'InDesign', 'Premiere Pro', 'After Effects', 'Final Cut Pro', 'Logic Pro', 'Ableton Live']
for i in range(5):
    employer_table_instance = employer_table.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        phone_no=fake.phone_number(),
        email=fake.email(),
        password=fake.password(),
        age=random.randint(18, 60),
        company_exist=True,
    )
    company_instance = company.objects.create(
        recruiter=employer_table_instance,
        cmp_email = fake.email(),
        name=fake.company(),
        bio=fake.text(),
        address=fake.address(),
        employees=random.randint(1, 100),
        image=fake.image_url(),
    )
    job_instance = Job.objects.create(
        company=company_instance,
        title=fake.job(),
        job_type=random.choice(possible_job_types),
        description=fake.text(),
        location=fake.city(),
        salary=fake.random_int(1000, 100000),
    )
    req_skill_instance = req_skill.objects.create(
        job=job_instance,
        imp_skill=random.choice(possible_skill),
        skill_2=random.choice(possible_skill),
        skill_3=random.choice(possible_skill),
        skill_4=random.choice(possible_skill),
        education=random.choice(possible_education_levels),
        speak_lng_1=random.choice(possible_languages),
        speak_lng_2=random.choice(possible_languages),
    )