<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Video Zone - Watch Now</title>
<style>
body{margin:0;background:#0f0f0f;color:#fff;font-family:Arial}
header{background:#000;padding:15px 20px;display:flex;justify-content:space-between;align-items:center}
header h1{color:#ff0000;margin:0;font-size:24px}
header input{padding:8px;width:200px;border-radius:20px;border:none}
.menu{padding:10px 20px;display:flex;gap:10px}
.menu button{background:#222;color:#fff;border:none;padding:8px 15px;border-radius:20px;cursor:pointer}
.menu button:hover{background:red}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:15px;padding:20px}
.card{background:#1a1a1a;border-radius:10px;overflow:hidden}
.card img{width:100%;height:140px;object-fit:cover}
.card-body{padding:12px}
.card-body h3{margin:0 0 5px 0;font-size:16px}
.card-body p{color:#aaa;font-size:13px;margin:0 0 10px 0}
.watch{display:block;text-align:center;background:red;color:#fff;text-decoration:none;padding:10px;border-radius:6px;font-weight:bold}
.watch:hover{background:#c00}
</style>
</head>
<body>

<header>
<h1>VIDEO ZONE</h1>
<input type="text" placeholder="Search Video...">
</header>

<div class="menu">
<button>All</button>
<button>Movie</button>
<button>Sports</button>
<button>Funny</button>
</div>

<div class="grid">

<!-- 1 নম্বর ভিডিও - এখানে তোমার লিংক বসাও -->
<div class="card">
<img src="https://via.placeholder.com/400x220?text=Video+1" alt="video">
<div class="card-body">
<h3>ভিডিওর নাম এখানে লিখো ১</h3>
<p>10K views • 2 days ago</p>
<a class="watch" href="https://google.com" target="_blank">▶ Watch Now</a>
</div>
</div>

<!-- 2 নম্বর ভিডিও -->
<div class="card">
<img src="https://via.placeholder.com/400x220?text=Video+2" alt="video">
<div class="card-body">
<h3>ভিডিওর নাম এখানে লিখো ২</h3>
<p>25K views • 1 day ago</p>
<a class="watch" href="https://google.com" target="_blank">▶ Watch Now</a>
</div>
</div>

<!-- 3 নম্বর ভিডিও -->
<div class="card">
<img src="https://via.placeholder.com/400x220?text=Video+3" alt="video">
<div class="card-body">
<h3>ভিডিওর নাম এখানে লিখো ৩</h3>
<p>50K views • 5 hours ago</p>
<a class="watch" href="https://google.com" target="_blank">▶ Watch Now</a>
</div>
</div>

<!-- 4 নম্বর ভিডিও -->
<div class="card">
<img src="https://via.placeholder.com/400x220?text=Video+4" alt="video">
<div class="card-body">
<h3>ভিডিওর নাম এখানে লিখো ৪</h3>
<p>8K views • 1 week ago</p>
<a class="watch" href="https://google.com" target="_blank">▶ Watch Now</a>
</div>
</div>

</div>

</body>
</html>