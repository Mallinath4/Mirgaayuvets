from flask import Flask, render_template, url_for
import os
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

# Complete blogs_data list for app.py
blogs_data = [
    {
        "id": "puppy_proofing",
        "title": "10 Essential Puppy Proofing Tips from SKvets",
        "image": "images/puppy.jpeg",
        "excerpt": "Create a safe and friendly environment for your new best friend...",
        "content": """
        <h2>10 Essential Puppy Proofing Tips from SKvets</h2>
        <p>Bringing a new puppy home is exciting, but it requires careful preparation to ensure their safety. Here are our top 10 tips for creating a puppy-safe environment.</p>
        
        <h3>1. Secure Electrical Cords</h3>
        <p>Puppies love to chew, and electrical cords can be dangerous. Use cord protectors or keep them out of reach. Consider using bitter apple spray as a deterrent.</p>
        
        <h3>2. Remove Toxic Plants</h3>
        <p>Many common houseplants are toxic to dogs, including lilies, azaleas, and sago palms. Research and remove any dangerous plants from your home.</p>
        
        <h3>3. Lock Cabinets</h3>
        <p>Install child-proof locks on cabinets containing cleaning supplies, medications, or other harmful substances. Puppies are curious and can get into trouble quickly.</p>
        
        <h3>4. Secure Trash Cans</h3>
        <p>Use tight-fitting lids or store trash cans in secured areas to prevent your puppy from getting into garbage, which can contain harmful foods or objects.</p>
        
        <h3>5. Check for Small Objects</h3>
        <p>Remove small items that could be choking hazards, including coins, jewelry, small toys, and buttons. Regularly scan floors and low surfaces.</p>
        
        <h3>6. Install Baby Gates</h3>
        <p>Use baby gates to restrict access to stairs or certain rooms until your puppy is trained and mature enough to handle these areas safely.</p>
        
        <h3>7. Secure Windows and Balconies</h3>
        <p>Ensure windows have secure screens and balconies have appropriate barriers to prevent falls.</p>
        
        <h3>8. Store Food Safely</h3>
        <p>Keep human food, especially chocolate, grapes, onions, and other toxic foods, safely stored away from curious puppies.</p>
        
        <h3>9. Check Your Yard</h3>
        <p>Remove toxic plants, secure fencing, and eliminate any small objects or chemicals that could harm your puppy during outdoor play.</p>
        
        <h3>10. Create a Safe Space</h3>
        <p>Designate a puppy-safe room or area where your new friend can stay when unsupervised, complete with food, water, toys, and a comfortable bed.</p>
        """
    },
    {
        "id": "puppy_care",
        "title": "How to take care of your Puppy and feed them?",
        "image": "images/Maltese Dog 1.png",
        "excerpt": "The first week of the puppies' lives is the most critical to their survival...",
        "content": """
        <h2>Complete Guide to Puppy Care and Feeding</h2>
        <p>The first few weeks and months of a puppy's life are crucial for their development and long-term health. Here's your comprehensive guide to proper puppy care.</p>
        
        <h3>Feeding Schedule by Age</h3>
        <p><strong>8-12 weeks:</strong> Feed 4 times per day<br>
        <strong>3-6 months:</strong> Feed 3 times per day<br>
        <strong>6+ months:</strong> Feed 2 times per day</p>
        
        <h3>Choosing the Right Food</h3>
        <ul>
            <li>Select high-quality puppy food appropriate for your dog's expected adult size</li>
            <li>Look for AAFCO certification on the label</li>
            <li>Avoid foods with excessive fillers or by-products</li>
            <li>Consult your veterinarian for specific recommendations</li>
        </ul>
        
        <h3>Feeding Guidelines</h3>
        <ul>
            <li>Feed at consistent times each day</li>
            <li>Use measuring cups for accurate portions</li>
            <li>Provide fresh water at all times</li>
            <li>Monitor your puppy's weight and adjust portions as needed</li>
        </ul>
        
        <h3>Early Healthcare Needs</h3>
        <ul>
            <li>First vet visit within 48 hours of bringing puppy home</li>
            <li>Begin vaccination series at 6-8 weeks</li>
            <li>Start deworming protocol</li>
            <li>Discuss spay/neuter timing</li>
        </ul>
        
        <h3>Socialization and Training</h3>
        <p>Early socialization is critical. Expose your puppy to various people, sounds, and experiences in a safe, controlled manner during the first 16 weeks.</p>
        
        <h3>Creating a Routine</h3>
        <p>Establish consistent schedules for feeding, potty breaks, playtime, and sleep to help your puppy feel secure and aid in house training.</p>
        """
    },
    {
        "id": "vet_checkups",
        "title": "Why Regular Veterinary Checkups are Important",
        "image": "images/img2.jpg",
        "excerpt": "Routine vet visits ensure your pet's long-term health and well-being...",
        "content": """
        <h2>The Importance of Regular Veterinary Checkups</h2>
        <p>Regular veterinary visits are one of the most important things you can do for your pet's health and longevity. Here's why consistent healthcare matters.</p>
        
        <h3>Early Detection of Health Issues</h3>
        <p>Many serious health conditions don't show obvious symptoms until they're advanced. Regular checkups allow veterinarians to:</p>
        <ul>
            <li>Detect problems before they become serious</li>
            <li>Monitor changes in your pet's condition</li>
            <li>Identify risk factors for future issues</li>
            <li>Perform diagnostic tests when needed</li>
        </ul>
        
        <h3>Preventive Care Benefits</h3>
        <ul>
            <li><strong>Vaccinations:</strong> Protect against serious diseases</li>
            <li><strong>Parasite Prevention:</strong> Control fleas, ticks, and worms</li>
            <li><strong>Dental Care:</strong> Prevent dental disease and related problems</li>
            <li><strong>Weight Management:</strong> Prevent obesity-related health issues</li>
        </ul>
        
        <h3>Recommended Checkup Schedule</h3>
        <ul>
            <li><strong>Puppies/Kittens:</strong> Every 3-4 weeks until 16 weeks old</li>
            <li><strong>Adult Pets (1-7 years):</strong> Once per year</li>
            <li><strong>Senior Pets (7+ years):</strong> Every 6 months</li>
            <li><strong>Pets with Chronic Conditions:</strong> As recommended by veterinarian</li>
        </ul>
        
        <h3>What to Expect During a Checkup</h3>
        <ul>
            <li>Physical examination from nose to tail</li>
            <li>Weight and body condition assessment</li>
            <li>Vaccination updates as needed</li>
            <li>Parasite screening and prevention</li>
            <li>Discussion of diet and behavior</li>
            <li>Dental evaluation</li>
        </ul>
        
        <h3>Cost-Effectiveness of Preventive Care</h3>
        <p>While regular checkups require an investment, they're much more cost-effective than treating serious diseases that could have been prevented or caught early.</p>
        
        <h3>Building a Relationship with Your Vet</h3>
        <p>Regular visits help your veterinarian understand your pet's normal baseline, making it easier to detect changes and provide personalized care recommendations.</p>
        """
    },
    {
        "id": "pet_nutrition",
        "title": "The Ultimate Pet Nutrition Guide",
        "image": "images/img4.jpg",
        "excerpt": "Learn how to provide a balanced diet for your pet to keep them healthy...",
        "content": """
        <h2>The Ultimate Pet Nutrition Guide</h2>
        <p>Proper nutrition is the foundation of your pet's health. Understanding your pet's nutritional needs helps ensure a long, healthy, and happy life.</p>
        
        <h3>Basic Nutritional Requirements</h3>
        <p>All pets need six basic nutrients:</p>
        <ul>
            <li><strong>Water:</strong> Most important nutrient - always provide fresh, clean water</li>
            <li><strong>Protein:</strong> Essential for growth and tissue repair</li>
            <li><strong>Carbohydrates:</strong> Provide energy and fiber</li>
            <li><strong>Fats:</strong> Essential fatty acids and energy source</li>
            <li><strong>Vitamins:</strong> Support various body functions</li>
            <li><strong>Minerals:</strong> Support bone health and metabolic processes</li>
        </ul>
        
        <h3>Life Stage Nutrition</h3>
        <p><strong>Puppy/Kitten:</strong> High-calorie, nutrient-dense food for rapid growth<br>
        <strong>Adult:</strong> Balanced maintenance diet based on activity level<br>
        <strong>Senior:</strong> Easily digestible food, often with joint support</p>
        
        <h3>Reading Pet Food Labels</h3>
        <ul>
            <li>Look for AAFCO nutritional adequacy statement</li>
            <li>Check the ingredient list - first few ingredients are most important</li>
            <li>Understand guaranteed analysis percentages</li>
            <li>Consider your pet's specific needs (size, age, activity level)</li>
        </ul>
        
        <h3>Common Feeding Mistakes</h3>
        <ul>
            <li>Overfeeding - leading cause of obesity</li>
            <li>Too many treats (should be less than 10% of daily calories)</li>
            <li>Feeding human food without knowing what's safe</li>
            <li>Sudden diet changes without gradual transition</li>
            <li>Free-feeding instead of measured portions</li>
        </ul>
        
        <h3>Special Dietary Considerations</h3>
        <ul>
            <li><strong>Food Allergies:</strong> May require elimination diets</li>
            <li><strong>Weight Management:</strong> Controlled portions and exercise</li>
            <li><strong>Medical Conditions:</strong> Prescription diets may be necessary</li>
            <li><strong>Active Pets:</strong> May need higher calorie density</li>
        </ul>
        
        <h3>When to Consult a Veterinarian</h3>
        <p>Consult your vet about nutrition if your pet has changes in appetite, weight, energy level, or if you're considering a diet change for health reasons.</p>
        """
    },
    {
        "id": "dog_training",
        "title": "Top 5 Dog Training Tips for Beginners",
        "image": "images/img5.jpg",
        "excerpt": "Training your dog doesn't have to be stressful. Follow these expert tips...",
        "content": """
        <h2>Top 5 Dog Training Tips for Beginners</h2>
        <p>Training your dog doesn't have to be overwhelming. With patience, consistency, and the right approach, you can build a strong bond while teaching essential skills.</p>
        
        <h3>1. Start with Positive Reinforcement</h3>
        <p>Reward good behavior immediately with treats, praise, or play. This creates positive associations and encourages your dog to repeat desired behaviors.</p>
        <ul>
            <li>Use high-value treats your dog loves</li>
            <li>Time rewards perfectly - within seconds of good behavior</li>
            <li>Be enthusiastic with praise</li>
            <li>Avoid punishment-based methods</li>
        </ul>
        
        <h3>2. Be Consistent with Commands</h3>
        <p>Use the same word for each command every time. If you use "sit" once, don't switch to "sit down" later.</p>
        <ul>
            <li>Choose simple, clear commands</li>
            <li>Ensure all family members use the same words</li>
            <li>Practice commands in different locations</li>
            <li>Be patient - repetition is key</li>
        </ul>
        
        <h3>3. Keep Training Sessions Short</h3>
        <p>Dogs have short attention spans. Multiple 5-10 minute sessions throughout the day are more effective than one long session.</p>
        <ul>
            <li>End on a positive note</li>
            <li>Practice 2-3 times daily</li>
            <li>Stop if your dog seems tired or frustrated</li>
            <li>Make training fun and engaging</li>
        </ul>
        
        <h3>4. Master the Basics First</h3>
        <p>Focus on essential commands before moving to advanced tricks:</p>
        <ul>
            <li><strong>Sit:</strong> Foundation for many other commands</li>
            <li><strong>Stay:</strong> Teaches impulse control</li>
            <li><strong>Come:</strong> Essential for safety</li>
            <li><strong>Down:</strong> Helps with relaxation and control</li>
            <li><strong>Leave it:</strong> Prevents unwanted behaviors</li>
        </ul>
        
        <h3>5. Socialize Early and Often</h3>
        <p>Expose your dog to various people, animals, sounds, and environments in a positive way, especially during the critical socialization period (3-14 weeks).</p>
        <ul>
            <li>Start slowly with less overwhelming situations</li>
            <li>Watch your dog's body language</li>
            <li>Reward calm, confident behavior</li>
            <li>Never force interactions</li>
        </ul>
        
        <h3>Common Training Mistakes to Avoid</h3>
        <ul>
            <li>Inconsistent rules and expectations</li>
            <li>Inadvertently rewarding bad behavior</li>
            <li>Getting frustrated or losing patience</li>
            <li>Skipping socialization</li>
            <li>Expecting too much too quickly</li>
        </ul>
        
        <h3>When to Seek Professional Help</h3>
        <p>Consider professional training if you're dealing with aggression, severe anxiety, or if you're not seeing progress with basic training after several weeks of consistent effort.</p>
        """
    }
    # Add more blog entries as needed...
]

