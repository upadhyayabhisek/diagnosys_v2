import sqlite3
from werkzeug.security import generate_password_hash

def seed_data():
    db_path = '../instance/mediai.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    hashed_pw = generate_password_hash("nepal123")
    users = [
        ("Prerana Rajbhandari", "prerana@example.com", "user", 1, "Female", "1995-08-22"),
        ("Rohan Shrestha", "rohan@example.com", "user", 1, "Male", "1988-12-02"),
        ("Kriti Joshi", "kriti@example.com", "user", 1, "Female", "2001-03-10"),
        ("Binod Chaudhary", "binod@example.com", "user", 1, "Male", "1975-07-25"),
        ("Aarati Paudel", "aarati@example.com", "user", 0, "Female", "1992-11-30"),
        ("Suman Gurung", "suman@example.com", "user", 1, "Male", "1994-01-14"),
        ("Deepika Lama", "deepika@example.com", "user", 1, "Female", "1997-06-05"),
        ("Nabin Maharjan", "nabin@example.com", "user", 1, "Male", "1985-09-18"),
        ("Ishani Shah", "ishani@example.com", "user", 1, "Female", "1999-04-20")
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO users (name, email, password, role, status, gender, birthday) 
        VALUES (?, ?, ?, ?, ?, ?, ?)""", 
        [(u[0], u[1], hashed_pw, u[2], u[3], u[4], u[5]) for u in users])

    hospitals = [
        ("Manmohan Memorial Medical College", "Swayambhu, Kathmandu", "Advanced teaching hospital with 24/7 ER.", "Teaching, Private, Surgery", "manmohan.jpg"),
        ("Grande International Hospital", "Dhapasi, Kathmandu", "Premium healthcare with international standards.", "Private, Multi-specialty, Cardiology", "grande.jpg"),
        ("Medicity Hospital", "Bhaisepati, Lalitpur", "Nepal's first quaternary care hospital.", "Private, Neurology, Oncology", "medicity.jpg"),
        ("Kanti Children's Hospital", "Maharajgunj, Kathmandu", "The primary government pediatric hospital.", "Government, Pediatrics, NGO", "kanti.jpg"),
        ("Lumbini Provincial Hospital", "Butwal, Rupandehi", "Largest referral center in Lumbini Province.", "Government, Regional, General", "lumbini.jpg"),
        ("Bir Hospital", "Ratnapark, Kathmandu", "The oldest and busiest hospital in Nepal.", "Government, Historic, Trauma", "bir.jpg"),
        ("B.C. Cancer Hospital", "Bharatpur, Chitwan", "Dedicated oncology care and research.", "Cancer, Government, Specialized", "chitwan_cancer.jpg")
    ]
    cursor.executemany("INSERT INTO hospitals (name, address, description, tags, image) VALUES (?, ?, ?, ?, ?)", hospitals)

    doctors = [
        ("Dr. Om Murti Pant", "om.pant@gmail.com", "Neurology", "Annapurna Neurological Hospital"),
        ("Dr. Raamesh Koirala", "raamesh@heart.com", "Cardiac Surgery", "Shahid Gangalal Heart Center"),
        ("Dr. Jyoti Agrawal", "jyoti.a@clinic.com", "Gynecology", "Norvic International"),
        ("Dr. Anup Bastola", "anup.b@health.np", "Infectious Disease", "Sukraraj Tropical Hospital"),
        ("Dr. Sudhamshu KC", "sudhamshu@liver.com", "Hepatology", "Bir Hospital"),
        ("Dr. Archana Amatya", "archana@tuth.com", "Dermatology", "T.U. Teaching Hospital"),
        ("Dr. Bishal Gyawali", "bishal.g@cancer.com", "Oncology", "B.P. Koirala Cancer Center"),
        ("Dr. Pukar Chandra Shrestha", "pukar@transplant.com", "Nephrology", "Human Organ Transplant Center")
    ]
    cursor.executemany("INSERT OR IGNORE INTO doctors (name, email, specialty, workplace) VALUES (?, ?, ?, ?)", doctors)

    faqs = [
        ("What is the cost of a general OPD ticket?", "In government hospitals, it ranges from NPR 50-100. In private, it ranges from NPR 500-1000.", "Pricing"),
        ("How do I get a Health Insurance card in Nepal?", "You can visit your local ward office or designated enrollment center with your citizenship.", "Insurance"),
        ("Which hospital is best for emergency trauma?", "Bir Hospital (Trauma Center) and TUTH are highly recommended for emergencies.", "Emergency"),
        ("Are telemedicine services available?", "Yes, many hospitals like Grande and Medicity offer video consultations.", "Digital Health"),
        ("Do I need an appointment for blood tests?", "Most labs allow walk-ins, but fasting is required for sugar and lipid profile tests.", "Lab Services"),
        ("How to check doctor availability?", "You can use our search bar or contact the hospital's help desk via the numbers provided.", "General")
    ]
    cursor.executemany("INSERT INTO faqs (question, answer, category) VALUES (?, ?, ?)", faqs)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_data()