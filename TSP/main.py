if __name__ == '__main__':
    from TSP.greedy_func import solve_tsp

    # Prepare the square symmetric distance matrix for 3 nodes:
    #  Distance from 0 to 1 is 1.0
    #                1 to 2 is 3.0
    #                0 to 2 is 2.0

    D = [[0, 1.0, 2.0],[1.0, 0, 3.0],[2.0, 3.0, 0]]
    D2 = [[0, 4.0, 2.0], [4.0, 0, 3.0], [2.0, 3.0, 0]]
    D3 = [[0, 5.0, 1.0, 2.0, 3.0],
          [5.0, 0, 2.0, 4.0, 3.0],
          [1.0, 2.0, 0, 6.0, 1.0],
          [2.0, 4.0, 6.0, 0, 7.0],
          [3.0, 3.0, 1.0, 7.0, 0]]

    tmp = solve_tsp(D)
    tmp2 = solve_tsp(D2)
    tmp3 = solve_tsp(D3)

    # will print [1,0,2], path with total length of 3.0 units
    print(tmp)
    print(tmp2)
    print(tmp3)
