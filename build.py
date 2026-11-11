# 5ページの HTML を共通のヘッダー・フッターで書き出す（python3 build.py）
from pathlib import Path

ROOT = Path(__file__).parent

LOGO = '''<svg viewBox="0 0 40 40" aria-hidden="true">
<polygon points="20,3 36,12 20,21 4,12" fill="#5cc8f0"/>
<polygon points="4,12 20,21 20,38 4,29" fill="#1488bb"/>
<polygon points="36,12 20,21 20,38 36,29" fill="#2c62c9"/>
<text x="20" y="17" text-anchor="middle" font-size="10" font-weight="900" fill="#0e1a33" font-family="sans-serif">IF</text>
</svg>'''

PAGES = [
    ("index.html", "トップ"),
    ("about.html", "会社概要"),
    ("service.html", "サービス"),
    ("works.html", "作品"),
]


def header(current):
    links = "".join(
        f'<li><a href="{f}"{" aria-current=\"page\"" if f == current else ""}>{n}</a></li>'
        for f, n in PAGES
    )
    cur = ' aria-current="page"' if current == "contact.html" else ""
    return f'''<p class="notice">本サイトは講義課題として制作したものです。（実在しない仮想企業です）</p>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html">{LOGO}<span>If Channel<small>株式会社イフチャンネル</small></span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">メニュー</button>
    <nav class="nav" id="nav"><ul>{links}<li><a class="nav-cta" href="contact.html"{cur}>お問い合わせ</a></li></ul></nav>
  </div>
</header>'''


FOOTER = '''<footer class="site-footer">
  <div class="wrap">
    <div><b style="color:#fff">株式会社イフチャンネル（仮想企業）</b><br>「もしも」を3Dで見せる、物理シミュレーション動画スタジオ</div>
    <div><a href="index.html">トップ</a><a href="about.html">会社概要</a><a href="service.html">サービス</a><a href="works.html">作品</a><a href="contact.html">お問い合わせ</a></div>
    <p class="copy">本サイトは講義課題として制作したものです。掲載の会社・料金・実績は架空です。作品画像は制作者が自作した3D動画の画面です。<br>&copy; 2026 If Channel (practice)</p>
  </div>
</footer>
<script>
const b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
b.addEventListener('click',()=>{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);b.textContent=o?'閉じる':'メニュー';});
</script>'''


def page(fname, title, desc, body):
    html = f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>【実習】{title}｜If Channel（株式会社イフチャンネル）</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Zen+Kaku+Gothic+New:wght@700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
{header(fname)}
<main>
{body}
</main>
{FOOTER}
</body>
</html>
'''
    (ROOT / fname).write_text(html, encoding="utf-8")


CTA = '''<section class="cta-band">
  <div class="wrap">
    <h2>あなたの「もしも」を、3Dで見てみませんか？</h2>
    <p>授業の教材、商品のPR、イベントの話題づくり。まずは気軽にご相談ください。</p>
    <div class="btns" style="justify-content:center"><a class="btn btn-dark" href="contact.html">無料で相談する</a></div>
  </div>
