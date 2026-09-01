from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mahi97.github.io"

WORKS = [
    {
        "slug": "elsaa",
        "title": "ELSAA: Efficient Low-Rank and Sparse Attention Approximation for Training Transformers",
        "authors": ["Mahdi Heidari", "Mohammad Mahdi Rahimi", "Jaekyun Moon"],
        "date": "2026/07/22",
        "year": "2026",
        "venue": "arXiv:2607.20214 [cs.LG]",
        "venue_meta": ("citation_technical_report_number", "arXiv:2607.20214"),
        "extra_meta": [("citation_arxiv_id", "2607.20214")],
        "doi": "10.48550/arXiv.2607.20214",
        "official_url": "https://arxiv.org/abs/2607.20214",
        "abstract": "The quadratic N × N attention score matrix remains a central obstacle to extending Transformers to longer input lengths. Existing efficient attention methods usually reduce this bottleneck by either imposing sparsity, so that each query attends to only a small subset of keys, or by using low-rank or kernel sketches, so that global interactions are compressed into a lower-dimensional representation. We propose ELSAA, an efficient low-rank and sparse approximation of attention. ELSAA approximates the induced attention score operator itself: a sparse branch captures selected high-similarity interactions, while a low-rank branch summarizes diffuse global interactions. A denominator-aware fusion term scales the sparse branch according to its estimated attention mass relative to the low-rank branch. This provides a practical framework for constructing low-rank and sparse attention outputs without materializing the full quadratic score matrix.",
        "citation": "Heidari, M., Rahimi, M. M., & Moon, J. (2026). ELSAA: Efficient Low-Rank and Sparse Attention Approximation for Training Transformers. arXiv:2607.20214.",
        "bibtex": """@misc{heidari2026elsaa,\n  title = {ELSAA: Efficient Low-Rank and Sparse Attention Approximation for Training Transformers},\n  author = {Heidari, Mahdi and Rahimi, Mohammad Mahdi and Moon, Jaekyun},\n  year = {2026},\n  eprint = {2607.20214},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.LG},\n  doi = {10.48550/arXiv.2607.20214}\n}""",
    },
    {
        "slug": "evofed",
        "title": "EvoFed: Leveraging Evolutionary Strategies for Communication-Efficient Federated Learning",
        "authors": ["Mohammad Mahdi Rahimi", "Hasnain Irshad Bhatti", "Younghyun Park", "Humaira Kousar", "Jaekyun Moon"],
        "date": "2023/12/10",
        "year": "2023",
        "venue": "Advances in Neural Information Processing Systems 36 (NeurIPS 2023)",
        "venue_meta": ("citation_conference_title", "Advances in Neural Information Processing Systems 36 (NeurIPS 2023)"),
        "extra_meta": [("citation_volume", "36")],
        "doi": "10.52202/075280-2726",
        "official_url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/c48fe446e651cd49fb58a6833e015103-Abstract-Conference.html",
        "code_url": "https://github.com/mahi97/EvoFL",
        "abstract": "Federated Learning (FL) is a decentralized machine learning paradigm that enables collaborative model training across dispersed nodes without forcing individual nodes to share data. Its broad adoption is hindered by the high communication costs of transmitting a large number of model parameters. EvoFed integrates Evolutionary Strategies with FL through fitness-based information sharing. Rather than exchanging updated model parameters, each node transmits distance-based similarity measures between its locally updated model and a synchronized population of noise-perturbed models. The server aggregates these fitness values to update the global model. The analysis establishes convergence, and experiments show performance comparable to FedAvg while drastically reducing communication requirements in practical settings.",
        "citation": "Rahimi, M. M., Bhatti, H. I., Park, Y., Kousar, H., & Moon, J. (2023). EvoFed: Leveraging Evolutionary Strategies for Communication-Efficient Federated Learning. Advances in Neural Information Processing Systems, 36.",
        "bibtex": """@inproceedings{rahimi2023evofed,\n  title = {EvoFed: Leveraging Evolutionary Strategies for Communication-Efficient Federated Learning},\n  author = {Rahimi, Mohammad Mahdi and Bhatti, Hasnain Irshad and Park, Younghyun and Kousar, Humaira and Moon, Jaekyun},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {36},\n  year = {2023},\n  doi = {10.52202/075280-2726}\n}""",
    },
    {
        "slug": "thesis",
        "title": "Communication-efficient Federated Learning",
        "authors": ["Mohammad Mahdi Rahimi"],
        "date": "2025",
        "year": "2025",
        "venue": "Ph.D. dissertation, Korea Advanced Institute of Science and Technology (KAIST)",
        "venue_meta": ("citation_dissertation_institution", "Korea Advanced Institute of Science and Technology"),
        "official_url": "https://library.kaist.ac.kr/search/detail/view.do?bibCtrlNo=1142925&flag=dissertation",
        "abstract": "Advances in deep learning have revolutionized numerous fields, yet deploying these models often requires aggregating massive datasets in a central location, raising critical privacy and scalability concerns. Federated Learning addresses this by enabling collaborative model training directly on distributed client devices without sharing private data. This thesis addresses communication overhead, computational inefficiency, client heterogeneity, and personalization through three contributions: EvoFed, an evolutionary-strategy-based method that exchanges compact fitness similarity metrics; Model-Agnostic Projection Adaptation, a unified low-rank factorization method that compresses the model parameter space; and Principal-Aligned LoRA, a personalized approach that uses singular value decomposition to align client-specific updates. Together, these methods improve the efficiency, scalability, and personalization of federated learning.",
        "citation": "Rahimi, M. M. (2025). Communication-efficient Federated Learning [Ph.D. dissertation, Korea Advanced Institute of Science and Technology].",
        "bibtex": """@phdthesis{rahimi2025communication,\n  title = {Communication-efficient Federated Learning},\n  author = {Rahimi, Mohammad Mahdi},\n  school = {Korea Advanced Institute of Science and Technology},\n  year = {2025},\n  type = {Ph.D. dissertation}\n}""",
    },
    {
        "slug": "xqmix",
        "title": "XQMIX: Extended QMix for StarCraft Multi-Agent Challenge",
        "authors": ["Mohammad Mahdi Rahimi"],
        "date": "2021/02/14",
        "year": "2021",
        "venue": "Technical report, Korea Advanced Institute of Science and Technology (KAIST)",
        "venue_meta": ("citation_technical_report_institution", "Korea Advanced Institute of Science and Technology"),
        "doi": "10.13140/RG.2.2.23575.91040",
        "official_url": "https://www.researchgate.net/publication/349296708_XQMIX_Extended_QMix_for_StarCraft_Multi-Agent_Challenge",
        "code_url": "https://github.com/mahi97/XQMIX",
        "abstract": "This report describes improvements to decentralized multi-agent learning for the StarCraft II Multi-Agent Challenge. The principal additions are multi-step learning and noisy networks. Other evaluated changes include the optimizer, learning-rate decay schedule, loss functions, and regularization. The report analyzes which changes improve upon the QMIX baseline and where additional hyperparameter tuning is required.",
        "citation": "Rahimi, M. M. (2021). XQMIX: Extended QMix for StarCraft Multi-Agent Challenge. Technical report, KAIST. https://doi.org/10.13140/RG.2.2.23575.91040",
        "bibtex": """@techreport{rahimi2021xqmix,\n  title = {XQMIX: Extended QMix for StarCraft Multi-Agent Challenge},\n  author = {Rahimi, Mohammad Mahdi},\n  institution = {Korea Advanced Institute of Science and Technology},\n  year = {2021},\n  doi = {10.13140/RG.2.2.23575.91040}\n}""",
    },
    {
        "slug": "opem",
        "title": "OPEM: Open Source PEM Cell Simulation Tool",
        "authors": ["Sepand Haghighi", "Kasra Askari", "Sarmin Hamidi", "Mohammad Mahdi Rahimi"],
        "date": "2018/07/22",
        "year": "2018",
        "venue": "Journal of Open Source Software, 3(27), 676",
        "venue_meta": ("citation_journal_title", "Journal of Open Source Software"),
        "extra_meta": [("citation_volume", "3"), ("citation_issue", "27"), ("citation_firstpage", "676"), ("citation_issn", "2475-9066")],
        "doi": "10.21105/joss.00676",
        "official_url": "https://joss.theoj.org/papers/10.21105/joss.00676",
        "code_url": "https://github.com/ECSIM/opem",
        "abstract": "OPEM is an open-source modeling tool for evaluating proton-exchange membrane fuel cells. It combines static and dynamic models that accept operating variables and cell parameters, predict the performance of PEM fuel cells, and produce CSV, HTML, and OPEM outputs. The package is implemented in Python and provides a platform for collaborative development of PEM fuel-cell models.",
        "citation": "Haghighi, S., Askari, K., Hamidi, S., & Rahimi, M. M. (2018). OPEM: Open Source PEM Cell Simulation Tool. Journal of Open Source Software, 3(27), 676. https://doi.org/10.21105/joss.00676",
        "bibtex": """@article{haghighi2018opem,\n  title = {OPEM: Open Source PEM Cell Simulation Tool},\n  author = {Haghighi, Sepand and Askari, Kasra and Hamidi, Sarmin and Rahimi, Mohammad Mahdi},\n  journal = {Journal of Open Source Software},\n  volume = {3},\n  number = {27},\n  pages = {676},\n  year = {2018},\n  doi = {10.21105/joss.00676}\n}""",
    },
    {
        "slug": "parsian-2019",
        "title": "PARSIAN 2019 Extended Team Description Paper",
        "authors": ["Kian Behzad", "Elham Daneshmand", "Nadia Moradi", "Mahdi Hajmohammadi Onidin", "Mohammad Reza Kolani", "Yasamin Alizadeh Gharib", "Atiyeh Pirmoradi", "Mohammad Mahdi Rahimi", "Mohammad Mahdi Shirazi", "Mohammad Azam Khosravi"],
        "date": "2019",
        "year": "2019",
        "venue": "RoboCup Small Size League Extended Team Description Papers",
        "venue_meta": ("citation_conference_title", "RoboCup 2019 Small Size League"),
        "official_url": "https://ssl.robocup.org/wp-content/uploads/2019/03/2019_ETDP_Parsian.pdf",
        "abstract": "This paper illustrates mechanical, electronics, control, and software improvements made by the Parsian Small Size Soccer team since the previous year. The work covers the dribbler system, electronic and software cooperation, computational-geometry path planning, inverse modeling of robot kinematics, log-analyzer development, and learning opponent defense strategies.",
        "citation": "Behzad, K., Daneshmand, E., Moradi, N., et al. (2019). PARSIAN 2019 Extended Team Description Paper. RoboCup Small Size League.",
        "bibtex": """@techreport{behzad2019parsian,\n  title = {PARSIAN 2019 Extended Team Description Paper},\n  author = {Behzad, Kian and Daneshmand, Elham and Moradi, Nadia and Hajmohammadi Onidin, Mahdi and Kolani, Mohammad Reza and Alizadeh Gharib, Yasamin and Pirmoradi, Atiyeh and Rahimi, Mohammad Mahdi and Shirazi, Mohammad Mahdi and Khosravi, Mohammad Azam},\n  institution = {RoboCup Small Size League},\n  year = {2019}\n}""",
    },
    {
        "slug": "parsian-2018",
        "title": "PARSIAN 2018 Extended Team Description Paper",
        "authors": ["Mohammad Mahdi Rahimi", "Mohammad Mahdi Shirazi", "Mohammad Amin Najaf Gholyan", "Fateme Hashemi Chaleshtori", "Nadia Moradi", "Kian Behzad", "Seyed Hamidreza Roodabeh", "Ali Gavahi", "Fateme Farokhi Moghadam", "Seyed Ali Ghazi Asgar", "Yasamin Alizadeh Gharib", "Mahshid Memarian", "Amir Hadi Tavakoli", "Mohammad Azam Khosravi"],
        "date": "2018",
        "year": "2018",
        "venue": "RoboCup Small Size League Extended Team Description Papers",
        "venue_meta": ("citation_conference_title", "RoboCup 2018 Small Size League"),
        "official_url": "https://ssl.robocup.org/wp-content/uploads/2019/01/2018_ETDP_Parsian.pdf",
        "abstract": "This paper presents Parsian's hardware elaboration, software architecture, and improvements since the previous year. Hardware innovations include a new ball-detection sensor, debugger module, and robot fault recovery. Software enhancements include a microservice architecture based on ROS, open-loop motion correction, a motion profiler, and a new obstacle-avoidance strategy.",
        "citation": "Rahimi, M. M., Shirazi, M. M., Gholyan, M. A. N., et al. (2018). PARSIAN 2018 Extended Team Description Paper. RoboCup Small Size League.",
        "bibtex": """@techreport{rahimi2018parsian,\n  title = {PARSIAN 2018 Extended Team Description Paper},\n  author = {Rahimi, Mohammad Mahdi and Shirazi, Mohammad Mahdi and Najaf Gholyan, Mohammad Amin and Hashemi Chaleshtori, Fateme and Moradi, Nadia and Behzad, Kian and Roodabeh, Seyed Hamidreza and Gavahi, Ali and Farokhi Moghadam, Fateme and Ghazi Asgar, Seyed Ali and Alizadeh Gharib, Yasamin and Memarian, Mahshid and Tavakoli, Amir Hadi and Khosravi, Mohammad Azam},\n  institution = {RoboCup Small Size League},\n  year = {2018}\n}""",
    },
    {
        "slug": "parsian-2017",
        "title": "PARSIAN 2017 Extended Team Description Paper",
        "authors": ["Mohammad Mahdi Rahimi", "Mohammad Mahdi Shirazi", "Maziar Arfaee", "Mohammad Amin Najaf Gholian", "Amir Hossein Zamani", "Hamed Hosseini", "Fateme Hashemi Chaleshtori", "Nadia Moradi", "Atousa Ahsani", "Mahmoud Jafari", "Amin Zahedi", "Parsa Abdollahi", "Alireza Zolanvari", "Mohammad Azam Khosravi"],
        "date": "2017",
        "year": "2017",
        "venue": "RoboCup Small Size League Extended Team Description Papers",
        "venue_meta": ("citation_conference_title", "RoboCup 2017 Small Size League"),
        "official_url": "https://ssl.robocup.org/wp-content/uploads/2019/01/2017_ETDP_Parsian.pdf",
        "abstract": "This paper describes improvements to Parsian robots' hardware and software architecture. Hardware developments include fault detection, two-way communication, and the dribbler system. Software developments include pass and interception skills, an adaptive attack strategy for regular play, and reactive offense and defense for free kicks.",
        "citation": "Rahimi, M. M., Shirazi, M. M., Arfaee, M., et al. (2017). PARSIAN 2017 Extended Team Description Paper. RoboCup Small Size League.",
        "bibtex": """@techreport{rahimi2017parsian,\n  title = {PARSIAN 2017 Extended Team Description Paper},\n  author = {Rahimi, Mohammad Mahdi and Shirazi, Mohammad Mahdi and Arfaee, Maziar and Najaf Gholian, Mohammad Amin and Zamani, Amir Hossein and Hosseini, Hamed and Hashemi Chaleshtori, Fateme and Moradi, Nadia and Ahsani, Atousa and Jafari, Mahmoud and Zahedi, Amin and Abdollahi, Parsa and Zolanvari, Alireza and Khosravi, Mohammad Azam},\n  institution = {RoboCup Small Size League},\n  year = {2017}\n}""",
    },
    {
        "slug": "parsian-2016",
        "title": "PARSIAN Extended Team Description for RoboCup 2016",
        "authors": ["Mohammad Mahdi Rahimi", "Mohammad Mahdi Shirazi", "Seyede Parisa Dajkhosh", "Alireza Zolanvari", "Maziar Arfaee", "Hamidreza Kazemi Khoshkijari", "Amirhossein Abbasi Fashami", "Alireza Saeidi Shahrivar", "Mohammad Azam Khosravi"],
        "date": "2016",
        "year": "2016",
        "venue": "RoboCup Small Size League Extended Team Description Papers",
        "venue_meta": ("citation_conference_title", "RoboCup 2016 Small Size League"),
        "official_url": "https://ssl.robocup.org/wp-content/uploads/2019/01/2016_ETDP_Parsian.pdf",
        "abstract": "The Parsian team placed among the top eight teams in the RoboCup 2015 Small Size League. This paper presents the current mechanical and electrical design, offensive and defensive tactics, and low-level skills. It covers new visual-planner features for open and set play, a revised defensive marking system, ball-manipulation skills, and improvements to ball and robot state estimation through profiling.",
        "citation": "Rahimi, M. M., Shirazi, M. M., Dajkhosh, S. P., et al. (2016). PARSIAN Extended Team Description for RoboCup 2016. RoboCup Small Size League.",
        "bibtex": """@techreport{rahimi2016parsian,\n  title = {PARSIAN Extended Team Description for RoboCup 2016},\n  author = {Rahimi, Mohammad Mahdi and Shirazi, Mohammad Mahdi and Dajkhosh, Seyede Parisa and Zolanvari, Alireza and Arfaee, Maziar and Kazemi Khoshkijari, Hamidreza and Abbasi Fashami, Amirhossein and Saeidi Shahrivar, Alireza and Khosravi, Mohammad Azam},\n  institution = {RoboCup Small Size League},\n  year = {2016}\n}""",
    },
    {
        "slug": "parsian-2015",
        "title": "PARSIAN Team Description for RoboCup 2015",
        "authors": ["Alireza Zolanvari", "Mohammad Mahdi Shirazi", "Seyede Parisa Dajkhosh", "Amir Mohammad Naderi", "Maziar Arfaee", "Mohammad Behbooei", "Hamidreza Kazemi Khoshkijari", "Erfan Tazimi", "Mohammad Mahdi Rahimi", "Alireza Saeidi Shahrivar"],
        "date": "2015",
        "year": "2015",
        "venue": "RoboCup Small Size League Team Description Papers",
        "venue_meta": ("citation_conference_title", "RoboCup 2015 Small Size League"),
        "official_url": "https://ssl.robocup.org/wp-content/uploads/2019/01/2015_TDP_Parsian.pdf",
        "abstract": "This team description paper presents the PARSIAN Small Size Soccer team's entry for RoboCup 2015. It describes the robots' mechanical, electrical, control, and software systems, including a new mechanical design, updates to the control system and visual planner, and enhancements to predefined plays.",
        "citation": "Zolanvari, A., Shirazi, M. M., Dajkhosh, S. P., et al. (2015). PARSIAN Team Description for RoboCup 2015. RoboCup Small Size League.",
        "bibtex": """@techreport{zolanvari2015parsian,\n  title = {PARSIAN Team Description for RoboCup 2015},\n  author = {Zolanvari, Alireza and Shirazi, Mohammad Mahdi and Dajkhosh, Seyede Parisa and Naderi, Amir Mohammad and Arfaee, Maziar and Behbooei, Mohammad and Kazemi Khoshkijari, Hamidreza and Tazimi, Erfan and Rahimi, Mohammad Mahdi and Saeidi Shahrivar, Alireza},\n  institution = {RoboCup Small Size League},\n  year = {2015}\n}""",
    },
]

