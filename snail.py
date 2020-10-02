def snail(matrix):

    if matrix == [[]]:
        return []

    if len(matrix) == 2:
        final_result = [matrix[0][0], matrix[0][1], matrix[1][1], matrix[1][0]]
        return final_result

    final_result = []

    def snail_for_3(matrix):
        result = []

        for num in matrix[0]:
            result.append(num)
        try:
            result.append(matrix[1][-1])
            result.append(matrix[2][-1])
            result.append(matrix[2][1])
            result.append(matrix[2][0])
            result.append(matrix[1][0])
            result.append(matrix[1][1])
        except:
            pass
        return result

    def cut_corners(matrix):

        result = []

        def flip_matrix(matrix):
            for row in range(len(matrix)):
                matrix[row] = matrix[row][::-1]
            matrix = matrix[::-1]
            return matrix

        while len(matrix) > 3:
            for num in matrix[0]:
                result.append(num)
            matrix.pop(0)
            for row in range(len(matrix)):
                result.append(matrix[row][-1])
                matrix[row].pop(-1)
            if len(matrix) > 3:
                matrix = flip_matrix(matrix)

        matrix = flip_matrix(matrix)

        return (result, matrix)

    if len(matrix) == 3:

        return snail_for_3(matrix)

    else:

        cut_corners_return = cut_corners(matrix)

        outside_numbers = cut_corners_return[0]
        matrix_left = cut_corners_return[1]

        final_result.extend(outside_numbers)
        final_result.extend(snail_for_3(matrix_left))

        return final_result