</section>'''

WORKS = [
    ("air", "もしも、5秒間だけ空気が消えたら？", "消える系", "音も、風も、浮力も消えた5秒間。"),
    ("gravity", "もしも、5秒間だけ重力が消えたら？", "消える系", "台所のお茶わんから街の車まで。"),
    ("rain", "もしも、空の水が全部いっぺんに雨になったら？", "地球スケール", "空にある水の量を実際に計算。"),
    ("jump", "もしも、ジャンプするたびに2倍高く跳べたら？", "どんどん大きくなる", "電柱、ビル、山、そして雲の上へ。"),
    ("freeze", "もしも、5秒で海が凍ったら？", "地球スケール", "港の波が一瞬で止まる。"),
    ("ring", "もしも、地球に土星みたいな輪があったら？", "宇宙", "日本の夜空はどう見える？"),
]


def work_cards(items):
    return "".join(
        f'''<article class="work"><img src="img/{k}.jpg" alt="3D動画「{t}」の画面" loading="lazy" width="405" height="720"><div><span class="tag">{g}</span><h3>{t}</h3><p>{d}</p></div></article>'''
        for k, t, g, d in items
    )


# 自作の図：制作の流れ（横＝PC用、縦＝スマホ用）
STEPS = [("1", "企画", "「もしも」を考える"), ("2", "計算", "本物の物理で数字を出す"),
         ("3", "3D制作", "three.jsで世界を作る"), ("4", "チェック", "ちらつき・音量を機械で確認"),
         ("5", "公開", "YouTubeに毎日2本")]


def flow_h():
    parts = ['<svg class="flow-svg flow-h" viewBox="0 0 1000 190" role="img" aria-label="制作の流れ：企画、計算、3D制作、チェック、公開">']
    for i, (n, t, s) in enumerate(STEPS):
        x = 20 + i * 196
        fill = "#0e1a33" if i % 2 == 0 else "#1488bb"
        parts.append(f'<rect x="{x}" y="30" width="160" height="130" rx="18" fill="{fill}"/>')
        parts.append(f'<circle cx="{x+80}" cy="30" r="20" fill="#ffcf3f"/><text x="{x+80}" y="37" text-anchor="middle" font-size="20" font-weight="900" fill="#0e1a33">{n}</text>')
        parts.append(f'<text x="{x+80}" y="95" text-anchor="middle" font-size="24" font-weight="700" fill="#fff">{t}</text>')
        parts.append(f'<text x="{x+80}" y="128" text-anchor="middle" font-size="13" fill="#c8d5ec">{s}</text>')
        if i < len(STEPS) - 1:
            parts.append(f'<polygon points="{x+166},85 {x+190},95 {x+166},105" fill="#2bb3e8"/>')
    parts.append("</svg>")
    return "".join(parts)


def flow_v():
    parts = ['<svg class="flow-svg flow-v" viewBox="0 0 320 560" role="img" aria-label="制作の流れ：企画、計算、3D制作、チェック、公開">']
    for i, (n, t, s) in enumerate(STEPS):
        y = 10 + i * 110
        fill = "#0e1a33" if i % 2 == 0 else "#1488bb"
        parts.append(f'<rect x="20" y="{y}" width="280" height="84" rx="16" fill="{fill}"/>')
        parts.append(f'<circle cx="58" cy="{y+42}" r="20" fill="#ffcf3f"/><text x="58" y="{y+49}" text-anchor="middle" font-size="20" font-weight="900" fill="#0e1a33">{n}</text>')
        parts.append(f'<text x="94" y="{y+38}" font-size="22" font-weight="700" fill="#fff">{t}</text>')
        parts.append(f'<text x="94" y="{y+64}" font-size="13" fill="#c8d5ec">{s}</text>')
        if i < len(STEPS) - 1:
            parts.append(f'<polygon points="150,{y+90} 170,{y+90} 160,{y+104}" fill="#2bb3e8"/>')
    parts.append("</svg>")
    return "".join(parts)


FLOW = f'<figure class="figure">{flow_h()}{flow_v()}<figcaption>図：If Channel の制作の流れ（自作）</figcaption></figure>'

ICON_SHORT = '<svg class="icon" viewBox="0 0 48 48"><rect x="13" y="4" width="22" height="40" rx="5" fill="#0e1a33"/><polygon points="20,17 30,24 20,31" fill="#2bb3e8"/></svg>'
ICON_EDU = '<svg class="icon" viewBox="0 0 48 48"><polygon points="24,6 46,17 24,28 2,17" fill="#0e1a33"/><path d="M11 22v10c0 4 26 4 26 0V22" fill="#2bb3e8"/></svg>'
ICON_PR = '<svg class="icon" viewBox="0 0 48 48"><path d="M6 20h8l18-10v28L14 28H6z" fill="#0e1a33"/><path d="M36 17c4 3 4 11 0 14" stroke="#2bb3e8" stroke-width="4" fill="none" stroke-linecap="round"/></svg>'

# ---------- トップ ----------
page("index.html", "トップ", "「もしも」を本物の物理で3Dにする、ショート動画スタジオ If Channel（講義課題の仮想企業）", f'''
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow">3D SIMULATION SHORTS STUDIO</span>
      <h1>ありえない「もしも」を、<br><em>本物の物理</em>で見せる。</h1>
      <p class="lead">If Channel は「もしも、5秒間だけ重力が消えたら？」のような思考実験を、実際の物理計算と3DCGで縦型ショート動画にする制作会社です。60秒で「なるほど！」を届けます。</p>
      <div class="btns"><a class="btn btn-primary" href="contact.html">制作を相談する</a><a class="btn btn-ghost" href="works.html">作品を見る</a></div>
    </div>
    <div class="hero-phones">
      <img class="phone" src="img/gravity.jpg" alt="3D動画「もしも、5秒間だけ重力が消えたら？」の画面" width="405" height="720">
      <img class="phone" src="img/jump.jpg" alt="3D動画「もしも、ジャンプするたびに2倍高く跳べたら？」の画面" width="405" height="720">
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="label">FOR WHOM</span><h2>こんな方のための会社です</h2>
    <p>スマホで動画を見る10〜20代に「科学っておもしろい」と感じてもらうこと。それが私たちの目的です。</p></div>
    <div class="grid-3">
      <div class="card"><div class="num">01</div><h3>ショート動画の視聴者</h3><p>すき間時間に、驚きと「へえ」がほしい人へ。毎日7:00と18:00に新作を公開。</p></div>
      <div class="card"><div class="num">02</div><h3>学校・塾の先生</h3><p>重力や気圧など、目に見えない物理を生徒に「見せたい」先生へ。授業用の動画を作ります。</p></div>
      <div class="card"><div class="num">03</div><h3>企業・自治体の広報</h3><p>商品やイベントを「もしも」の切り口で話題にしたい担当者へ。</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="label">SERVICE</span><h2>サービス</h2></div>
    <div class="grid-3">
      <div class="card">{ICON_SHORT}<h3>自社チャンネル運営</h3><p>YouTube ショートで3Dシミュレーション動画を毎日2本公開しています。</p></div>
      <div class="card">{ICON_EDU}<h3>教材動画の制作</h3><p>単元に合わせた「もしも」を企画し、数字の根拠つきで授業用に制作します。</p></div>
      <div class="card">{ICON_PR}<h3>PR動画の制作</h3><p>商品やサービスを主役にした、思わず最後まで見てしまう縦型動画を作ります。</p></div>
    </div>
    <div class="btns"><a class="btn btn-dark" href="service.html">サービスと料金を見る</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="label">NUMBERS</span><h2>数字で見る If Channel</h2></div>
    <div class="stats">
      <div class="stat"><b>2本</b><span>1日に公開する本数</span></div>
      <div class="stat"><b>60秒</b><span>1本の長さの目安</span></div>
      <div class="stat"><b>100%</b><span>出典つきの物理計算</span></div>
      <div class="stat"><b>0人</b><span>動画の中でケガをする人</span></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="label">WORKS</span><h2>最近の作品</h2></div>
    <div class="works">{work_cards(WORKS[:4])}</div>
    <div class="btns"><a class="btn btn-dark" href="works.html">作品をもっと見る</a></div>
  </div>
