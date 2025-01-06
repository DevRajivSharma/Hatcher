import random
from faker import Faker
from django.core.management.base import BaseCommand
from employer.models import employer_table, company, Job, req_skill

fake = Faker()

class Command(BaseCommand):
    help = "Generate 50 fake entries for the employer_table, company, Job, and req_skill models."

    def handle(self, *args, **kwargs):
        # Generate 10 fake employers
        employers = []
        for _ in range(50):
            employer = employer_table.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_no=fake.unique.random_int(min=1000000000, max=9999999999),
                email=fake.unique.email(),
                password="password123",  # Default password (hashed in save method)
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
                address=fake.address(),
                employees=random.randint(10, 500),
                image=fake.image_url(),
            )
            companies.append(company_instance)

        # Generate 30 fake jobs
        jobs = []
        for _ in range(30):
            job = Job.objects.create(
                company=random.choice(companies),
                title=fake.job(),
                job_type=random.choice(["Full-time", "Part-time", "Contract"]),
                description=fake.text(max_nb_chars=200),
                location=fake.city(),
                salary=f"${random.randint(30000, 120000)}",
            )
            jobs.append(job)

        # Generate 50 fake required skills
        for _ in range(50):
            req_skill.objects.create(
                job=random.choice(jobs),
                imp_skill=fake.word(),
                skill_2=fake.word(),
                skill_3=fake.word(),
                skill_4=fake.word(),
                education=random.choice(
                    ["Bachelor's Degree", "Master's Degree", "High School Diploma"]
                ),
                speak_lng_1=fake.language_name(),
                speak_lng_2=fake.language_name(),
            )

        self.stdout.write(self.style.SUCCESS("Successfully added 50 fake data entries!"))
