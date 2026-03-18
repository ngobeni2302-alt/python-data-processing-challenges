def separate_scores(scores):
    math_score = []
    science_score = []

    for math, science in scores:
        math_score.append(math)
        science_score.append(science)
    
    return math_score, science_score


def split_coordinates(coords):

    new = [x for x, y in coords]
    news = [y for x, y in coords]

    return new, news

def build_student_index(students):
    return {student : students.index(student) for student in students}


def map_items_to_position(items):
    dict = {}
    for i, item in enumerate(items):
        dict[item] = i
    return dict


def normalize_tags(tags):
    return set(x.lower() for x in tags)

def clean_usernames(usernames):
    new_usernames = set()

    for username in usernames:
        new_usernames.add(username.lower())
    return new_usernames

def group_by_city(people):
    """
    [
    {"name": "Alice", "city": "Cape Town"},
    {"name": "Bob", "city": "Cape Town"}
]
    """
    city_people = {}

    for i in people:
        name = i["name"]
        people = i["city"]

        if people not in city_people:
            city_people[people] = []
        city_people[people].append(name)
    return city_people


def categorize_books(books):
    """
    [
    {"title": "Book1", "genre": "Fiction"},
    {"title": "Book2", "genre": "Horror"},
    {"title": "Book1", "genre": "Fiction"},
    {"title": "Book2", "genre": "Romance"}    
]
    """

    books_read = {}

    for book in books:
        title = book["title"]
        genre = book["genre"]

        if genre not in books_read:
            books_read[genre] = []
        books_read[genre].append(title)
    return books_read

print(categorize_books([
    {"title": "Book1", "genre": "Fiction"},
    {"title": "Book2", "genre": "Horror"},
    {"title": "Book1", "genre": "Fiction"},
    {"title": "Book2", "genre": "Romance"}    
]))
