def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    name = {}
    report_dict = {}

    for i in range(len(id_list)):
        name[id_list[i]] = i

    for nick in report:
        a, b = nick.split()
        if b not in report_dict:
            report_dict[b] = [0, []]
        report_dict[b][0] += 1
        report_dict[b][1].append(name[a])

    for key, value in report_dict.items():
        if value[0] >= k:
            for nick in value[1]:
                answer[nick] += 1

    return answer
