import copy


class Node(object):
    def __init__(self, key, remain=int(1e9), data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.remain = remain  # 밑으로 남은 최대 글자 개수


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        n = len(string)

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char, n)
            curr_node = curr_node.children[char]

            if curr_node.remain < n:  # 남은 글자 개수가 더 많으면 갱신
                curr_node.remain = n
            n -= 1

        curr_node.data = string

    # 접미사로 ?가 있는 경우
    def suffix_q(self, string):
        curr_node = self.head
        result = 0
        n = len(string)

        children_list = []
        is_first = 1
        for char in string:

            if char == '?':  # ?면
                if is_first == 1:  # 처음이면
                    children_list = list(curr_node.children.values())
                    is_first = 0
                else:
                    temp = []
                    for node in children_list:  # 현재 단계의 모든 자식들 찾기
                        if node.remain < n:  # 글자 수 맞는게 없다면
                            continue
                        temp += list(node.children.values())
                    children_list = copy.deepcopy(temp)

            else:  # 문자면
                if char in curr_node.children.keys():
                    curr_node = curr_node.children[char]
                    if curr_node.remain < n:  # 글자 수 맞는게 없다면
                        return 0
                else:
                    return 0

            n -= 1

        # 조건에 맞는 문자 결과에 넣기
        for node in children_list:
            if node.data:
                result += 1

        return result

    # 접두사로 ?가 있는 경우
    def prefix_q(self, string):
        curr_node = self.head
        result = 0
        n = len(string) + 1

        # ? 접두사 확인 & 문자 찾기
        children_list = [curr_node]
        for char in string:
            if char == '?':  # ?이면
                temp = []
                for node in children_list:  # 현재 단계의 모든 자식들 찾기
                    if node.remain < n:  # 글자 수 가능한게 자식에 없으면
                        continue
                    temp += list(node.children.values())
                children_list = copy.deepcopy(temp)
            else:  # 문자면
                temp = []
                for node in children_list:  # 문자 자식 찾기
                    if node.remain < n:  # 글자 수 가능한게 자식에 없으면
                        continue

                    if char in node.children.keys():
                        temp.append(node.children[char])
                children_list = copy.deepcopy(temp)

            n -= 1

        # 조건에 맞는 문자 결과에 넣기
        for node in children_list:
            if node.data:
                result += 1

        return result


def solution(words, queries):
    answer = []
    trie = Trie()

    # 맨 앞글자로 trie 사전 구성
    for word in words:
        trie.insert(word)

    # 쿼리
    for query in queries:
        if query[0] == '?':  # ?가 접두사
            response = trie.prefix_q(query)
            answer.append(response)

        else:  # ?가 접미사
            response = trie.suffix_q(query)
            answer.append(response)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))