</section>
{CTA}
''')

# ---------- 会社概要 ----------
page("about.html", "会社概要", "株式会社イフチャンネル（仮想企業）の理念・会社データ・沿革", f'''
<section class="page-hero"><div class="wrap"><span class="eyebrow">ABOUT</span><h1>会社概要</h1><p>「もしも」から、科学をもっと身近に。</p></div></section>

<section>
  <div class="wrap grid-2">
    <div>
      <div class="section-head"><span class="label">MISSION</span><h2>見えない物理を、<br>見えるようにする。</h2></div>
      <p>重力、空気、光の速さ。私たちの毎日を支えているのに、ふだんは目に見えないものがたくさんあります。</p>
      <p>If Channel は「もしもそれが消えたら？」「もしも2倍になったら？」という問いを立て、実際の物理の数字で計算し、3DCGで映像にします。こわがらせるためではなく、「世界ってよくできている」と気づいてもらうためです。</p>
      <p>だから私たちの動画では、誰もケガをしません。壊れるのはモノと景色だけ。最後はいつもの日常に戻って終わります。</p>
    </div>
    <img src="img/air.jpg" alt="3D動画「もしも、5秒間だけ空気が消えたら？」の画面" style="max-width:300px;margin:0 auto;border-radius:16px" width="405" height="720" loading="lazy">
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="label">VALUES</span><h2>大切にしていること</h2></div>
    <div class="grid-3">
      <div class="card"><div class="num">本物</div><h3>数字は本物の物理で</h3><p>公的機関や論文の値をもとに計算し、出典を説明文にのせます。</p></div>
      <div class="card"><div class="num">安心</div><h3>誰も傷つけない</h3><p>災害や戦争を思わせる表現は使いません。人は驚くだけ。</p></div>
      <div class="card"><div class="num">一瞬</div><h3>最初の1秒で引きこむ</h3><p>題名と一番強い場面を冒頭に。2〜3秒ごとに新しい発見を入れます。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="label">COMPANY</span><h2>会社データ</h2></div>
    <table class="info">
      <tr><th>会社名</th><td>株式会社イフチャンネル（If Channel Inc.）※講義課題の仮想企業</td></tr>
      <tr><th>代表者</th><td>代表取締役　○○ ○○</td></tr>
      <tr><th>設立</th><td>2026年11月（架空）</td></tr>
      <tr><th>所在地</th><td>東京都（架空）</td></tr>
      <tr><th>事業内容</th><td>3D物理シミュレーション動画の企画・制作／YouTube ショートチャンネルの運営／教育・広報向け動画の受託制作</td></tr>
      <tr><th>制作環境</th><td>three.js（3DCG）、Python（物理計算・動画の仕上げ）、生成AI（企画・台本づくりの補助）</td></tr>
    </table>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="label">HISTORY</span><h2>沿革</h2></div>
    <ul class="timeline">
      <li><b>2026年11月 はじめ</b><br>「もしも」をテーマにしたショート動画の制作をはじめる</li>
      <li><b>2026年11月9日</b><br>3Dシミュレーション第1作「もしも、5秒間だけ空気が消えたら？」を公開</li>
      <li><b>2026年11月</b><br>毎日2本（7:00・18:00）の公開体制へ。株式会社イフチャンネル設立（架空）</li>
    </ul>
  </div>
