import tkinter as tk
from PIL import Image, ImageTk, ImageOps, ImageDraw
import webbrowser

def open_certifications():
    certs_window = tk.Toplevel(root)
    certs_window.title("Certifications")
    certs_window.geometry("400x800")
    certs_window.configure(bg='#f0f8ff')  # AliceBlue background

    certs_label = tk.Label(certs_window, text="Certifications", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#333333")
    certs_label.pack(pady=10)

    cert_links = [
        "https://lnkd.in/eTzr3Kri", "https://lnkd.in/eYRV6q8E", "https://lnkd.in/e4UkJjbF", 
        "https://lnkd.in/eHwyh3R4", "https://lnkd.in/eKuPiWDV", "https://lnkd.in/ebDFgPhu",
        "https://lnkd.in/eqH-JdGV", "https://lnkd.in/e97rmDV6", "https://www.guvi.in/verify-certificate?id=Oau9421lXEC712623F",
        # Add all 50 links
    ]

    for i, link in enumerate(cert_links, start=1):
        cert_button = tk.Button(certs_window, text=f"Certification {i}", command=lambda url=link: webbrowser.open(url), bg="#4682b4", fg="white", font=("Helvetica", 12, "bold"))
        cert_button.pack(pady=2)

def show_achievement_info(achievement_info):
    info_window = tk.Toplevel(root)
    info_window.title("Achievement Details")
    info_window.geometry("400x300")
    info_window.configure(bg='#f0f8ff')  # AliceBlue background

    info_label = tk.Label(info_window, text=achievement_info, font=("Helvetica", 14), bg="#f0f8ff", fg="#333333")
    info_label.pack(pady=20)

def open_achievements():
    ach_window = tk.Toplevel(root)
    ach_window.title("Achievements")
    ach_window.geometry("400x800")
    ach_window.configure(bg='#f0f8ff')  # AliceBlue background

    ach_label = tk.Label(ach_window, text="Achievements", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#333333")
    ach_label.pack(pady=10)

    achievements_list = [
        "I have Conducted a CYBERSECURITY WORKSHOP: Details about the workshop.",
        "I have Conducted AI WORKSHOP: Details about the AI workshop.",
        "I worked as a Python Developer INTERN: Details about the internship.",
        # Add all 50 achievements with details
    ]

    for i, achievement in enumerate(achievements_list, start=1):
        ach_button = tk.Button(ach_window, text=f"Achievement {i}", command=lambda info=achievement: show_achievement_info(info), bg="#4682b4", fg="white", font=("Helvetica", 12, "bold"))
        ach_button.pack(pady=2)

def open_skills():
    skills_window = tk.Toplevel(root)
    skills_window.title("My Skills")
    skills_window.geometry("400x400")
    skills_window.configure(bg='#f0f8ff')  # AliceBlue background
    
    skills_label = tk.Label(skills_window, text="Skills", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#333333")
    skills_label.pack(pady=10)

    skills_list = [
        "Python Developer", "AI Developer", "Prompt Engineer", 
        "Design Thinker", "Creative Thinker", "Graphic Designer", 
        "Communication", "Problem Solving"
    ]
    
    skills_text = "\n".join([f"- {skill}" for skill in skills_list])
    
    skills_description = tk.Label(skills_window, text=skills_text, bg="#f0f8ff", font=("Helvetica", 14), justify="left")
    skills_description.pack(pady=10)

def circular_crop(image):
    mask = Image.new("L", (image.size[0], image.size[1]), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

    circular_image = Image.new("RGBA", (image.size[0], image.size[1]), (0, 0, 0, 0))
    circular_image.paste(image, (0, 0), mask)
    return circular_image

def exit_application():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("My Portfolio")
root.geometry("800x800")

# Create a Canvas for the moving background
canvas = tk.Canvas(root, width=800, height=800, bd=0, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load background image and create a moving effect
bg_image = Image.open("C:/Users/Deepu/Desktop/python/portfolio/technology-6701504_640.webp")  # Replace with your background image path
bg_image = bg_image.resize((1600, 800), Image.LANCZOS)  # Resize image to double the width
bg_image_tk = ImageTk.PhotoImage(bg_image)
bg_id = canvas.create_image(0, 0, anchor="nw", image=bg_image_tk)

def move_background():
    canvas.move(bg_id, -10, 0)  # Move the background image left by 10 pixels to increase speed
    if canvas.coords(bg_id)[0] <= -800:
        canvas.coords(bg_id, 0, 0)  # Reset position when the image is out of view
    canvas.after(20, move_background)  # Repeat after 20 ms for faster animation

move_background()  # Start the animation

# Create a frame for centering content
content_frame = tk.Frame(root, bg='#f0f8ff')
content_frame.place(relx=0.5, rely=0.5, anchor='center')

# Profile Image with Circular Crop
profile_frame = tk.Frame(content_frame, bg="#ffffff")
profile_frame.pack(pady=20)

profile_img = Image.open("C:/Users/Deepu/Desktop/python/portfolio/1714398748168.png")  # Replace with your profile image path
profile_img = ImageOps.fit(profile_img, (150, 150), Image.LANCZOS)
profile_img = circular_crop(profile_img)
profile_photo = ImageTk.PhotoImage(profile_img)
profile_label = tk.Label(profile_frame, image=profile_photo, bg='#f0f8ff')
profile_label.pack()

# Header Section
header = tk.Frame(content_frame, bg="#4682b4", bd=5)
header.pack(fill="x")
header_label = tk.Label(header, text="Nagadeepak's Portfolio", font=("Helvetica", 24, "bold"), fg="white", bg="#4682b4")
header_label.pack(pady=10)

# About Section
about = tk.Label(content_frame, text="About Me", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#333333")
about.pack(pady=10)
about_text = tk.Label(content_frame, text="I am a passionate developer with experience in Python, AI, and web development.", bg="#f0f8ff", fg="#333333")
about_text.pack(pady=5)

# Buttons
skills_button = tk.Button(content_frame, text="View Skills", command=open_skills, bg="#4682b4", fg="white", font=("Helvetica", 14, "bold"))
skills_button.pack(pady=10)

certifications_button = tk.Button(content_frame, text="View Certifications", command=open_certifications, bg="#4682b4", fg="white", font=("Helvetica", 14, "bold"))
certifications_button.pack(pady=10)

achievements_button = tk.Button(content_frame, text="View Achievements", command=open_achievements, bg="#4682b4", fg="white", font=("Helvetica", 14, "bold"))
achievements_button.pack(pady=10)

contact = tk.Label(content_frame, text="Contact", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#333333")
contact.pack(pady=10)
contact_info = tk.Label(content_frame, text="Email: nagadeepak1712@gmail.com", bg="#f0f8ff", fg="#333333")
contact_info.pack(pady=5)

# Exit Button
exit_button = tk.Button(content_frame, text="Exit", command=exit_application, bg="#ff6347", fg="white", font=("Helvetica", 14, "bold"))
exit_button.pack(pady=20)

root.mainloop()
