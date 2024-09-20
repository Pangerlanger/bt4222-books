# Data Description

### df_interactions

user_id (String): unique ID of users

book_id (Integer): unique ID of books

review_id (String): unique ID of review by a user for a book

is_read (Boolean): True or False value to indicate whether the user has read the book

rating (Integer): rating given by the user, a score out of 5

review_text_incomplete: ?

date_added: ?

date_updated: ?

read_at (DateTime): the date that user finished reading the book

started_at (DateTime): the date that user started reading the book

---

### df_children_books

isbn: (String) - The International Standard Book Number, in this case, a 10-digit ISBN identifier for the book.

text_reviews_count: (Integer) - The number of text reviews available for the book.

series: (Array) - Represents if the book is part of a series. If a book is not a part of a series, it is empty.

country_code: (String) - The country code, indicating the origin or country associated with the book.

language_code: (String) - The language code for the book.

popular_shelves: (Array of Objects) - A list of popular shelves where the book appears, with each shelf being represented by an object containing:

1. count: (Integer) - The number of times the book appears in that shelf.
2. name: (String) - The name of the shelf (e.g., "picture-books", "ducks").

asin: (String) - Amazon Standard Identification Number.

is_ebook: (Boolean) - Indicates whether the book is an eBook.

average_rating: (Float) - The average rating of the book.

kindle_asin: (String) - The Kindle ASIN identifier. This is empty in the record.

similar_books: (Array) - A list of similar books as determined in the review.

description: (String) - A text description of the book.

format: (String) - The format of the book, whether it's a hardcover or softcopy version.

link: (String) - A URL linking to the book's page on Goodreads.

authors: (Array of Objects) - A list of authors associated with the book, each represented as an object containing:

1. author_id: (String) - The unique ID of the author.

2. role: (String) - The role of the author in the book (e.g., writer, photographer).

publisher: (String) - The name of the publisher

num_pages: (Integer) - The number of pages in the book

publication_day: (Integer) - The day of the month the book was published.

isbn13: (String) - The 13-digit ISBN identifier of the book.

publication_month: (Integer) - The month in which the book was published.

edition_information: (String) - Information about the edition of the book.

publication_year: (Integer) - The year the book was published.

url: (String) - The Goodreads URL for the book's details page.

image_url: (String) - The URL for the book's cover image.

book_id: (String) - The unique ID of the book on Goodreads.

ratings_count: (Integer) - The number of ratings the book has received.

work_id: (String) - ID used to identify each author's piece of work

title: (String) - Title of the book.

title_without_series: (String) - Title of the book without mentioning the series name.

---

### df_reviews

user_id: (String) - A unique identifier representing the user who submitted the review.

book_id: (String) - A unique identifier for the book being reviewed.

review_id: (String) - A unique identifier for the specific review.

rating: (Integer) - The rating given to the book by the user, typically on a scale of 1 to 5.

review_text: (String) - The text content of the user's review.

date_added: (Datetime) - The date and time when the review was first added to the system.

date_updated: (Datetime) - The date and time when the review was last updated.

read_at: (Datetime) - The date when the user completed reading the book.

started_at: (Datetime) - The date when the user began reading the book.

n_votes: (Integer) - The number of upvotes or helpful votes the review has received.

n_comments: (Integer) - The number of comments the review has received.