PUBLIC_PREPRINTS = [
    {
        "year": "2026",
        "title": "Low-Rank Aggregation via Optimal Right-Space Projection",
        "authors": "Mohammad Mahdi Rahimi, Mahdi Heidari, Humaira Kousar, Daewon Seo, and Jaekyun Moon",
        "status": "Public preprint on OpenReview",
        "url": "https://openreview.net/forum?id=2hNK26yQee",
    },
    {
        "year": "2025",
        "title": "Reshape-then-Factorize: Communication-Efficient FL via Model-Agnostic Projection Optimization",
        "authors": "Mohammad Mahdi Rahimi, Younghyun Park, Humaira Kousar, Hasnain Irshad Bhatti, Dong-Jun Han, and Jaekyun Moon",
        "status": "Public preprint on OpenReview",
        "url": "https://openreview.net/forum?id=6zNODYRJvI",
    },
]


STYLE = """\
:root{--bg:#0b1020;--card:#121a33;--fg:#e9eefc;--muted:#a7b4d6;--acc:#8ab4ff;--border:#22325f;--code:#0a0f1f}
*{box-sizing:border-box}html{color-scheme:dark}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.62 Inter,system-ui,-apple-system,Segoe UI,sans-serif}
a{color:var(--acc)}main{max-width:920px;margin:auto;padding:42px 20px 80px}.nav{display:flex;gap:18px;flex-wrap:wrap;margin-bottom:30px}.card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:24px;margin:18px 0}
h1{font:800 clamp(2rem,6vw,3.2rem)/1.12 Georgia,serif;margin:.2rem 0 1rem}h2{font:700 1.35rem/1.25 Georgia,serif;margin-top:1.7rem}.authors{font-size:1.08rem}.meta,.note{color:var(--muted)}.actions{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0}.button{display:inline-block;padding:9px 13px;border:1px solid var(--border);border-radius:999px;text-decoration:none;background:#172650}.button.primary{background:#254b92;color:#fff}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:var(--code);border:1px solid var(--border);border-radius:10px;padding:14px}.work{padding:16px 0;border-bottom:1px solid var(--border)}.work:last-child{border:0}.work h2{margin:.1rem 0 .35rem}.tag{display:inline-block;border:1px solid var(--border);border-radius:999px;padding:3px 8px;color:var(--muted);font-size:.82rem}.footer{margin-top:36px;color:var(--muted);font-size:.9rem}@media print{body{background:#fff;color:#111}.card{border:1px solid #ccc}.nav,.actions{display:none}a{color:#111}}
"""


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def meta_tags(work: dict) -> str:
    tags = [
        f'<meta name="citation_title" content="{esc(work["title"])}">',
        *[f'<meta name="citation_author" content="{esc(author)}">' for author in work["authors"]],
        f'<meta name="citation_publication_date" content="{esc(work["date"])}">',
        f'<meta name="citation_pdf_url" content="{BASE}/publications/{work["slug"]}/paper.pdf">',
        f'<meta name="{esc(work["venue_meta"][0])}" content="{esc(work["venue_meta"][1])}">',
        '<meta name="citation_language" content="en">',
    ]
    tags.extend(f'<meta name="{esc(name)}" content="{esc(value)}">' for name, value in work.get("extra_meta", []))
    if work.get("doi"):
        tags.append(f'<meta name="citation_doi" content="{esc(work["doi"])}">')
    return "\n  ".join(tags)


