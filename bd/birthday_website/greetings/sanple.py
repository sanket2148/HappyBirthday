# 1. Adding a GIF as Background
# CSS Code:
# css
# Copy code
# body {
#     font-family: 'Arial', sans-serif;
#     margin: 0;
#     padding: 0;
#     background: url('/static/greetings/background.gif') no-repeat center center/cover;
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     min-height: 100vh;
#     color: white;
#     overflow: hidden;
# }
# Replace background.gif with your GIF file's name in the static/greetings folder.
# Ensure the file size of the GIF isn’t too large for smoother loading.
# 2. Adding a Video as Background
# CSS and HTML Code:
# html
# Copy code
# <div class="video-container">
#     <video autoplay muted loop playsinline>
#         <source src="/static/greetings/background.mp4" type="video/mp4">
#         Your browser does not support the video tag.
#     </video>
# </div>
# <div class="container">
#     <h1>Happy Birthday, My Love!</h1>
#     <p>This is just the beginning of a little surprise journey for you. ❤️</p>
#     <a href="/surprise/" class="button">Next Surprise</a>
# </div>
# CSS for Video:
# css
# Copy code
# .video-container {
#     position: fixed;
#     top: 0;
#     left: 0;
#     width: 100%;
#     height: 100%;
#     z-index: -1;
#     overflow: hidden;
# }
#
# video {
#     width: 100%;
#     height: 100%;
#     object-fit: cover;
# }
# Key Features:
# autoplay and loop: Ensures the video starts automatically and plays in a loop.
# muted: Keeps the background video silent for a cleaner user experience.
# playsinline: Ensures compatibility with mobile browsers.
# Recommendations:
# GIF Option: Use for light animations or when file size matters.
# Video Option: Great for dynamic and cinematic effects. Keep it subtle and romantic (e.g., glowing candles, soft waves, or starry skies).
# Host the video file in the static/greetings folder for smooth loading.
# Would you like suggestions for romantic video ideas or sources for high-quality GIFs? Let me know!
#
#
#
#
#
#