</section>
{CTA}
''')

# ---------- サービス ----------
page("service.html", "サービス", "If Channel の3Dシミュレーション動画制作サービス・料金・制作の流れ", f'''
<section class="page-hero"><div class="wrap"><span class="eyebrow">SERVICE</span><h1>サービス・料金</h1><p>企画から公開まで、まとめてお任せください。</p></div></section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="label">WHAT WE DO</span><h2>3つのサービス</h2></div>
    <div class="grid-3">
      <div class="card">{ICON_SHORT}<h3>自社チャンネル「If Channel」</h3><p>毎日7:00と18:00に、3Dの「もしも」動画を YouTube ショートで公開。見るのは無料です。</p></div>
      <div class="card">{ICON_EDU}<h3>教材動画の制作</h3><p>理科・地学の単元に合わせて企画。計算の根拠をまとめた先生用の資料もお渡しします。</p></div>
      <div class="card">{ICON_PR}<h3>PR動画の制作</h3><p>「もしも、この商品が2倍になったら？」など、商品が主役の縦型動画を作ります。</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="label">FLOW</span><h2>制作の流れ</h2><p>ご相談から公開まで、最短2週間。すべての動画で、ちらつきや音量を機械でチェックしてからお渡しします。</p></div>
    {FLOW}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="label">PRICE</span><h2>料金プラン（架空）</h2><p>表示は税込の目安です。内容に合わせてお見積もりします。</p></div>
    <div class="grid-3">
      <div class="card price"><h3>ライト</h3><div class="yen">5万円<small>／1本</small></div><ul><li>30秒の3D動画 1本</li><li>既存のセット（台所・公園・街など）を使用</li><li>修正 1回</li></ul></div>
      <div class="card price featured"><span class="badge">いちばん人気</span><h3>スタンダード</h3><div class="yen">12万円<small>／1本</small></div><ul><li>60秒の3D動画 1本</li><li>オリジナルの企画と物理計算</li><li>出典つきの説明資料</li><li>修正 2回</li></ul></div>
      <div class="card price"><h3>シリーズ</h3><div class="yen">40万円<small>／4本</small></div><ul><li>60秒の3D動画 4本</li><li>新しいセットを1つ制作</li><li>公開スケジュールの提案</li><li>修正 各2回</li></ul></div>
    </div>
    <div class="btns" style="justify-content:center"><a class="btn btn-primary" href="contact.html">見積もりを依頼する</a></div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="label">FAQ</span><h2>よくある質問</h2></div>
    <details><summary>動画の数字は本当に正しいのですか？</summary><p>公的機関や論文の値をもとに計算し、出典を説明文にのせています。ただし「現実には起こらない思考実験」なので、画面にもそう表示します。</p></details>
    <details><summary>こわい表現はありますか？</summary><p>ありません。人がケガをする場面や、災害・戦争を思わせる表現は使いません。小学生にも安心して見せられます。</p></details>
    <details><summary>横長の動画も作れますか？</summary><p>はい。授業でプロジェクターに映す場合などは、横長（16:9）でもお作りします。</p></details>
  </div>
