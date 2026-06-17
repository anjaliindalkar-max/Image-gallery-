<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Responsive Image Gallery</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<header>
    <h1>📸 Image Gallery</h1>
    <p>Beautiful Responsive Gallery with Lightbox</p>
</header>

<div class="gallery">
    <img src="https://picsum.photos/id/1015/600/400" alt="Image 1">
    <img src="https://picsum.photos/id/1016/600/400" alt="Image 2">
    <img src="https://picsum.photos/id/1018/600/400" alt="Image 3">
    <img src="https://picsum.photos/id/1020/600/400" alt="Image 4">
    <img src="https://picsum.photos/id/1024/600/400" alt="Image 5">
    <img src="https://picsum.photos/id/1035/600/400" alt="Image 6">
</div>

<div class="lightbox" id="lightbox">
    <span class="close">&times;</span>
    <img class="lightbox-img" src="">
</div>

<script src="script.js"></script>
</body>
</html>