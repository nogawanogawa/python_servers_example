from concurrent import futures
import grpc
from pb import cosine_similarity_pb2
from pb import cosine_similarity_pb2_grpc
from cosine_similarity.application import Similarity


class CosineSim(cosine_similarity_pb2_grpc.CosineSimServiceServicer):

    def __init__(self) -> None:
        super().__init__()
        self.sim = Similarity()

    def calc_cosine_sim(self, request, context):
        v1 = request.v1
        v2 = request.v2
        return cosine_similarity_pb2.CosineSimResponse(
            cosinesim=self.sim.calculate_similarity(v1, v2)
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cosine_sim = CosineSim()
    cosine_similarity_pb2_grpc.add_CosineSimServiceServicer_to_server(
        cosine_sim, server
    )

    server.add_insecure_port('[::]:5001')
    server.start()
    print("server started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
