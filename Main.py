<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Filterable Image Gallery</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h1>📸 Filterable Image Gallery</h1>
<p class="subtitle">Animals • Birds • Nature • City</p>

<div class="filter-buttons">
    <button class="active" data-name="all">All</button>
    <button data-name="animals">Animals</button>
    <button data-name="birds">Birds</button>
    <button data-name="nature">Nature</button>
    <button data-name="city">City</button>
</div>

<div class="gallery">

    <!-- Animals -->
    <div class="image" data-name="animals">
        <img src="https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=800" alt="">
    </div>

    <div class="image" data-name="animals">
        <img src="https://images.unsplash.com/photo-1517849845537-4d257902454a?w=800" alt="">
    </div>

    <!-- Birds -->
    <div class="image" data-name="birds">
        <img src="https://images.unsplash.com/photo-1444464666168-49d633b86797?w=800" alt="">
    </div>

    <div class="image" data-name="birds">
        <img src="https://images.unsplash.com/photo-1511823794984-b877161f3f1b?w=800" alt="">
    </div>

    <!-- Nature -->
    <div class="image" data-name="nature">
        <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800" alt="">
    </div>

    <div class="image" data-name="nature">
        <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800" alt="">
    </div>

    <!-- City -->
    <div class="image" data-name="city">
        <img src="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=800" alt="">
    </div>

    <div class="image" data-name="city">
        <img src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800" alt="">
    </div>

</div>

<div class="lightbox" id="lightbox">
    <span class="close">&times;</span>
    <img id="lightbox-img">
</div>

<footer>
    <p>Developed using HTML, CSS & JavaScript</p>
</footer>

<script src="script.js"></script>

</body>
</html>