def paper_page(work: dict) -> str:
    canonical = f'{BASE}/publications/{work["slug"]}/'
    schema = {
        "@context": "https://schema.org",
        "@type": "ScholarlyArticle",
        "headline": work["title"],
        "author": [{"@type": "Person", "name": name} for name in work["authors"]],
        "datePublished": work["date"].replace("/", "-") if len(work["date"]) > 4 else work["date"],
        "description": work["abstract"],
        "url": canonical,
        "encoding": {"@type": "MediaObject", "contentUrl": canonical + "paper.pdf", "encodingFormat": "application/pdf"},
        "sameAs": work["official_url"],
    }
    if work.get("doi"):
        schema["identifier"] = "https://doi.org/" + work["doi"]
    optional = []
    if work.get("code_url"):
        optional.append(f'<a class="button" href="{esc(work["code_url"])}">Code</a>')
    doi = f' · DOI: <a href="https://doi.org/{esc(work["doi"])}">{esc(work["doi"])}</a>' if work.get("doi") else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{esc(work['title'])}</title>
  <meta name="description" content="{esc(work['abstract'][:280])}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="../style.css">
  {meta_tags(work)}
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
<main>
  <nav class="nav"><a href="{BASE}/">Home</a><a href="../">All publications</a><a href="../bibliography.bib">BibTeX library</a></nav>
  <article class="card">
    <h1>{esc(work['title'])}</h1>
    <p class="authors">{esc(', '.join(work['authors']))}</p>
    <p class="meta">{esc(work['venue'])} · {esc(work['year'])}{doi}</p>
    <div class="actions"><a class="button primary" href="paper.pdf">Download PDF</a><a class="button" href="{esc(work['official_url'])}">Official record</a>{''.join(optional)}</div>
    <h2>Abstract</h2>
    <p>{esc(work['abstract'])}</p>
    <h2>Canonical citation</h2>
    <p>{esc(work['citation'])}</p>
    <pre>{esc(work['bibtex'])}</pre>
    <p class="note">Archive note: this author-hosted PDF preserves the visible pages of the official version. Only embedded document metadata was normalized so title and author fields match the title page.</p>
  </article>
  <p class="footer">Canonical publication page for citation indexing and bibliographic disambiguation.</p>
