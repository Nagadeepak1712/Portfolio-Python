Code Overview 🛠️📄
This Python script creates a portfolio application using Tkinter, with visually appealing features like animations, buttons, and modular sections. Below is the breakdown of the functionality:

Key Features 🎯✨
Background Animation 🌌🎥

Canvas is used to create a scrolling background effect.
Two images alternate positions, creating a seamless animation 🎞️.
Function: move_background() ensures continuous motion.
Profile Section 🖼️👤

Displays a circular cropped profile picture using Pillow (PIL) 📸.
Function: circular_crop() generates a circular mask for the image.
Header Section 🏷️💡

Contains the main title of the portfolio: "Nagadeepak's Portfolio" ✨.
Styled with bold fonts, colors, and padding for emphasis.
About Me Section 📝🤝

Brief introduction about you as a developer 👨‍💻.
Styled text for easy readability.
Skills Section 🧠💻

Displays your skillset in a separate window 🪟.
Organized in bullet points for clarity 🔸.
Certifications Section 🎓📜

Displays a list of certifications with clickable links 🔗.
Opens a new browser tab when clicked 🌐.
Function: open_certifications() dynamically generates buttons for each certification.
Achievements Section 🏆🎉

Lists your notable achievements, with details displayed on button click 🖱️.
Function: show_achievement_info() handles pop-up details.
Contact Section 📬📱

Displays your email for professional connections ✉️.
Positioned at the bottom for easy access.
Exit Button 🛑🚪

Safely exits the application with a single click.
