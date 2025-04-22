def tpl_run(text):
    return tpl_header + text + tpl_footer


tpl_home = """

<div class = "grid">
<div>
<h3>Зорилго</h3>
<p>Статистикийн үндсэн арга, техникээр асуудал шийдвэрлэж сурах</p>
</div>

<div>
<figure style="text-align: center;">
<img src="https://auth.num.edu.mn/oauth2/Image/num-logo.svg" alt="Minimal landscape"style="width:90%; height:auto;">        
</figure>
</div>
</div>
<hr>

<h4>Товч агуулга</h4>
<p>Өгөгдөлтэй ажиллах, магадлал, дискрет санамсаргүй хэмжигдэхүүн, тасралтгүй санамсаргүй хэмжигдэхүүн, бином тархалт, Пуассоны тархалт, нормаль тархалт, статистик үнэлгээ, таамаглал шалгах, корреляци, шугаман корреляци, хи-квадрат шинжүүр, симуляци</p>


"""

tpl_poisson = """
<h3>Пуассоны тархалт</h3>

<div class="grid">

<div>
<article>
    Пуассоны тархалт нь цаг хугацаа эсвэл орон зайд тогтмол интервал дотор тодорхой тооны үйл явдлууд тохиолдох магадлалыг илэрхийлдэг, дискрет магадлалын тархалт юм.
    <footer class ="math">\[ P(X = k) = \\frac{\lambda^k e^{-\lambda}}{k!} \]</footer>
</article>
</div>

<div>
<form action="/poisson" method="post">
<fieldest role = "group">
    <p data-tooltip="𝜆 - параметр"><input type="text" name="P_x" placeholder="𝜆" aria-label="text"></p>
    <p data-tooltip="a - доод хил"><input type="text" name="P_a" placeholder="a" aria-label="text"></p>
    <p data-tooltip="b - дээд хил"><input type="text" name="P_b" placeholder="b" aria-label="text"></p>
    <button type="submit" class="contrast" >Илгээх</button>
</fieldest>
</form>


"""

tpl_image = """
<img src = "/figure/{}">
</div>
</div>
"""

tpl_return = """
<h4>Үр дүн</h4>
<div>{}</div>

"""

tpl_binomial = """
<h3>Бином тархалт </h3>

<div class="grid">

<article>
    Бином тархалт нь амжилт, бүтэлгүйтэл гэсэн хоёр үр дүнтэй ба нийт туршилтаас амжилт илэрсэн туршилтуудийг загварчилдаг  дискрет магадлалын тархалт юм.
        <footer class ="math">\[ P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k} \]</footer>
</article>
<div>
<form action="/binomial" method="post">
<fieldest role = "group">
    <p data-tooltip="n - нийт туршилт"><input type="text" name="P_n" placeholder="n" aria-label="text"></p>
    <p data-tooltip="p - магадлал"><input type="text" name="P_p" placeholder="p" aria-label="Text"></p>
    <p data-tooltip="a - доод хил"><input type="text" name="P_a" placeholder="a" aria-label="text"></p>
    <p data-tooltip="b - дээд хил"><input type="text" name="P_b" placeholder="b" aria-label="text"></p>
    <button type="submit" class="contrast">Submit</button>
</fieldest>
</form>

"""

tpl_bin_image = """
<img src = "/figure_bin/{}/{}">
</div>
</div>
"""

tpl_normal = """
<h3> Нормал тархалт </h3>

<div class="grid">
<div>
<article>
    Нормал тархалт нь дундаж, медиан, моод бүгд тэнцүү ба хонх хэлбэртэй муруйгаар дүрслэгддэг.
        <footer class="math">\[ f(x) = \\frac{1}{\sigma \sqrt{2 \pi}} e^{-\\frac{(x - \mu)2}{2\sigma2}} \]</footer>
</article>
</div>
<div>

<form action="/normal" method="post">
<fieldest role = "group">
    <p data-tooltip = "μ - дундаж"><input type="text" name="P_mu" placeholder="μ" aria-label="Text"></p>
    <p data-tooltip = "σ - стандарт хазайлт"><input type="text" name="P_sygma" placeholder="σ" aria-label="text"></p>
    <p data-tooltip = "a - доод хил"><input type="text" name="P_a" placeholder="a" aria-label="text"></p>
    <p data-tooltip = "b - дээд хил "><input type="text" name="P_b" placeholder="b" aria-label="text"></p>
    <button type="submit" class="contrast">Submit</button>
</fieldest>

""" 

tpl_nor_image = """
<img src = "/figure_nor/{}/{}">
</div>
</div>
"""

tpl_geometric = """
<h3> Геометр тархалт </h3>
<div class="grid">
<div>
<article>
    Геометр тархалт нь санамсаргүй хувьсагчийг ашиглан анхны амжилт гарсан туршилтыг загварчилдаг дискрет магадлалын тархалт юм.
        <footer class ="math">\[ P(X = k) = (1 - p)^{k-1} p \]</footer>
</article>
</div>
<div>

<form action="/geometric" method="post">
<fieldest role = "group">
    <p data-tooltip = "p - магадлал"><input type="text" name="P_p" placeholder="p" aria-label="Text"></p>
    <p data-tooltip = "x - хувьсагч"><input type="text" name="P_x" placeholder="x" aria-label="text"></p>
    <p data-tooltip = "a - хилийн утга"><input type="text" name="P_a" placeholder="a" aria-label="text"></p>
    <button type="submit" class="contrast">Submit</button>
</fieldest>
</form>

"""

tpl_geo_image = """
<img src = "/figure_geo/{}">
</div>
</div>
"""

# Header and Footer
tpl_header = """
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="color-scheme" content="light dark">
<link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
    <link rel="stylesheet"href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.conditional.min.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.15/dist/katex.min.css" integrity="sha384-Htz9HMhiwV8GuQ28Xr9pEs1B4qJiYu/nYLLwlDklR53QibDfmQzi7rYxXhMH/5/u" crossorigin="anonymous">
    <title>Статистик MAED304 : Монгол Улсын Их Сургууль </title>
</head>
<body>

<nav class="container">
<ul>
    <li>Статистик - <strong>MAED304</strong></li>
</ul>
<ul>
    <li><a href="/">Нүүр</a></li>
    <li><a href="/poisson">Пуассон</a></li>
    <li><a href="/normal">Нормал</a></li>
    <li><a href="/binomial">Бином</a></li>
    <li><a href="/geometric">Геометр</a></li>
</ul>
</nav>
<main class="container">

"""

tpl_footer = """
<footer> <p style = "text-align: right;">&copy; 2024 А.Амарзаяа, Ц.Ариунболд</p> </footer>
    </main>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.15/dist/katex.min.js" integrity="sha384-bxmi2jLGCvnsEqMuYLKE/KsVCxV3PqmKeK6Y6+lmNXBry6+luFkEOsmp5vD9I/7+" crossorigin="anonymous"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.15/dist/contrib/auto-render.min.js" integrity="sha384-hCXGrW6PitJEwbkoStFjeJxv+fSOOQKOPbJxSfM6G5sWZjAyWhXiTIIAmQqnlLlh" crossorigin="anonymous"
        onload="renderMathInElement(document.body);"></script>

        </body>
</html>
"""
