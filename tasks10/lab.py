import ast
import csv
import datetime
import os

import numpy


def fix_types(db: dict) -> dict:
    int_keys = ["id", "age", "user_id", "movie_id"]
    float_keys = ["score"]
    date_keys = ["release_date"]
    arr_int_keys = ["genre_ids"]

    for int_key in int_keys:
        if int_key in db:
            db[int_key] = int(db[int_key])

    for float_key in float_keys:
        if float_key in db:
            db[float_key] = float(db[float_key])

    for date_key in date_keys:
        if date_key in db:
            db[date_key] = datetime.date.fromisoformat(db[date_key])

    for arr_key in arr_int_keys:
        if arr_key in db:
            db[arr_key] = ast.literal_eval(db[arr_key])
    return db


def create_database(directory_path: str) -> dict:
    db = dict()
    for filename in os.listdir(directory_path):
        file_path = f"{directory_path}/{filename}"
        with open(file_path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            d = {}
            for row in reader:
                fixed_row = fix_types(row)
                d[int(row["id"])] = fixed_row
            db[filename[:-4]] = d
    return db


def get_movie(id: int, db: dict) -> str:
    return db["movies"][id]  # type: ignore[no-any-return]


def get_genre(id: int, db: dict) -> str:
    return db["genres"][id]  # type: ignore[no-any-return]


def get_user(id: int, db: dict) -> str:
    return db["users"][id]  # type: ignore[no-any-return]


def get_release_list(db: dict) -> list:
    table = db["movies"]
    release_title = []
    for id, movie_data in table.items():
        release_title += [[movie_data["release_date"], movie_data["title"]]]
    return sorted(release_title)


def est_movie(type: str, db: dict) -> str:
    release_list = get_release_list(db)
    if type == "oldest":
        return release_list[0]  # type: ignore[no-any-return]
    else:
        return release_list[-1]  # type: ignore[no-any-return]


def get_avg_score(db: dict) -> list:
    table = db["votes"]
    score_dict = {}  # type: ignore[var-annotated]
    for id, vote_data in table.items():
        vote = [vote_data["score"]]
        movie_id = vote_data["movie_id"]
        if movie_id in score_dict:
            score_dict[movie_id] += vote
        else:
            score_dict[movie_id] = vote

    avg_dict = {}
    for movie_id in score_dict:
        avg_dict[movie_id] = numpy.average(score_dict[movie_id])

    title_avg = []

    for movie_id, movie_data in db["movies"].items():
        title = movie_data["title"]
        avg = avg_dict[movie_id]
        title_avg += [[avg, movie_id, title]]

    for x in title_avg:
        db["movies"][x[1]]["average_score"] = x[0]

    return sorted(title_avg)


def est_score(type: str, db: dict) -> list:
    score_arr = get_avg_score(db)
    if type == "highest":
        return score_arr[-1]  # type: ignore[no-any-return]
    else:
        return score_arr[0]  # type: ignore[no-any-return]


def add_mentions_count(db: dict) -> None:
    for genre_id, genre_data in db["genres"].items():
        count = 0
        table = db["movies"]
        for movie_id, movie_data in table.items():
            genres_ids = movie_data["genre_ids"]
            if genre_id in genres_ids:
                count += 1
        db["genres"][genre_id]["mentions"] = count


def get_mentions_arr(db: dict) -> list:
    arr = []
    for genre_id, genre_data in db["genres"].items():
        arr += [[genre_data["mentions"], genre_data["name"]]]
    return sorted(arr)


def est_mentioned(type: str, db: dict) -> list:
    arr = get_mentions_arr(db)
    if type == "most":
        return arr[0]  # type: ignore[no-any-return]
    else:
        return arr[-1]  # type: ignore[no-any-return]


def main() -> None:
    db = create_database("database")
    print(
        f"The oldest movie in the database is: {est_movie('oldest', db)[1]}, year of production: {est_movie('oldest', db)[0]}"
    )
    print(
        f"The latest movie in the database is: {est_movie('latest', db)[1]}, year of production: {est_movie('latest', db)[0]}"
    )
    print(
        f"The words movie in the database is: {est_score('lowest', db)[1]}, average score: {est_score('lowest', db)[0]}"
    )
    print(
        f"The best movie in the database is: {est_score('highest', db)[1]}, average score: {est_score('highest', db)[0]}"
    )
    add_mentions_count(db)


if __name__ == "__main__":
    main()
