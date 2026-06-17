<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h1>Image Gallery</h1>

<div class="gallery">
    <img src="images/img1.jpg" onclick="openModal(this.src)">
    <img src="images/img2.jpg" onclick="openModal(this.src)">
    <img src="images/img3.jpg" onclick="openModal(this.src)">
    <img src="images/img4.jpg" onclick="openModal(this.src)">
    <img src="images/img5.jpg" onclick="openModal(this.src)">
    <img src="images/img6.jpg" onclick="openModal(this.src)">
</div>

<div id="modal" class="modal">
    <span class="close" onclick="closeModal()">&times;</span>
    <img id="modalImg">
</div>

<script src="script.js"></script>

</body>
</html>
