from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    """
    Rearrange the point_list to get a balance 3dbtree when it is input into the tree
    : complexity best: O(1) when the len[list[Point]] <= 17
    : complexity worst: O(n^4) when the len[list[Point]] > 17
    n = number of point in list[Point]
    """
    def make_ordering_aux(point_list):
        """
        Rearrange the points and append it into the result list
        : complexity worst & best: O(n^2)
        m = len(divided_group)
        n = len(point_list)
        """
        if len(point_list) == 0:
            return
        center_point = get_center_point(point_list)
        result.append(center_point)
        divided_groups = divide_group_by_center(point_list, center_point)

        for group in divided_groups:
            make_ordering_aux(group)

    def get_center_point(point_lst) -> Point:
        """
        get the centre point
        : complexity best & worst: O(n)
        """

        def get_center_point_aux(point_list) -> list:
            """
            get a list of points with percentiles ratio(a,a)
            : complexity best & worst: O(2n)
            n = point in point_list
            """
            percentiles1 = Percentiles()
            percentiles2 = Percentiles()
            percentiles3 = Percentiles()
            for point in point_list:
                percentiles1.add_point(point[0])
                percentiles2.add_point(point[1])
                percentiles3.add_point(point[2])

            points1 = percentiles1.ratio(1 / 9 * 100, 1 / 9 * 100)
            points2 = percentiles2.ratio(1 / 9 * 100, 1 / 9 * 100)
            points3 = percentiles3.ratio(1 / 9 * 100, 1 / 9 * 100)
            center_points = []
            for point in point_list:
                if (point[0] in points1) and (point[1] in points2) and (point[2] in points3):
                    center_points.append(point)
            return center_points

        while len(point_lst) > 8:
            point_lst = get_center_point_aux(point_lst)

        return point_lst[0]

    def divide_group_by_center(point_list, center_point) -> list[list]:
        """
        divide the point in point_list into their octants depends on the center_point
        : complexity best & worst: O(n)
        n = len(point_list)
        """
        ppp = []
        ppn = []
        pnp = []
        pnn = []
        nnn = []
        nnp = []
        npp = []
        npn = []

        for point in point_list:
            if (point[0] < center_point[0]) and (point[1] < center_point[1]) and (point[2] < center_point[2]):
                nnn.append(point)

            elif (point[0] < center_point[0]) and (point[1] > center_point[1]) and (point[2] < center_point[2]):
                npn.append(point)

            elif (point[0] < center_point[0]) and (point[1] < center_point[1]) and (point[2] > center_point[2]):
                nnp.append(point)

            elif (point[0] < center_point[0]) and (point[1] > center_point[1]) and (point[2] > center_point[2]):
                npp.append(point)

            elif (point[0] > center_point[0]) and (point[1] < center_point[1]) and (point[2] < center_point[2]):
                pnn.append(point)

            elif (point[0] > center_point[0]) and (point[1] < center_point[1]) and (point[2] > center_point[2]):
                pnp.append(point)

            elif (point[0] > center_point[0]) and (point[1] > center_point[1]) and (point[2] < center_point[2]):
                ppn.append(point)

            elif (point[0] > center_point[0]) and (point[1] > center_point[1]) and (point[2] > center_point[2]):
                ppp.append(point)

        arranged_point_list = [ppp, ppn, pnp, pnn, npp, nnp, npn, nnn]
        return arranged_point_list

    if len(my_coordinate_list) <= 17:  # ignore rearranging if the point is less than 18
        return my_coordinate_list
    else:
        result = []
        make_ordering_aux(my_coordinate_list)
        return result