# Complete services_data dictionary for app.py
services_data = {
    "vaccination": {
        "title": "Pet Vaccination Services",
        "image": "imgs1.png",
        "description": "Comprehensive vaccination services for your pets at home",
        "content": """
        <h2>Professional Pet Vaccination at Your Doorstep</h2>
        <p>Our experienced veterinarians provide complete vaccination services in the comfort of your home, eliminating the stress of clinic visits for both you and your pet.</p>
        
        <h3>Core Vaccinations We Provide:</h3>
        <ul>
            <li><strong>Dogs:</strong> DHPP (Distemper, Hepatitis, Parvovirus, Parainfluenza), Rabies</li>
            <li><strong>Cats:</strong> FVRCP (Feline Viral Rhinotracheitis, Calicivirus, Panleukopenia), Rabies</li>
        </ul>
        
        <h3>Non-Core Vaccinations:</h3>
        <ul>
            <li>Lyme Disease</li>
            <li>Kennel Cough</li>
            <li>Feline Leukemia</li>
        </ul>
        
        <h3>Benefits of Home Vaccination:</h3>
        <ul>
            <li>Reduced stress for your pet</li>
            <li>No exposure to sick animals</li>
            <li>Convenient scheduling</li>
            <li>Personalized care and attention</li>
        </ul>
        
        <h3>Vaccination Schedule:</h3>
        <p>We follow the latest veterinary guidelines to ensure your pet receives vaccines at the optimal times for maximum protection.</p>
        
        """
    },
    "general_treatment": {
        "title": "General Pet Treatment",
        "image": "imgs2.jpg",
        "description": "Comprehensive general treatment services for all your pet's health needs",
        "content": """
        <h2>Comprehensive General Treatment Services</h2>
        <p>Our skilled veterinarians provide a wide range of general treatment services at your home, ensuring your pet receives professional care without the stress of traveling to a clinic.</p>
        
        <h3>Services We Provide:</h3>
        <ul>
            <li>Health examinations and consultations</li>
            <li>Wound care and bandaging</li>
            <li>Skin condition treatment</li>
            <li>Eye and ear infections</li>
            <li>Digestive issues</li>
            <li>Minor surgical procedures</li>
        </ul>
        
        <h3>When to Seek Treatment:</h3>
        <ul>
            <li>Changes in eating or drinking habits</li>
            <li>Lethargy or unusual behavior</li>
            <li>Vomiting or diarrhea</li>
            <li>Difficulty breathing</li>
            <li>Skin irritation or allergies</li>
        </ul>
        
        <h3>Our Approach:</h3>
        <p>We believe in thorough examinations and clear communication with pet owners. Our veterinarians will explain the diagnosis, treatment options, and provide detailed care instructions.</p>
        """
    },
    "deworming": {
        "title": "Pet Deworming Services",
        "image": "imgs3.jpg",
        "description": "Professional deworming services with fecal analysis",
        "content": """
        <h2>Professional Deworming Services</h2>
        <p>Keep your pets healthy and parasite-free with our comprehensive deworming services, including fecal analysis and targeted treatment.</p>
        
        <h3>Why Deworming is Important:</h3>
        <ul>
            <li>Prevents intestinal parasites</li>
            <li>Protects family health</li>
            <li>Improves pet's overall well-being</li>
            <li>Prevents weight loss and malnutrition</li>
        </ul>
        
        <h3>Our Process:</h3>
        <ol>
            <li><strong>Fecal Analysis:</strong> We examine your pet's stool sample to identify specific parasites</li>
            <li><strong>Targeted Treatment:</strong> Based on results, we provide appropriate deworming medication</li>
            <li><strong>Follow-up:</strong> We schedule follow-up visits to ensure treatment effectiveness</li>
        </ol>
        
        <h3>Common Parasites We Treat:</h3>
        <ul>
            <li>Roundworms</li>
            <li>Hookworms</li>
            <li>Tapeworms</li>
            <li>Whipworms</li>
            <li>Giardia</li>
        </ul>
        
        <h3>Deworming Schedule:</h3>
        <p>We recommend regular deworming based on your pet's age, lifestyle, and risk factors. Puppies and kittens require more frequent treatment than adult pets.</p>
        """
    },
    "grooming": {
        "title": "Pet Grooming Services",
        "image": "imgs4.jpg",
        "description": "Professional grooming services in the comfort of your home",
        "content": """
        <h2>Professional Pet Grooming at Home</h2>
        <p>Our expert groomers bring professional grooming services directly to your door, ensuring your pet looks and feels their best in a familiar, stress-free environment.</p>
        
        <h3>Grooming Services Include:</h3>
        <ul>
            <li>Full bath with premium shampoo</li>
            <li>Hair trimming and styling</li>
            <li>Nail trimming and filing</li>
            <li>Ear cleaning</li>
            <li>Teeth brushing</li>
            <li>Flea and tick treatment</li>
        </ul>
        
        <h3>Benefits of Home Grooming:</h3>
        <ul>
            <li>Familiar environment reduces anxiety</li>
            <li>One-on-one attention</li>
            <li>No travel stress</li>
            <li>Flexible scheduling</li>
            <li>Personalized grooming approach</li>
        </ul>
        
        <h3>Grooming Packages:</h3>
        <ul>
            <li><strong>Basic Package:</strong> Bath, dry, nail trim</li>
            <li><strong>Standard Package:</strong> Bath, dry, nail trim, ear cleaning</li>
            <li><strong>Premium Package:</strong> Full service including styling and teeth cleaning</li>
        </ul>
        
        <h3>Suitable for All Breeds:</h3>
        <p>Our groomers are experienced with all dog and cat breeds, understanding the specific needs and grooming requirements of each.</p>
        """
    },
    "nail_trimming": {
        "title": "Professional Nail Trimming",
        "image": "nail.jpeg",
        "description": "Expert nail care to keep your pet comfortable and healthy",
        "content": """
        <h2>Professional Nail Trimming Services</h2>
        <p>Regular nail trimming is essential for your pet's comfort and health. Our experienced professionals provide safe and stress-free nail care at your home.</p>
        
        <h3>Why Regular Nail Trimming is Important:</h3>
        <ul>
            <li>Prevents overgrowth and cracking</li>
            <li>Reduces risk of injury</li>
            <li>Improves walking comfort</li>
            <li>Prevents damage to furniture</li>
            <li>Maintains proper paw health</li>
        </ul>
        
        <h3>Our Nail Care Process:</h3>
        <ol>
            <li><strong>Assessment:</strong> We examine your pet's nails and paws</li>
            <li><strong>Gentle Handling:</strong> Calming techniques to keep pets relaxed</li>
            <li><strong>Professional Trimming:</strong> Using proper tools and techniques</li>
            <li><strong>Filing:</strong> Smooth finishing for comfort</li>
        </ol>
        
        <h3>Signs Your Pet Needs Nail Trimming:</h3>
        <ul>
            <li>Clicking sounds when walking</li>
            <li>Nails touching the ground</li>
            <li>Scratching furniture or people</li>
            <li>Difficulty walking</li>
        </ul>
        
        <h3>Frequency Recommendations:</h3>
        <p>Most pets need nail trimming every 3-4 weeks, but this can vary based on activity level and nail growth rate.</p>
        """
    },
    "dental_care": {
        "title": "Pet Dental Care",
        "image": "imgs6.jpg",
        "description": "Comprehensive dental health services for your pet",
        "content": """
        <h2>Professional Pet Dental Care</h2>
        <p>Dental health is crucial for your pet's overall well-being. Our comprehensive dental care services help prevent disease and maintain oral hygiene.</p>
        
        <h3>Dental Services We Provide:</h3>
        <ul>
            <li>Dental examinations</li>
            <li>Professional teeth cleaning</li>
            <li>Tartar and plaque removal</li>
            <li>Oral health assessment</li>
            <li>Dental X-rays (when needed)</li>
            <li>Treatment of dental diseases</li>
        </ul>
        
        <h3>Signs of Dental Problems:</h3>
        <ul>
            <li>Bad breath</li>
            <li>Yellow or brown tartar buildup</li>
            <li>Red or swollen gums</li>
            <li>Difficulty eating</li>
            <li>Pawing at the face</li>
            <li>Loose or missing teeth</li>
        </ul>
        
        <h3>Prevention Tips:</h3>
        <ul>
            <li>Regular brushing at home</li>
            <li>Dental treats and toys</li>
            <li>Professional cleanings</li>
            <li>Regular dental checkups</li>
        </ul>
        
        <h3>Age-Specific Care:</h3>
        <p>Puppies and kittens need different dental care than adult and senior pets. We provide age-appropriate dental services.</p>
        """
    },
    "pet_xray": {
        "title": "Mobile Pet X-Ray Services",
        "image": "imgs7.jpg",
        "description": "Advanced diagnostic imaging at your doorstep",
        "content": """
        <h2>Advanced Mobile X-Ray Services</h2>
        <p>Our state-of-the-art mobile X-ray equipment brings advanced diagnostic capabilities directly to your home, providing accurate imaging without the stress of clinic visits.</p>
        
        <h3>When X-Rays Are Needed:</h3>
        <ul>
            <li>Suspected fractures or injuries</li>
            <li>Digestive blockages</li>
            <li>Joint problems</li>
            <li>Chest conditions</li>
            <li>Abdominal issues</li>
            <li>Pre-surgical planning</li>
        </ul>
        
        <h3>Our X-Ray Services:</h3>
        <ul>
            <li>Digital X-ray imaging</li>
            <li>Immediate image review</li>
            <li>Professional interpretation</li>
            <li>Treatment recommendations</li>
            <li>Referral coordination when needed</li>
        </ul>
        
        <h3>Benefits of Mobile X-Ray:</h3>
        <ul>
            <li>No transportation stress</li>
            <li>Familiar environment for your pet</li>
            <li>Immediate results</li>
            <li>Convenient scheduling</li>
            <li>Professional equipment</li>
        </ul>
        
        <h3>Safety Standards:</h3>
        <p>We follow strict radiation safety protocols to ensure the safety of your pet, your family, and our staff during all X-ray procedures.</p>
        """
    },
    "emergency_care": {
        "title": "24/7 Emergency Pet Care",
        "image": "imgs8.jpg",
        "description": "Immediate veterinary response for urgent situations",
        "content": """
        <h2>24/7 Emergency Veterinary Services</h2>
        <p>When your pet faces a medical emergency, every second counts. Our emergency response team is available around the clock to provide immediate care.</p>
        
        <h3>Emergency Situations We Handle:</h3>
        <ul>
            <li>Trauma and accidents</li>
            <li>Difficulty breathing</li>
            <li>Seizures</li>
            <li>Poisoning</li>
            <li>Severe bleeding</li>
            <li>Collapse or unconsciousness</li>
            <li>Severe pain</li>
        </ul>
        
        <h3>Our Emergency Response:</h3>
        <ol>
            <li><strong>Immediate Assessment:</strong> Quick phone triage</li>
            <li><strong>Rapid Deployment:</strong> Emergency team dispatch</li>
            <li><strong>On-Site Stabilization:</strong> Immediate care</li>
            <li><strong>Treatment Plan:</strong> Comprehensive emergency care</li>
            <li><strong>Follow-up:</strong> Continued monitoring</li>
        </ol>
        
        <h3>Emergency Equipment:</h3>
        <ul>
            <li>Portable oxygen</li>
            <li>Emergency medications</li>
            <li>IV fluids and equipment</li>
            <li>Monitoring devices</li>
            <li>Emergency surgical tools</li>
        </ul>
        
        <h3>When to Call Emergency Services:</h3>
        <p>If you're unsure whether your pet's condition is an emergency, call us immediately. It's better to be safe and get professional advice.</p>
        """
    },
    "nutrition_guidance": {
        "title": "Pet Nutrition Consultation",
        "image": "imgs9.jpg",
        "description": "Personalized nutrition plans for optimal pet health",
        "content": """
        <h2>Professional Pet Nutrition Guidance</h2>
        <p>Proper nutrition is the foundation of good health. Our veterinary nutritionists create personalized feeding plans tailored to your pet's specific needs.</p>
        
        <h3>Nutrition Services We Provide:</h3>
        <ul>
            <li>Comprehensive nutritional assessment</li>
            <li>Customized diet plans</li>
            <li>Weight management programs</li>
            <li>Food allergy testing</li>
            <li>Supplement recommendations</li>
            <li>Feeding behavior consultation</li>
        </ul>
        
        <h3>Life Stage Nutrition:</h3>
        <ul>
            <li><strong>Puppy/Kitten:</strong> Growth and development nutrition</li>
            <li><strong>Adult:</strong> Maintenance and activity-based diets</li>
            <li><strong>Senior:</strong> Age-appropriate nutrition</li>
            <li><strong>Pregnant/Nursing:</strong> Special nutritional needs</li>
        </ul>
        
        <h3>Special Dietary Needs:</h3>
        <ul>
            <li>Weight management</li>
            <li>Food allergies and sensitivities</li>
            <li>Diabetes management</li>
            <li>Kidney disease diets</li>
            <li>Digestive disorders</li>
        </ul>
        
        <h3>Our Approach:</h3>
        <p>We consider your pet's age, breed, activity level, health conditions, and preferences to create a nutrition plan that promotes optimal health and longevity.</p>
        """
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

# Individual blog pages
@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    blog = next((b for b in blogs_data if b['id'] == blog_id), None)
    if not blog:
        return "Blog not found", 404
    return render_template('blog_detail.html', blog=blog)

# Services page
@app.route('/services')
def services():
    return render_template('services.html')

# Individual service pages
@app.route('/service/<service_id>')
def service_detail(service_id):
    service = services_data.get(service_id)
    if not service:
        return "Service not found", 404
    return render_template('service_detail.html', service=service)

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
