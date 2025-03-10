<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Services - Black Alliance</title>
 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
 <style>
 :root{
            --background-image-url: url('/static/images/bg.jpg');
        }
    </style>
 <link rel="stylesheet" href="/static/css/main.css">
 <link rel="stylesheet" href="/static/css/animation.css">
</head>
<body>
 <nav class="navbar p-4 shadow-md">
 <div class="container mx-auto flex justify-between items-center">
 <div class="text-2xl text-primary">Black Alliance ♚</div>
 <div class="hidden lg:flex navbar-menu">
 <a href="/" class="hover:text-primary">Home</a>
 <a href="/team" class="hover:text-primary">Team</a>
 <a href="/services" class="hover:text-primary">Services</a>
 <a href="/status" class="hover:text-primary">Status</a>
 <a href="/pricing" class="hover:text-primary">Pricing</a>
 <a href="/contact" class="hover:text-primary">Contact</a>
 </div>
 <div class="lg:hidden">
 <span id="menu-btn" class="navbar-icon text-2xl">
 <i class="fas fa-bars"></i>
 </span>
 </div>
 </div>
 </nav>
 <div id="sidebar" class="fixed inset-0 bg-white text-gray-800 lg:hidden">
 <div class="w-64 h-full p-4">
 <ul class="space-y-6">
 <li><a href="/" class="hover:text-primary">Home</a></li>
 <li><a href="/team" class="hover:text-primary">Team</a></li>
 <li><a href="/services" class="hover:text-primary">Services</a></li>
 <li><a href="/status" class="hover:text-primary">Status</a></li>
 <li><a href="/pricing" class="hover:text-primary">Pricing</a></li>
 <li><a href="/contact" class="hover:text-primary">Contact</a></li>
 </ul>
 </div>
 </div>
 
 

<header class="bg-header shadow-lg flex items-center justify-center text-center"></header>

<div class="container mx-auto px-4 py-16">
 <section id="cards">
 <h2 class="text-3xl font-bold text-center text-primary mb-8">Our Services</h2>
 <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
 
 <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
 <div class="card-img service mt-4 mb-4">
 <img src="/static/images/convo.jpg" alt="𝘊𝘩𝘢𝘵 𝘛𝘰𝘰𝘭">
 </div>
 <div class="status-indicators status-active">
 <span class="circle"></span>
 <span class="circle"></span>
 <span class="circle"></span>
 </div>
 <h3 class="text-2xl font-bold text-primary mb-4">𝘊𝘩𝘢𝘵 𝘛𝘰𝘰𝘭</h3>
 <p>Ultimate Facebook Messages sender tool.</p>
 <a href="/service/chat" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
 </div>
 
 <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
 <div class="card-img service mt-4 mb-4">
 <img src="/static/images/post.jpg" alt="𝘊𝘰𝘮𝘮𝘦𝘯𝘵𝘴 𝘛𝘰𝘰𝘭">
 </div>
 <div class="status-indicators status-active">
 <span class="circle"></span>
 <span class="circle"></span>
 <span class="circle"></span>
 </div>
 <h3 class="text-2xl font-bold text-primary mb-4">𝘊𝘰𝘮𝘮𝘦𝘯𝘵𝘴 𝘛𝘰𝘰𝘭</h3>
 <p>Facebook Post Comments Tool By Cookies.</p>
 <a href="/service/post" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
 </div>
 
 <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
 <div class="card-img service mt-4 mb-4">
 <img src="/static/images/postv2.jpg" alt="𝘊𝘰𝘮𝘮𝘦𝘯𝘵𝘴 𝘛𝘰𝘰𝘭 𝘝2">
 </div>
 <div class="status-indicators status-active">
 <span class="circle"></span>
 <span class="circle"></span>
 <span class="circle"></span>
 </div>
 <h3 class="text-2xl font-bold text-primary mb-4">𝘊𝘰𝘮𝘮𝘦𝘯𝘵𝘴 𝘛𝘰𝘰𝘭 𝘝2</h3>
 <p>Facebook Post Comments Tool v2 By Tokens.</p>
 <a href="/service/postv2" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
 </div>
 
 <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
 <div class="card-img service mt-4 mb-4">
 <img src="/static/images/2fa.jpg" alt="2𝘍𝘈 𝘓𝘪𝘷𝘦">
 </div>
 <div class="status-indicators status-active">
 <span class="circle"></span>
 <span class="circle"></span>
 <span class="circle"></span>
 </div>
 <h3 class="text-2xl font-bold text-primary mb-4">2𝘍𝘈 𝘓𝘪𝘷𝘦</h3>
 <p>Get OTP Code Live using 2FA Live.</p>
 <a href="/service/2fa" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
 </div>
 
 <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
 <div class="card-img service mt-4 mb-4">
 <img src="/static/images/checker.jpg" alt="𝘊𝘩𝘦𝘤𝘬𝘦𝘳 𝘛𝘰𝘰𝘭">
 </div>
 <div class="status-indicators status-active">
 <span class="circle"></span>
 <span class="circle"></span>
 <span class="circle"></span>
 </div>
 <h3 class="text-2xl font-bold text-primary mb-4">𝘊𝘩𝘦𝘤𝘬𝘦𝘳 𝘛𝘰𝘰𝘭</h3>
 <p>Check Multiple Tokens, Cookies, Multiple ID&#39;s using Checker Tool</p>
 <a href="/service/checker" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
 </div>
 
 <div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
 <div class="card-img service mt-4 mb-4">
 <img src="/static/images/token.jpg" alt="𝘛𝘰𝘬𝘦𝘯 𝘌𝘹𝘵𝘳𝘢𝘤𝘵𝘰𝘳">
 </div>
 <div class="status-indicators status-active">
 <span class="circle"></span>
 <span class="circle"></span>
 <span class="circle"></span>
 </div>
 <h3 class="text-2xl font-bold text-primary mb-4">𝘛𝘰𝘬𝘦𝘯 𝘌𝘹𝘵𝘳𝘢𝘤𝘵𝘰𝘳</h3>
 <p>Profile &amp; Page Token Extractor using Cookies</p>
 <a href="/service/token" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
 </div>
 
 </div>
 </section>
</div>

 <footer class="footer py-6">
 <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
 <div class="mb-4 md:mb-0">
 <a href="/terms" class="hover:text-primary">Terms</a>
 <span class="mx-2">|</span>
 <a href="/privacy" class="hover:text-primary">Privacy</a>
 </div>
 
 <div name="links" class="flex space-x-4">
 <a href="https://www.facebook.com/Mr.Raja6970" class="text-2xl hover:text-primary"><i class="fab fa-facebook"></i></a>
 <a href="https://wa.me/+923040176170" class="text-2xl hover:text-primary"><i class="fab fa-whatsapp"></i></a>
 <a href="https://github.com" class="text-2xl hover:text-primary"><i class="fab fa-github"></i></a>
 </div>
 
 <div class="mt-4 md:mt-0 text-center">
 <p>© 2024 Black Alliance. All Rights Reserved.</p>
 <p>Made with ❤️ by <a href="https://www.facebook.com/i.farhanali.dev">Farhan Ali</a></p>
 </div>
 </div>
 </footer>
 
 <script src="/static/js/menu.js"></script>
    
    
</body>
</html>