</main>
</body>
</html>
"""


def publications_index() -> str:
    preprints = "".join(
        f'<article class="work"><span class="tag">{esc(w["year"])}</span><h2><a href="{esc(w["url"])}">{esc(w["title"])}</a></h2><p>{esc(w["authors"])}</p><p class="meta">{esc(w["status"])}</p></article>'
        for w in PUBLIC_PREPRINTS
    )
    hosted = "".join(
        f'<article class="work"><span class="tag">{esc(w["year"])}</span><h2><a href="{esc(w["slug"])}/">{esc(w["title"])}</a></h2><p>{esc(", ".join(w["authors"]))}</p><p class="meta">{esc(w["venue"])}</p></article>'
        for w in WORKS
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Publications | Mohammad Mahdi Rahimi</title>
  <meta name="description" content="Canonical publications and research outputs by Mohammad Mahdi Rahimi.">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{BASE}/publications/">
  <link rel="stylesheet" href="style.css">
</head>
<body><main>
  <nav class="nav"><a href="../">Home</a><a href="bibliography.bib">BibTeX library</a><a href="software.html">Software credit</a></nav>
  <h1>Publications</h1>
  <p class="meta">Canonical title, author, date, and full-text links. Each hosted work has a separate static page and machine-readable citation metadata.</p>
  <section class="card"><h2>Public preprints</h2>{preprints}</section>
  <section class="card"><h2>Peer-reviewed papers, reports, and dissertation</h2>{hosted}</section>
  <section class="card"><h2>Additional research outputs</h2>
    <article class="work"><span class="tag">2019</span><h2><a href="https://www.researchgate.net/publication/335276487_Extended_Abstract_Multi-Agent_Architecture_for_Soccer_Robots_based_on_ROS">Multi-Agent Architecture for Soccer Robots based on ROS</a></h2><p>Mohammad Mahdi Rahimi, Alireza Zolanvari, and Mohammad Mahdi Shirazi</p><p class="meta">Extended abstract, FIRA RoboWorld Cup and Summit 2019. The external record remains canonical until an author PDF is recovered.</p></article>
  </section>
  <p class="footer">Last updated 1 September 2026.</p>
</main></body></html>
"""


