def solution(genres, plays):
    answer = []
    length = len(genres)

    genre_dict = dict()
    for i in range(length):
        genre = genres[i]
        play = plays[i]

        if genre in genre_dict.keys():
            genre_dict[genre][0] += play
            genre_dict[genre].append((i, play))
        else:
            genre_dict[genre] = [play, (i, play)]

    # 장르별 내림차순 정렬
    genres_info = sorted(genre_dict.items(), key=lambda x: x[1][0], reverse=True)

    for genre, info in genres_info:
        song_list = info[1:]  # 총 play 제외 리스트
        song_list.sort(key=lambda x: (-x[1], x[0]))  # play 내림차순 정렬 (같으면 index 오름차순)
        for song in song_list[:2]:
            answer.append(song[0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
