from datetime import date
from django.shortcuts import render

# Create your views here.

all_posts = [
    {"slug": "hide-in-the-mountain", "image": "mountains.jpg",
        "author": "Karam", "date": date(2022, 8, 21), "title": "Mountain Hiking",
     "excerpt": " Mountain hiking is a thrilling adventure that offers breathtaking views, physical challenges, and a deep connection with nature. It requires endurance, preparation, and a sense of exploration.",
        "content": """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry.
        Lorem Ipsum has been the industry's standard dummy text ever since the
        1500s, when an unknown printer took a galley of type and scrambled it to
        make a type specimen book. It has survived not only five centuries, but also
        the leap into electronic typesetting, remaining essentially unchanged.

            It was popularised in the 1960s with the release of Letraset sheets
        containing Lorem Ipsum passages, and more recently with desktop publishing
        software like Aldus PageMaker including versions of Lorem Ipsum.

        It is a long established fact that a reader will be distracted by the
        readable content of a page when looking at its layout. The point of using
        Lorem Ipsum is that it has a more-or-less normal distribution of letters, as
        opposed to using 'Content here, content here', making it look like readable
        English. Many desktop publishing packages and web page editors now use Lorem
        Ipsum as their default model text, and a search for 'lorem ipsum' will
        uncover many web sites still in their infancy. Various versions have evolved
        over the years, sometimes by accident, sometimes on purpose (injected humour
        and the like).
        """},
    {"slug": "Programming", "image": "coding.jpg",
     "author": "Karam", "date": date(2023, 6, 5), "title": "Programming is fun",
     "excerpt": "Programming empowers innovation, unlocks possibilities, solves challenges, automates tasks, fuels technology advancement, and drives digital transformation globally.",
     "content": """
        Programming is the art and science of instructing computers to perform specific tasks. It is a creative process that involves designing, coding, and debugging software to achieve desired outcomes. Programmers use programming languages like Python, Java, and C++ to communicate with computers and develop software applications, websites, and systems. With precise instructions, programmers can bring ideas to life and create functional and efficient solutions.

        Programming plays a crucial role in various industries and domains. From finance and healthcare to entertainment and communication, programming enables innovation and drives progress. Programmers analyze problems, break them down into smaller manageable components, and devise algorithms and logical structures to solve them. Through programming, complex processes can be automated, data can be analyzed and visualized, and new technologies can be developed. The impact of programming can be seen in the advancements of artificial intelligence, machine learning, and blockchain technology, among others.

        Being a programmer requires continuous learning and adaptation. Technology is constantly evolving, and programmers need to stay up to date with the latest tools, languages, and frameworks. Problem-solving skills, attention to detail, and logical thinking are essential for programmers to write clean and efficient code. Collaboration and communication skills are also important as programmers often work in teams, sharing knowledge and ideas to create robust software solutions. With dedication and passion, programmers have the opportunity to shape the future, make a positive impact, and contribute to the ever-growing digital landscape.
        """},
    {"slug": "Woods", "image": "woods.jpg",
     "author": "Karam", "date": date(2023, 2, 5), "title": "Woods is useful",
     "excerpt": "Lush, serene, natural, mysterious, tranquil, abundant, sheltering, rejuvenating, diverse, wildlife, earthy, rustic, enchanting, refreshing, timeless.",
     "content": """
        Woods are captivating natural environments filled with an enchanting aura. The dense canopy of trees creates a sense of seclusion, providing a sanctuary from the bustling world. The sunlight filtering through the leaves creates a mesmerizing play of light and shadows, casting a tranquil and soothing ambiance. Walking through the woods, one can experience a profound connection with nature, immersing in the symphony of rustling leaves and the chorus of birdsong.

        Woods are havens of biodiversity, teeming with a rich array of flora and fauna. They provide a habitat for countless species, offering shelter, food, and protection. From towering ancient trees to delicate wildflowers, the woods showcase nature's artistic palette. Exploring the woods unveils a tapestry of life, where each step reveals hidden wonders, from vibrant mushrooms to elusive woodland creatures, adding an element of excitement and discovery to the journey.

        The woods hold a certain mystique and timeless appeal. They have been the setting for countless tales and legends, evoking a sense of wonder and adventure. Camping under the starry night sky, telling stories around a crackling campfire, and breathing in the scent of earth and pine needles evoke a deep connection to the natural world. The woods offer an escape from the fast-paced modern life, allowing one to unwind, recharge, and find solace in the simplicity and beauty of nature.
        """}
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    lastest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": lastest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post":  identified_post})