def software_page() -> str:
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Software credit | Mohammad Mahdi Rahimi</title><meta name="robots" content="index,follow"><link rel="canonical" href="{BASE}/publications/software.html"><link rel="stylesheet" href="style.css"></head>
<body><main><nav class="nav"><a href="../">Home</a><a href="./">Publications</a></nav><h1>Software credit</h1>
<section class="card"><h2>Authored or co-created software</h2>
<article class="work"><h2><a href="https://github.com/ECSIM/opem">OPEM</a></h2><p>Co-creator and co-author of the JOSS paper. Paper citations belong to all four listed paper authors.</p></article>
<article class="work"><h2><a href="https://github.com/sepandhaghighi/qpage">QPage</a></h2><p>Co-creator of the software record with Sepand Haghighi. DOI: <a href="https://doi.org/10.5281/zenodo.265544">10.5281/zenodo.265544</a>.</p></article>
</section>
<section class="card"><h2>Repository contributions, not paper authorship</h2>
<article class="work"><h2><a href="https://github.com/RoboCup-SSL/grSim">grSim</a></h2><p>Developer and maintainer of later software versions. The original 2011 paper was authored by Valiallah Monajjemi, Ali Koochakzadeh, and Saeed Shiry Ghidary. Repository contribution credit must remain separate from that paper's authorship and citations.</p></article>
<article class="work"><h2><a href="https://github.com/sepandhaghighi/pycm">PyCM</a></h2><p>Repository contributor. The 2018 JOSS paper was authored by Sepand Haghighi, Masoomeh Jasemi, Shaahin Hessabi, and Alireza Zolanvari. Repository contribution credit must remain separate from that paper's authorship and citations.</p></article>
</section>
<p class="footer">This separation prevents accidental authorship or citation misattribution.</p></main></body></html>
"""


def sitemap() -> str:
    urls = [f"{BASE}/", f"{BASE}/publications/", f"{BASE}/publications/software.html"]
    urls += [f'{BASE}/publications/{w["slug"]}/' for w in WORKS]
    body = "".join(f"  <url><loc>{html.escape(url)}</loc><lastmod>2026-09-01</lastmod></url>\n" for url in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'


write(ROOT / "publications/style.css", STYLE)
for work in WORKS:
    write(ROOT / f'publications/{work["slug"]}/index.html', paper_page(work))
write(ROOT / "publications/index.html", publications_index())
write(ROOT / "publications/software.html", software_page())
write(ROOT / "publications/bibliography.bib", "\n\n".join(w["bibtex"] for w in WORKS) + "\n")
write(ROOT / "sitemap.xml", sitemap())
write(ROOT / "robots.txt", "User-agent: *\nAllow: /\n\nSitemap: https://mahi97.github.io/sitemap.xml\n")