</section>
{CTA}
''')

# ---------- 作品 ----------
page("works.html", "作品", "If Channel が制作した3Dシミュレーション動画の作品一覧", f'''
<section class="page-hero"><div class="wrap"><span class="eyebrow">WORKS</span><h1>作品</h1><p>すべて自社で企画・計算・3D制作した動画です。</p></div></section>

<section>
  <div class="wrap">
    <div class="section-head"><span class="label">3D SHORTS</span><h2>3Dシミュレーション動画</h2>
    <p>縦型（1080×1920）・60秒前後。冒頭に題名とカウントダウン、最後は日常に戻って終わります。</p></div>
    <div class="works">{work_cards(WORKS)}</div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head"><span class="label">TYPES</span><h2>動画の3つの型</h2></div>
    <div class="grid-3">
      <div class="card"><div class="num">消える系</div><h3>5秒だけ〇〇が消えたら</h3><p>あたりまえにあるもの（空気・重力）が一瞬なくなり、その大切さに気づく型。</p></div>
      <div class="card"><div class="num">2倍系</div><h3>どんどん大きくなる</h3><p>1回ごとに2倍。電柱→ビル→山と、たとえがどんどん大きくなる型。</p></div>
      <div class="card"><div class="num">異変系</div><h3>小さな異変から大事件へ</h3><p>台所の小さなおかしな出来事が、最後は地球規模の景色につながる型。</p></div>
    </div>
  </div>
</section>
{CTA}
''')

# ---------- お問い合わせ ----------
page("contact.html", "お問い合わせ", "If Channel への制作のご相談・お問い合わせ", '''
<section class="page-hero"><div class="wrap"><span class="eyebrow">CONTACT</span><h1>お問い合わせ</h1><p>制作のご相談・お見積もりは、こちらのフォームからどうぞ。</p></div></section>

<section>
  <div class="wrap grid-2" style="align-items:start">
    <div>
      <div class="section-head"><span class="label">HOW IT WORKS</span><h2>ご相談の流れ</h2></div>
      <ul class="timeline">
        <li><b>1. フォームを送る</b><br>見たい「もしも」や目的を、ざっくりで大丈夫です。</li>
        <li><b>2. 2営業日以内にご返信</b><br>企画のたたき台と料金の目安をお送りします。</li>
        <li><b>3. オンラインで打ち合わせ</b><br>30分ほどで内容と公開日を決めます。</li>
      </ul>
      <p class="form-note">※本サイトは講義課題です。フォームは見本のため、送信しても内容はどこにも届きません。個人情報は入力しないでください。</p>
    </div>
    <form class="contact" id="contactForm">
      <label>お名前<span class="req">必須</span><input type="text" name="name" required autocomplete="off" placeholder="例）山田 花子"></label>
      <label>ご所属<input type="text" name="org" autocomplete="off" placeholder="例）〇〇中学校／〇〇株式会社"></label>
      <label>ご相談の種類<span class="req">必須</span>
        <select name="type" required><option value="">選んでください</option><option>教材動画の制作</option><option>PR動画の制作</option><option>チャンネルへの感想・テーマのリクエスト</option><option>その他</option></select></label>
      <label>見てみたい「もしも」・ご相談内容<span class="req">必須</span><textarea name="msg" rows="5" required placeholder="例）もしも、教室の空気が5秒だけなくなったら？を授業で使いたい"></textarea></label>
      <button class="btn btn-primary" type="submit" style="border:0;cursor:pointer;justify-self:start">内容を確認して送信</button>
      <p class="form-msg" id="formMsg" role="status">ありがとうございます。（課題用の見本のため、実際には送信されていません）</p>
    </form>
  </div>
</section>
<script>
document.getElementById('contactForm').addEventListener('submit',e=>{e.preventDefault();e.target.reset();document.getElementById('formMsg').style.display='block';});
</script>
''')

print("built")
