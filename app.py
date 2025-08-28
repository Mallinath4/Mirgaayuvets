from os import abort
import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home page



@app.route('/')
def index():
    services = []
    for service_id, data in services_data.items():
        services.append({
            "title": data["title"],
            "description": data["description"],
            "image": data["image"],
            "link": url_for('service_detail', service_id=service_id)
        })
    return render_template('index.html', services=services)

blogs_data = {
   "puppy_proofing": {
        "id": "puppy_proofing",
        "title": "10 Essential Puppy Proofing Tips from SKvets",
        "image": "images/puppy.jpeg",
        "excerpt": "Create a safe and friendly environment for your new best friend...",
        "file": "blogs/puppy_proofing.html"
    },
    "puppy_care":{ 
        "title": "How to take care of your Puppy and feed them?",
        "image": "images/Maltese Dog 1.png",
        "excerpt": "The first week of the puppies' lives is the most critical to their survival...",
        "file": "blogs/puppy_care.html"
    },
    "vet_checkups":{
        "title": "Why Regular Veterinary Checkups are Important",
        "image": "images/img2.jpg",
        "excerpt": "Routine vet visits ensure your pet's long-term health and well-being...",
        "file": "blogs/vet_checkups.html"
    },
    "pet_nutrition":{
        "title": "The Ultimate Pet Nutrition Guide",
        "image": "images/img4.jpg",
        "excerpt": "Learn how to provide a balanced diet for your pet to keep them healthy...",
        "file": "blogs/pet_nutrition.html"
    },
    "dog_training":{
        "title": "Top 5 Dog Training Tips for Beginners",
        "image": "images/img5.jpg",
        "excerpt": "Training your dog doesn't have to be stressful. Follow these expert tips...",
        "file": "blogs/dog_training.html"
    },
    "cat_care":{
        "title": "Essential Tips for Keeping Your Cat Happy",
        "image": "images/img10.jpg",
        "excerpt": "Cats require specific care and attention. Learn the best ways to care for them...",
        "file": "blogs/cat_care.html"
    },
    "senior_pet_care":{
        "title": "Caring for Senior Pets: What You Need to Know",
        "image": "images/img6.jpg",
        "excerpt": "Older pets need special care. Here are tips to keep them comfortable...",
        "file": "blogs/senior_pet_care.html"
    },
    "dog_breeds":{
        "title": "Choosing the Right Dog Breed for Your Lifestyle",
        "image": "images/img8.jpg",
        "excerpt": "Discover which dog breed suits your lifestyle the best...",
        "file": "blogs/dog_breeds.html"
    },
    "pet_emergencies":{
        "title": "How to Handle Pet Emergencies",
        "image": "images/img11.jpg",
        "excerpt": "Knowing how to act in an emergency can save your pet's life...",
        "file": "blogs/pet_emergencies.html"
    }
}


# Complete services_data dictionary for app.py
services_data = {
    "vaccination": {
        "title": "Pet Vaccination Services",
        "image": "imgs1.png",
        "description": "Comprehensive vaccination services for your pets at home",
        "file": "services/vaccination.html"
    },
    "general_treatment": {
        "title": "General Pet Treatment",
        "image": "imgs2.jpg",
        "description": "Comprehensive general treatment services for all your pet's health needs",
        "file": "services/general_treatment.html"
    },
    "deworming": {
        "title": "Pet Deworming Services",
        "image": "imgs3.jpg",
        "description": "Professional deworming services with fecal analysis",
        "file": "services/deworming.html"
    },
    "grooming": {
        "title": "Pet Grooming Services",
        "image": "imgs4.jpg",
        "description": "Professional grooming services in the comfort of your home",
        "file": "services/grooming.html"
    },
    "nail_trimming": {
        "title": "Professional Nail Trimming",
        "image": "nail.jpeg",
        "description": "Expert nail care to keep your pet comfortable and healthy",
        "file": "services/nail_trimming.html"
    },
    "dental_care": {
        "title": "Pet Dental Care",
        "image": "imgs6.jpg",
        "description": "Comprehensive dental health services for your pet",
        "file": "services/dental_care.html"
    },
    "pet_xray": {
        "title": "Mobile Pet X-Ray Services",
        "image": "imgs7.jpg",
        "description": "Advanced diagnostic imaging at your doorstep",
        "file": "services/pet_xray.html"
    },
    "emergency_care": {
        "title": "24/7 Emergency Pet Care",
        "image": "imgs8.jpg",
        "description": "Immediate veterinary response for urgent situations",
        "file": "services/emergency_care.html"
    },
    "nutrition_guidance": {
        "title": "Pet Nutrition Consultation",
        "image": "imgs9.jpg",
        "description": "Personalized nutrition plans for optimal pet health",
        "file": "services/nutrition_guidance.html"
    }
}

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')


# Gallery page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Blogs page
@app.route('/blogs')
def blogs():
    return render_template('blogs.html', blogs=blogs_data)


@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    blog = blogs_data.get(blog_id)
    if not blog:
        abort(404)
    return render_template(
        blog["file"], 
        blog=blog
    )

# Services page
@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/service/<service_id>')
def service_detail(service_id):
    service = services_data.get(service_id)
    if not service:
        abort(404)
    return render_template(
        service["file"], 
        service=service
    )


# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
