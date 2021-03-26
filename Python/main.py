from kruskal import KruskalAlgorithm

Graph = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
         (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]

output_file = r"C:\Users\Kirill_07\Documents\_Study\Inform\GitHub\Algorithms\Python\output.txt"


def algo_kruskal():
    k = KruskalAlgorithm(Graph, output_file)

    k.kruskal()
    k.write("w")

if __name__ == '__main__':
    algo_kruskal()
