intersection_points = set()


def calc_intersection(line0, line1):
    global intersection_points

    m0 = (line0[0][1] - line0[1][1]) / (line0[0][0] - line0[1][0])
    m1 = (line1[0][1] - line1[1][1]) / (line1[0][0] - line1[1][0])

    if m0 - m1 == 0:
        return

    x = ((m0 * line0[1][0]) - (m1 * line1[1][0]) - line0[1][1] + line1[1][1]) / (m0 - m1)

    if (line0[0][0] <= x) and (line0[1][0] >= x) and \
       (line1[0][0] <= x) and (line1[1][0] >= x):
        intersection_points.add(x)


def calc_max_line(graphs, x_range):
    global intersection_points
    max_lines = []

    for p in graphs:
        if p[-1][0] != x_range:
            p.append([p[-1][0], p[-1][1]])
            p.append([x_range, p[-1][1]])
        if p[0][0] != 0:
            p.insert(0, [p[0][0], 0])
            p.insert(0, [0, 0])

    for p in graphs:
        intersection_points.add(p[0][0])

        for n in range(1, len(p)):
            intersection_points.add(p[n][0])

            for q in graphs:
                mq = 0
                for m in range(1, len(q)):
                    mq += 1
                    if p[n - 1][0] <= q[m][0]:
                        if (p[n - 1][0] == q[m - 1][0]) and (p[n][0] == q[m][0]):
                            if (p[n - 1][1] == q[m - 1][1]) and (p[n][1] == q[m][1]):
                                mq = len(q)
                                break
                            else:
                                calc_intersection([p[n - 1], p[n]], [q[m - 1], q[m]])

                                mq = len(q)
                                break
                        break
                for m in range(mq, len(q)):
                    calc_intersection([p[n - 1], p[n]], [q[m - 1], q[m]])

                    if p[n][0] < q[m - 1][0]:
                        break

    intersection_points = sorted(intersection_points)

    #if intersection_points[0] != 0:
    #    intersection_points.insert(0, 0)

    for n in range(0, len(intersection_points) - 1):
        candidate_list = []

        for p in graphs:
            for m in range(1, len(p)):
                if p[m][0] > intersection_points[n]:
                    if p[m][0] - p[m - 1][0] != 0:
                        candidate_list.append([[p[m - 1], p[m]], (((p[m][1] - p[m - 1][1]) / (p[m][0] - p[m - 1][0])) * (((intersection_points[n] + intersection_points[n + 1]) * 0.5) - p[m][0] ) + p[m][1])])
                    else:
                        candidate_list.append([[p[m - 1], p[m]], p[m][1]])
                    break

        j = 0
        for p in range(1, len(candidate_list)):
            if candidate_list[p][1] > candidate_list[j][1]:
                j = p

        for k in [n, n + 1]:
            max_lines.append([intersection_points[k], (((candidate_list[j][0][1][1] - candidate_list[j][0][0][1]) / (candidate_list[j][0][1][0] - candidate_list[j][0][0][0])) * (intersection_points[k] - candidate_list[j][0][0][0])) + candidate_list[j][0][0][1]])

    return max_lines
